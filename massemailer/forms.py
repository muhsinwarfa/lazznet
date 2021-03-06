from django import forms
from .models import Mail, Scrapper


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields =['receiver','replymail','pdf' ,'subject','body']
        exclude = ('receiver',)

class ScrapperForm(forms.ModelForm):
    class Meta:
        model = Scrapper
        fields =['csvdump']