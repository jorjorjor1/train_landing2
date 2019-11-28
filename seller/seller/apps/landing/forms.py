from django import forms

class ContactForm(forms.Form):
    email_contact = forms.EmailField(label='Your e-mail', max_length=30)
    tel_contact = forms.CharField(label = 'Your phone')
    question = forms.CharField (label='Question', max_length=200, empty_value = '', required=False)