from django.shortcuts import redirect, render
from h11 import Response
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Employee, Product, Customer, Bill
from .serializers import EmployeeSerializer, ProductSerializer, CustomerSerializer, BillSerializer

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Employee.objects.all()
    #     else:
    #         return Employee.objects.none()

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     if not queryset.exists():
    #         return redirect('loginpage')
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BillListCreate(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        data1 = Employee(username=username,password=password)
        data1.save()
        user = User.objects.create_user(username=username, password=password)
        user.save()
        print(data1,user)
        return redirect('loginpage')
        
    return render(request,'register.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        curr_user = authenticate(username=username, password=password)
        print(curr_user)
        if curr_user is not None:
            login(request, curr_user)
            return redirect('bill-list-create')
        else:
            return render(request, 'login.html')
    return render(request,'login.html')

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('loginpage')