from django.shortcuts import render, redirect
from django.core.mail import send_mail,send_mass_mail, EmailMessage
from django.core import mail

from django.http import HttpResponse
from .forms import MailForm
from .models import Mail


from django.conf import settings
#
def index(request):
    a = "hello muthafcukaa"
    context = {
        'a': a
    }
    return render(request,'index.html',context)


def massemail(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            # get value of input by user
            receiver = request.POST['receiver']
            subject = request.POST['subject']
            body = request.POST['body']
            listofemails = receiver.split(",")
            listofmessages = []
            connection = mail.get_connection()

            # Manually open the connection
            connection.open()
            for email in listofemails:
                msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [email])
                msg.content_subtype = "html"
                msg.attach_file('attachments/myresume.pdf')
                listofmessages.append(msg)

            connection.send_messages(listofmessages)
            connection.close()

            form.save()
        return redirect('index')
    form = MailForm()
    return render(request,"emailform.html", {'form': form})

