from django.urls import path
from . import views

urlpatterns = [
    path('main/',views.main, name='main'),
    path('add/',views.DeliveryCreateForm.as_view(),name='add'),
    path('delivery/<int:del_id>/',views.delivery, name = 'delivery')
]
