from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


# Form for creating and updating Product objects
class ProductForm(forms.ModelForm):
    # Meta class to specify the model and fields
    class Meta:
        model = Product
        fields = '__all__'
    # Custom image field with a clearable file input widget
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        # Query all categories and create choices with friendly names
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        # Set choices for the 'category' field
        self.fields['category'].choices = friendly_names
        # Add CSS classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


 