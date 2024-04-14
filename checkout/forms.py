from django import forms
from .models import Order


# Define a form class for the Order model
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # Define placeholders for form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }
        # Set autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Customize form field attributes
        for field in self.fields:
            if field != 'country': # Skip 'country' field
                # Set placeholder with '*' for required fields
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                # Add a CSS class to form input fields
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove auto-generated labels
            self.fields[field].label = False