from django import forms
from index.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields = ('username','password')

        widgets = {
            'username':forms.TextInput(),
            'password':forms.PasswordInput(),
        }
