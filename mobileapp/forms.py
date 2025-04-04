from django.forms import ModelForm
from .models import Mobile


class ProductCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'

    def clean(self):
        cleaned_data=super().clean()
        mobile_name=cleaned_data.get('mobile_name')
        if mobile_name==mobile_name:
            msg="Mobile name should be unique."
            self.add_error('mobile_name',msg)

        price=cleaned_data.get('price')
        if price<500:
            msg="Invalid Amount."
            self.add_error("price",msg)
        

