from django import forms
from django.core.validators import FileExtensionValidator
from .models import Answer


class ResultForm(forms.ModelForm):
    model = Answer
    result = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['txt'])])
