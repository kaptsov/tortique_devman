from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.edit import FormView
from .forms import MyForm, OrderForm, CustomerForm
from .models import Orders, Customers


def index(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        customer_form = CustomerForm(request.POST)
        print(order_form.errors)
        print(customer_form.errors)
        if order_form.is_valid() and customer_form.is_valid():
            customer = customer_form.save()
            order = order_form.save(commit=False)
            print(dir(order))

    order_form = OrderForm()
    customer_form = CustomerForm()

    data = {
        'form': order_form,
        'customer_form': customer_form
    }
    return render(request, 'public/index.html', data)


class MyRegisterFormView(FormView):
    form_class = MyForm

    success_url = 'public/lk.html'
    template_name = 'registration/rega.html'

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

