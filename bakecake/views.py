from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import UserForm, OrderForm, CustomerForm
from django.urls import reverse
from .models import Orders, User, Levels, Forms, Topping, Decors, Berries
from django.forms.models import inlineformset_factory


def cart(request):
    user = User.objects.get(username=request.user.username)
    user_orders = Orders.objects.filter(customer=user)
    context = {
        'user': user,
        'user_orders': user_orders
    }

    return render(request, 'login/lk.html', context)


def index(request):

    levels = Levels.objects.all()
    forms = Forms.objects.all()
    toppings = Topping.objects.all()
    berries = Berries.objects.all()
    decors = Decors.objects.all()

    order_form_set = inlineformset_factory(User, Orders, form=OrderForm)
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)
        new_order = order_form.save()
        print(new_order.level)
       # print(levels.select_related())
        new_customer = customer_form.save()
        order_inline_formset = order_form_set(
            request.POST,
            request.FILES,
            instance=new_customer
        )
        order_inline_formset.save()

    order_form = OrderForm()
    customer_form = CustomerForm()

    context = {
        'levels': levels,
        't_forms': forms,
        "toppings": toppings,
        "berries": berries,
        "decors": decors,
        'form': order_form,
        'customer_form': customer_form
    }

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        print(user)
        context['is_auth'] = True
        context['username'] = request.user.username
        context['user_first_name'] = user.first_name
        context['user_email'] = user.email

    return render(request, 'public/index.html', context)


class UserFormView(View):

    form_class = UserForm
    template_name = 'registration/rega.html'

    # ???????????????? ??????????
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # ???????????????? ????????????
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))