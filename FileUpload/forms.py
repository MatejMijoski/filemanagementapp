from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Uploaded, Comment


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Repeat Password"


class LogInForm:
    class Meta:
        model = User
        fields = ('username', 'password1')


class FileUploadForm(forms.ModelForm):
    file = forms.FileField(allow_empty_file=True)

    class Meta:
        model = Uploaded
        fields = (
            'name',
            'file',
            'link',
            'description',
            'usertags',
        )


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
        )

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    widgets = {
        'email': forms.TextInput(attrs={'class': 'form-control'}),
    }


class ChangeTagsForm(forms.ModelForm):
    class Meta:
        model = Uploaded
        fields = ['usertags']
