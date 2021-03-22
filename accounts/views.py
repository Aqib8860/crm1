from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .decorators import *
from .forms import *
from .models import *


@unauthenticated_user
def register(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('accounts:login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_page(request):

    form = UserLoginForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:home')
        else:
            messages.info(request, 'Username OR Password is Incorrect')

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='accounts:login')
@admin_only
def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)


@login_required(login_url='accounts:login')
@admin_only
def customer(request, cus_id):
    customer = get_object_or_404(Customer, pk=cus_id)
    orders = customer.order_set.all()
    # search_filter = OrderFilter()
    # total_orders = orders.customer_set.all().count
    context = {
        'customer': customer,
        'orders': orders,
        # 'search_filter': search_filter,
    }
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='accounts:login')
@admin_only
def create_order(request, cus_id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = get_object_or_404(Customer, pk=cus_id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('accounts:customer', args=cus_id))
    context = {'formset': formset}
    return render(request, 'accounts/create_order_form.html', context)


@login_required(login_url='accounts:login')
@admin_only
def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/create_order_form.html', context)


@login_required(login_url='accounts:login')
@admin_only
def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete_order.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['customer'])
def user_page(request):
    orders = request.user.customer.order_set.all()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
    }
    return render(request, 'accounts/user.html', context)


def user_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/user_settings.html', context)
