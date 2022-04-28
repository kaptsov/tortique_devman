from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, OrderForm, CustomerForm
from django.forms.models import inlineformset_factory
from .models import Orders, Customers


def index(request):
    OrderFormSet = inlineformset_factory(Customers, Orders, form=OrderForm)
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        print(customer_form)
        if customer_form.is_valid:
            new_customer = customer_form.save()
            order_inline_formset = OrderFormSet(
                request.POST,
                request.FILES,
                instance=new_customer
            )
            print(order_inline_formset)
            order_inline_formset.save()

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

