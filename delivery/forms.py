from django.forms import ModelForm
from .models import DeliveryModel
class DeliveryForm(ModelForm):
    class Meta:
        model = DeliveryModel
        fields = ('title','description','price','category')