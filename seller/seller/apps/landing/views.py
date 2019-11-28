from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from landing import views
from .forms import ContactForm
from .mail_sender import send_simple_message
from django.conf import settings
from .models import New, FlatRodonit, InfoText, FlatAqvarel

# Create your views here.


def main_page(request):
    news = New.objects.all()
    flats_rodo = FlatRodonit.objects.order_by('price')
    flats_aqva = FlatAqvarel.objects.order_by('price')
    info_text = InfoText.objects.all()
    return render (request, 'main.html', {'news':news, 'flats_rodo':flats_rodo, 'flats_aqva':flats_aqva, 'info_text':info_text})

def form_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form, 'ajax received')
        if form.is_valid():
            e_mail = form.cleaned_data['email_contact']
            print(form.cleaned_data['email_contact'])
            tel = form.cleaned_data['tel_contact']
            print(form.cleaned_data['tel_contact'])
            question = form.cleaned_data['question']
            print(form.cleaned_data['question'])
            send_simple_message(e_mail, tel, question)
            success = 'success'
            return render (request, 'success.html', {'success':success})
        else:
            return render (request, 'fail.html', {})


def prices(request):
    return render (request, 'prices.html')
