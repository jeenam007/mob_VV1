from django.forms import ModelForm
from .models import Mobile
from django import forms


class ProductCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "specs":forms.Textarea(attrs={"class":"form-control"}),
        }

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get('price')
        if price<500:
            msg="Invalid Amount."
            self.add_error("price",msg)
        

