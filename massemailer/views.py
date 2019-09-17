from django.shortcuts import render, redirect
from django.core.mail import send_mail,send_mass_mail
from django.http import HttpResponse
from .forms import MailForm
from .models import Mail
from django.conf import settings

def index(request):
    a = "hello muthafcukaa"

    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'muhsin.warfa@gmail.com',
    #     ['mwarfa@qatar.cmu.edu'],
    #     fail_silently=False,
    # )
    context= {
        'a': a
    }
    return render(request,'index.html',context)

def massemail(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            # get value of input by user
            # receiver = request.POST['receiver']
            # messege 1 has two CC's
            message1 = (
            'broooo', 'This is message 1', settings.EMAIL_HOST_USER, ['debanif@mail-file.net', 'rixon.kendyl@golld.us'])
            # message 2 sends directly
            message2 = ('hii ni ya pili', 'Here is another message 2', settings.EMAIL_HOST_USER, ['kerdocilmo@enayu.com'])
            send_mass_mail((message1, message2), fail_silently=False)
            form.save()
        return redirect('index')
    form = MailForm()
    return render(request,"emailform.html", {'form': form})




