from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.urls import reverse
from .models import Orders, Customers


def cart(request):
    return render(request, 'login/lk.html')


def index(request):

    form_class = UserForm
    if request.method == 'POST':
        print(dict(request.POST.items()))
        form = form_class(request.POST)
        print(form)
    return render(request, 'public/index.html')


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
    return HttpResponseRedirect(reverse("index"))