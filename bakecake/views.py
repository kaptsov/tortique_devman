from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, OrderForm, CustomerForm
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


class UserFormView(View):

    form_class = UserForm
    template_name = 'registration/register.html'

    # получаем форму
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # посылаем данные
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            ###
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('exam:index')

        return render(request, self.template_name, {'form': form})

