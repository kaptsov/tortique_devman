from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.edit import FormView
from .forms import MyForm, OrderForm, CustomerForm
from .models import Orders, Customers


def index(request):
    if request.method == 'POST':
        print(dict(request.POST.items()))
    return render(request, 'public/index.html')


class MyRegisterFormView(FormView):
    form_class = MyForm

    success_url = 'public/lk.html'
    template_name = 'registration/rega.html'

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

