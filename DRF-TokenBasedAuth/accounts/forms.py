from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    # Overriding first_name field
    first_name = forms.CharField(max_length=50, required=True, label='First Name')
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Defining our own label for password2 field
        self.fields['password2'].label = 'Confirm Password'

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = '__all__'