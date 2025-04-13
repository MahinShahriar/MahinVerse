from django import forms
from django_recaptcha.fields import ReCaptchaField


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(required=True)


class ContactForm(forms.Form):
    email = forms.EmailField()
    number = forms.NumberInput()
    subject = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            # 'class': 'w-full px-4 py-3 border-2 rounded-lg focus:ring-2 focus:ring-blue-300 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
            'required': True,
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 6,
            # 'class': 'w-full px-4 py-3 border-2 rounded-lg focus:ring-2 focus:ring-blue-300 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
            'required': True,
        })
    )

    def clean_message(self):
        message = self.cleaned_data.get("message")
        # Spam Protection: Block repeated messages
        if "http" in message or "www" in message:  # Prevent links (basic spam filtering)
            raise forms.ValidationError("Links are not allowed in messages.")
        return message

class Subscriber(forms.Form):
    # created this class to identify the user email is exist or not. It will be developed .
    email = forms.EmailField()