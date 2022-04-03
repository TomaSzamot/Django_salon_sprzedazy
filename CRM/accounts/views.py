from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm, ProductForm, ClientForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group



@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'accounts/login.html', context )

@unauthenticated_user
def register_page(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Client.objects.create(
                user = user,
                # name = user.username,
            )
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context )

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):

    orders = Order.objects.all()
    clients = Client.objects.all()
    orders_sold = orders.filter(status = "sold").count()
    orders_delivered = orders.filter(status = "available").count()
    orders_pending = orders.filter(status = "reserved").count()

    context = {'orders': orders, 'clients': clients, 'orders_sold': orders_sold,
               'orders_delivered': orders_delivered, 'orders_pending': orders_pending}

    return render(request, 'accounts/dashboard.html', context )

def user_Page(request):

    orders = request.user.client.order_set.all()

    context = {'orders': orders}
    return render(request, 'accounts/user.html', context )

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products_key': products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def client(request, pk):

    client = Client.objects.get(id=pk)
    orders = client.order_set.all()
    orders_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'client': client,'orders':orders, 'orders_count': orders_count, 'myFilter': myFilter }

    return render(request, 'accounts/client.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_client(request):
    form_client = ClientForm()
    if request.method == "POST":

        form_client = ClientForm(request.POST)
        if form_client.is_valid():
            form_client.save()
            return redirect('/')

    context = {'form_client': form_client}
    return render(request, 'accounts/client_form.html', context)

def create_car(request):
    form_car = ProductForm()
    if request.method == "POST":

        form_car = ProductForm(request.POST)
        if form_car.is_valid():
            form_car.save()
            return redirect('/')

    context = {'form_car': form_car}
    return render(request, 'accounts/product_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request):
    form = OrderForm()
    if request.method == "POST":

        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":

        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_client(request):

    context= {'create_client': create_client}
    return render(request, 'accounts/client_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):

    order = Order.objects.get(id=pk)
    context = {'item': order}
    if request.method == "POST":
        order.delete()
        return redirect('/')

    return render(request, 'accounts/delete.html', context)

