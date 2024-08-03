from django import forms
from .models import Supplier
from django.core.exceptions import ValidationError

class SupplierForm(forms.ModelForm):
    representative_phone = forms.CharField(initial='+7', max_length=12)

    class Meta:
        model = Supplier
        fields = ['company_name', 'representative_name', 'representative_phone', 'address']

    def clean_representative_phone(self):
        phone = self.cleaned_data['representative_phone']
        if not phone.startswith('+7') or not phone[1:].isdigit() or len(phone) != 12:
            raise ValidationError('Телефон должен начинаться с +7 и содержать 11 цифр после знака +.')
        return phone