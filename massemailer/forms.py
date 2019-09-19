from django import forms
from .models import Mail, Scrapper


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields =['receiver','subject','body']

class ScrapperForm(forms.ModelForm):
    class Meta:
        model = Scrapper
        fields =['csvdump']