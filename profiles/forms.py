from django import forms
from .models import UserProfile, MyWallet


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


class MyWalletForm(forms.ModelForm):
    class Meta:
        model = MyWallet
        fields = ['name', 'card_number', 'expire_number', 'cvv_number']
    def clean_default_cvv_number(self):
        # Add any custom validation logic for the CVV number if needed
        cvv_number = self.cleaned_data.get('default_cvv_number')
        if cvv_number and (cvv_number < 100 or cvv_number > 999):
            raise forms.ValidationError("CVV number must be a 3-digit number.")
        return cvv_number

