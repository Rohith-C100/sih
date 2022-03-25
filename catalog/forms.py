from django import forms
from django.core.exceptions import ValidationError

from catalog.models import LecturerFeedback,CollegeFeedback


# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']

#         # Check if a date is not in the past.
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))

#         # Check if a date is in the allowed range (+4 weeks from today).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

#         # Remember to always return the cleaned data.
#         return data

class Lfeedback(forms.Form):
    questions=LecturerFeedback.objects.get(id=1)
    CHOICES = [('1', 'very poor'), ('2', 'poor'),('3', 'good'),('4', 'very good'),('5', 'excellent')]
    one =forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=questions.one)
    two = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=questions.two)
    three = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=questions.three)
    four = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=questions.four)

class Cfeedback(forms.Form):
    questions=CollegeFeedback.objects.get(id=1)
    CHOICES = [('1', 'very poor'), ('2', 'poor'),('3', 'good'),('4', 'very good'),('5', 'excellent')]
    one =forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=questions.one)
    two = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=questions.two)
    three = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=questions.three)
    four = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=questions.four)