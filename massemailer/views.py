from django.shortcuts import render, redirect
from django.core.mail import send_mail,send_mass_mail, EmailMessage
from urllib.request import Request, urlopen, HTTPError,HTTPSHandler
import urllib
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.core import mail
from .forms import MailForm,ScrapperForm
from .models import Mail,Scrapper
from django.conf import settings
import re
import requests
from bs4 import BeautifulSoup as soup


def index(request):
    if request.method == 'POST':
        post = request.POST.copy()
        url = request.POST['csvdump']
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            urllib.request.urlopen(req)
        except urllib.error.URLError as e:
              return render(request,"404.html")
        webpage = urlopen(req).read()
        page_soup = soup(webpage, "html.parser")

        email = page_soup(text=re.compile(r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*'))
        _emailtokens = str(email).replace("\\t", "").replace("\\n", "").split(' ')
        if len(_emailtokens):
            emails = ([match.group(0) for token in _emailtokens for match in
                       [re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", str(token.strip()))] if match])
        post.update({'csvdump' : " ".join(str(x) for x in emails)})
        request.POST = post
        form = ScrapperForm(request.POST)
        if(len(email) == 0):
            emails = None
            objectid = None
            return render(request, 'listofemails.html', {'emails': emails, 'objectid': objectid})

        if form.is_valid():
            x = form.save()
            objectid = x.id
            return render(request,'listofemails.html',{'emails' : emails , 'objectid' : objectid})

    form = ScrapperForm()
    context = {
        'form': form
    }

    return render(request,'index.html',context)





def massemail(request , id):
    normalid = id
    mailobj = Scrapper.objects.get(id = normalid)
    if request.method == 'POST':
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            # get value of input by user
            form.receiver = mailobj.csvdump
            subject = request.POST['subject']
            body = request.POST['body']
            replymail = request.POST['replymail']


            try:
                pdf = request.FILES['pdf']
                fs = FileSystemStorage()
                name = fs.save(pdf.name, pdf)
            except MultiValueDictKeyError:
                pdf = None

            listofemails = form.receiver.split(",")
            listofmessages = []
            connection = mail.get_connection()
            # Manually open the connection
            connection.open()
            headers = {'Reply-To': replymail}
            for email in listofemails:
                msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [email], headers=headers)
                msg.content_subtype = "html"
                if pdf is not None:
                    msg.attach_file(pdf.name)
                listofmessages.append(msg)
            connection.send_messages(listofmessages)
            connection.close()
            form.save()
        return redirect('index')
    form = MailForm()
    return render(request,"emailform.html", {'form': form, 'normalid' : normalid})

