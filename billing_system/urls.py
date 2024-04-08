from django.contrib import admin
from django.urls import path
from . import views

from .views import (
    EmployeeListCreate, EmployeeRetrieveUpdateDestroy,
    ProductListCreate, ProductRetrieveUpdateDestroy,
    CustomerListCreate, CustomerRetrieveUpdateDestroy,
    BillListCreate, BillRetrieveUpdateDestroy
)

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
    path('bills/', BillListCreate.as_view(), name='bill-list-create'),
    path('bills/<int:pk>/', BillRetrieveUpdateDestroy.as_view(), name='bill-retrieve-update-destroy'),

    path('register',views.register,name="register"),
    path('',views.loginpage,name="loginpage"),
    path('logoutUser',views.logoutUser,name='logoutUser'),
]
