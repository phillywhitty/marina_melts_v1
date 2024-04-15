from django import forms
from .models import UserProfile, MyWallet
from django.core.exceptions import ValidationError
from django.forms.widgets import DateInput
from datetime import datetime
import re


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class ExpiryDateField(forms.DateField):
    def to_python(self, value):
        try:
            # Parse the input to a Python datetime object
            date_obj = datetime.strptime(f"01/{value}", '%d/%m/%y').date()
            return date_obj
        except ValueError:
            # If validation fails, raise a custom error
            raise ValidationError("Enter a valid expiry date in mm/yy format.")

class MyWalletForm(forms.ModelForm):
    expire_number = forms.CharField(max_length=5, label='Expiration Date (mm/yy)')
    class Meta:
        model = MyWallet
        fields = ['name', 'card_number', 'expire_number', 'cvv_number']

    def clean_cvv_number(self):
        cvv_number = self.cleaned_data.get('cvv_number')
        if cvv_number and (cvv_number < 100 or cvv_number > 999):
            raise ValidationError("CVV number must be a 3-digit number.")
        return cvv_number

    def clean_expire_number(self):
        expire_number = self.cleaned_data.get('expire_number')
        if not expire_number:
            raise ValidationError("Expiry date is required.")
        elif not re.match(r'\d{2}/\d{2}', expire_number):
            raise forms.ValidationError('Invalid expiration date format. Please use mm/yy format.')
        return expire_number
