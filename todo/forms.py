from django import forms
from todo.models import User

class UserRegiterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['fullname', 'email', 'picture']

    def validate(self):
        password = self.changed_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password and confirm password must be same!')
        elif len(password) < 8:
            raise forms.ValidationError('Password must contain at least 8 charecters!')
        return password