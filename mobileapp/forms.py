from django.forms import ModelForm
from .models import Mobile


class ProductCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'

    def clean(self):
        print('inside clean')

