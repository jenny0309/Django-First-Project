from django import forms
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

class FormName(forms.Form):
    name = forms.CharField() # validators=[check_for_z]
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:') # let users enter email once again
    text = forms.CharField(widget=forms.Textarea) # check types of widgets on documentation

    def clean(self):
        all_clean_data = super().clean() # return all clean data of the form at once
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

    # botcatcher = forms.CharField(required=False, # required=False <- don't show it on user page!
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)]) # equivalent to the code below

    # def clean_botcatcher(self): # botcatcher automatically recognises this method
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher