from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Digite sua senha"})
    )
    confirm_password = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirme sua senha"})
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Digite seu email"})
    )
    

    class Meta:
        model = User
        fields = ["name", "email"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("As senhas não correspondem.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Nome de Usuário",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite seu nome de usuário"})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Digite sua senha"})
    )
