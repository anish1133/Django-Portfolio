from django import forms
from django.core.mail import send_mail
from .models import UserDetails


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    Subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(max_length=300, required=True)

    def save(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        Subject = self.cleaned_data.get("Subject")
        message = self.cleaned_data.get("message")
        recipient_email = UserDetails.objects.first().email
        print(recipient_email)

        send_mail(
            subject=f"Contact Form - {Subject}",
            message=f"Name: {name}\nEmail: {email}\n\n{message}",
            from_email=email,
            recipient_list=[recipient_email],
            fail_silently=False,
        )
