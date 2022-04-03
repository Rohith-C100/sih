from random import choices
from sre_parse import State
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
    one =forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=CHOICES,label=questions.one)
    two = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=CHOICES,label=questions.two)
    three = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=CHOICES,label=questions.three)
    four = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=CHOICES,label=questions.four)

class Cfeedback(forms.Form):

    questions=CollegeFeedback.objects.get(id=1)
    CHOICES = [('1', 'very poor'), ('2', 'poor'),('3', 'good'),('4', 'very good'),('5', 'excellent')]
    one =forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}),choices=CHOICES,label=questions.one)
    two = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=CHOICES,label=questions.two)
    three = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=CHOICES,label=questions.three)
    four = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=CHOICES,label=questions.four)

# widget=forms.RadioSelect(attrs={'class':'btn'})

class sign_up_form(forms.Form):
    first_name=forms.CharField(strip=True,min_length=2,required=True)
    last_name=forms.CharField(strip=True,min_length=2,required=True)
    email_id=forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    re_enter_password=forms.CharField(widget=forms.PasswordInput)
    role_choice = (("student", "student"), ("parent", "parent"))
    role=forms.ChoiceField(choices=role_choice)
    # role = forms.ChoiceField(, choices=[CHOICES], required=False)
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get("password")
        re_entered_password=cleaned_data.get("re_enter_password")

        if(password!=re_entered_password):
            raise ValidationError(
                "Enter the correct password for both the fields."
            )
        # else:
        #     return cleaned_data


class filter_form(forms.Form):
    STATE_CHOICES = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    DISTRICT_CHOICES = (("Tumkur", "Tumkur"), ("Banglore", "Banglore"))
    state=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-select'}),choices = STATE_CHOICES)
    district=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-select'}),choices = DISTRICT_CHOICES)
  
# creating a form 
# class GeeksForm(forms.Form):
#     geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)
    # def clean(self):
    #     cleaned_data=super().clean()
    #     password=cleaned_data.get("password")
    #     re_entered_password=cleaned_data.get("re_enter_password")

    #     if(password!=re_entered_password):
    #         raise ValidationError(
    #             "Enter the correct password for both the fields."
    #         )
        # else:
        #     return cleaned_data

