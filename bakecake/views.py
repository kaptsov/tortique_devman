from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import MyForm, OrderForm, CustomerForm
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


class MyRegisterFormView(FormView):
    form_class = MyForm

    success_url = 'public/lk.html'
    template_name = 'registration/rega.html'

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

