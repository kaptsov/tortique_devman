from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


def index(request):
    return render(request, 'public/index.html')


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