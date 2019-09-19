from django.shortcuts import render, redirect
from django.core.mail import send_mail,send_mass_mail, EmailMessage
from urllib.request import Request, urlopen

from django.core import mail
from django.http import HttpResponse
from .forms import MailForm,ScrapperForm
from .models import Mail,Scrapper
from django.conf import settings
import re
import requests
from bs4 import BeautifulSoup as soup


def index(request):
    a = "hello muthafcukaa"
    if request.method == 'POST':
        form = ScrapperForm(request.POST)
        if form.is_valid():
            url =  request.POST['csvdump']
            form.save()
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            page_soup = soup(webpage, "html.parser")
            email = page_soup(text=re.compile(r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*'))
            _emailtokens = str(email).replace("\\t", "").replace("\\n", "").split(' ')
            if len(_emailtokens):
                email = ([match.group(0) for token in _emailtokens for match in
                       [re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", str(token.strip()))] if match])
                print(email)
            return render(request,'listofemails.html',{'email' : email})

    form = ScrapperForm()
    context = {
        'a': a,
        'form': form
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


