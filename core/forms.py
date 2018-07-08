from django import forms
from django.core.validators import RegexValidator

character_validator = RegexValidator(regex='^[a-zA-Z-\s]*$',
                                     message='Please provide characters only.',
                                     code='invalid_username')

class SliderForm(forms.Form):
    name = forms.CharField(max_length=20, required=True,
                           validators=[character_validator])
