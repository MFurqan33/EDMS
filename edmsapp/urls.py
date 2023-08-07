from django.contrib import admin  #password and user = admin admin  user1=django123#
from django.urls import path

from edmsapp import views
from django.contrib.auth import views as auth_views  
# from .views import OrderView

 

urlpatterns = [
path("home",views.home,name='home'),
path("",views.order,name='order'),
# path('', OrderView.as_view(), name='order'), #views index function 
path('payment_page/<int:order_id>/', views.payment_page, name='payment_page'),
 path('payment_success/', views.payment_success, name='payment_success'),
path("contact",views.contact,name='contact'),
path("ordertable",views.Ordertable,name='ordertable'),
path('cancel_order/<int:id>/', views.cancel_order, name='cancel_order'),
path('invoice', views.invoice_page, name='invoice'),
path('invoiceview/<str:invoice_number>/', views.invoiceview, name='invoiceview'),


 

]
