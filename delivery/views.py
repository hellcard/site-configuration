from django.shortcuts import render

from .models import Category, DeliveryModel
# Create your views here.

from django.views.generic.edit import CreateView
from .forms import DeliveryForm
from django.urls import reverse_lazy

from django.conf import settings

def main(request):
    if settings.SITE_TITLE == '' or settings.SITE_TITLE == None:
        site_title = 'delivery'
    else:
        site_title = settings.SITE_TITLE
    deliveries = DeliveryModel.objects.all()
    categories = Category.objects.all()
    return render(request, 'delivery/main.html', {'deliveries' : deliveries, 'categories' : categories, 'site_title' : site_title})

class DeliveryCreateForm(CreateView):
    template_name = 'delivery/add.html'
    form_class = DeliveryForm
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if settings.SITE_TITLE == '' or settings.SITE_TITLE == None:
            context['site_title'] = 'delivery'
        else:
            context['site_title'] = settings.SITE_TITLE
        return context
    
    
def delivery(request, del_id):
    categories = Category.objects.all()
    deliveries = DeliveryModel.objects.filter(category=del_id)
    cur_del = Category.objects.get(pk = del_id)
    if settings.SITE_TITLE == '' or settings.SITE_TITLE == None:
        site_title = 'delivery'
    else:
        site_title = settings.SITE_TITLE
    return render(request, 'delivery/delivery.html', {'cur_del' : cur_del,'deliveries' : deliveries ,'categories' : categories, 'site_title' : site_title})