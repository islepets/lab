from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Call, Client, Reason, Operator, Status

class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ReasonForm(forms.ModelForm):
    class Meta:
        model = Reason
        fields = '__all__'

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = '__all__'

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]