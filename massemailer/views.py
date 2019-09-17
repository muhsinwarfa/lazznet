from django.shortcuts import render, redirect
from django.core.mail import send_mail,send_mass_mail
from django.http import HttpResponse
from .forms import MailForm
from .models import Mail
from django.conf import settings

def index(request):
    a = "hello muthafcukaa"
    context= {
        'a': a
    }
    return render(request,'index.html',context)




def massemail(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            # get value of input by user
            receiver = request.POST['receiver']
            listofemails = receiver.split(",")
            finaltuple = ()
            for email in listofemails:
                finaltuple = finaltuple + (('This general subject', 'This is message',settings.EMAIL_HOST_USER,[email]),)
            send_mass_mail(finaltuple, fail_silently=False)
            form.save()
        return redirect('index')
    form = MailForm()
    return render(request,"emailform.html", {'form': form})

