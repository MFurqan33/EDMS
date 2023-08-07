from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from datetime import datetime
from edmsapp.models import Contact,Order,Price,stockAvailable
from users.models import UserDetail
from django.contrib.auth.models import User
from decimal import Decimal
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')


def order(request):
    stock_available = stockAvailable.objects.first()
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        quantity = Decimal(quantity)
        price_obj = get_object_or_404(Price)
        price = price_obj.price  # Access the price value from the Price object
       
        payment = Decimal(quantity) * price
        address = request.POST.get('address')    
        # print(quantity,price,payment,address,'dasjfkasjfljlasjfljalsdjflkasjfkjsafjasj')
        stock_available = stockAvailable.objects.first()

        if stock_available.Stock<quantity:
            messages.error(request, f"Your Order quantity is more than the available Quantity : \n You Entered : {quantity} , Available :{stock_available.Stock} ")
            return redirect('order')

        # Create a new Order object and save it to the database
        order = Order(user=request.user, quantity=quantity, payment=payment, address=address,price=price, date=datetime.today())
        order.save()
        request.session['order_id'] = order.id

        # stock_available.Stock -= quantity   #Problem: Stock Quantity minus horahi thi without payment 
        # stock_available.save()              # So we updated Stock quantity in payment view 

        return redirect(reverse('payment_page', args=[order.id]))
        # return redirect('order_success')  # Redirect to a success page or any other desired URL

    context={'stock_available':stock_available}
    return render(request,'index.html',context)  


def payment_page(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        # Perform the payment processing here
        # Update the 'paid' to True
        order.paid = True
        order.save()

        stock_available = stockAvailable.objects.first()
        stock_available.Stock -= order.quantity
        stock_available.save()

        # Redirect to a success page or any other desired URL
        return redirect('payment_success')

    return render(request,'payment_page.html', {'order': order})


def generate_invoice_number():
    prefix = 'INV'
    current_date = datetime.now().strftime('%Y%m%d')
    counter = Order.objects.count() + 1
    invoice_number = f'{prefix}-{current_date}-{counter:04d}'
    return invoice_number

def payment_success(request):
    order_id = request.session.get('order_id')  # Assuming you have stored the order ID in the session
    order = get_object_or_404(Order, id=order_id)
    
    # Generate an invoice number (you can use any logic here)
    invoice_number = generate_invoice_number()
    
    # Create an Invoice object and associate it with the order
    order.invoice_number = invoice_number
    order.save()
    # Clear the session data
    del request.session['order_id']

    return render(request, 'payment_success.html', {'order': order})

def invoice_page(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)  # Retrieve the list of orders from the database
        

        context = {
            'orders': orders,  # Pass the orders queryset to the template context    
        }
        
        return render(request,'invoice.html',context)
    else:
        return redirect('login')
    
def invoiceview(request, invoice_number):
    order = get_object_or_404(Order, invoice_number=invoice_number)
    price=Price.objects.get()
    mobile=UserDetail.objects.get(user=request.user)
    context={
        'order': order,
        'price':price,
        'mobile':mobile,
    }
    return render(request, 'invoiceview.html', context) 
 
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def Ordertable(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)  # Retrieve the list of orders from the database
        
        context = {
            'orders': orders  # Pass the orders queryset to the template context
        }
        
        return render(request, 'ordertable.html', context)
    else:
        return redirect('login')


def cancel_order(request, id):
    try:
        order = Order.objects.get(id=id)
        # Performing cancellation logic 
        # you can update the order status to "Canceled"
        order.delivery_status = 'cancelled'
        order.save()
        # Redirect to the order list page or a success page
        return redirect('ordertable')
    except Order.DoesNotExist:
        # Handle the case when the order does not exist
        return redirect('order_list')
    

        

       