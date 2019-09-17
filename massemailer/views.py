from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    a = "hello muthafcukaa"

    send_mail(
        'Subject here',
        'Here is the message.',
        'muhsin.warfa@gmail.com',
        ['mwarfa@qatar.cmu.edu'],
        fail_silently=False,
    )
    context= {
        'a': a
    }
    return render(request,'index.html',context)

def massemail(request):

    datatuple = (
        ('Subject', 'Message.', 'from@example.com', ['john@example.com']),
        ('Subject', 'Message.', 'from@example.com', ['jane@example.com']),
    )
    send_mass_mail(datatuple)
