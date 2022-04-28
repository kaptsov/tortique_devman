from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import MyForm


def index(request):
    return render(request, 'public/index.html')


def lk(request):
    return render(request, 'public/lk.html')


class MyRegisterFormView(FormView):
    form_class = MyForm

    success_url = 'public/lk.html'
    template_name = 'registration/rega.html'

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)
