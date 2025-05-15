from django.forms import ModelForm
from .models import Mobile,Cart
from django import forms


class ProductCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "brand":forms.Select(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "specs":forms.Textarea(attrs={"class":"form-control"}),
        }

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get('price')
        if price<500:
            msg="Invalid Amount."
            self.add_error("price",msg)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
        

    # email_id = forms.EmailField(required=False)
    # address = forms.CharField(required=False)
    # customer_name = forms.CharField(required=False)
    # mob_no = forms.IntegerField(required=False)
        

