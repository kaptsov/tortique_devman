from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.urls import reverse
from .models import Orders, Customers, Levels, Forms, Topping, Decors, Berries


def cart(request):
    return render(request, 'login/lk.html')


def index(request):

    levels = Levels.objects.all()
    forms = Forms.objects.all()
    toppings = Topping.objects.all()
    berries = Berries.objects.all()
    decors = Decors.objects.all()

    return render(request, 'public/index.html', context={
        'levels': levels,
        't_forms': forms,
        "toppings": toppings,
        "berries": berries,
        "decors": decors

    })


class UserFormView(View):

    form_class = UserForm
    template_name = 'registration/rega.html'

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

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))