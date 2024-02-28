from django import forms 

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget= forms.TextInput(
          attrs= { 'class' : 'form-control'}
        )
    )
    senha= forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        )
    )

class CadastroForms(forms.Form):
    
    nome_cadastro  = forms.CharField(
        label="Nome do Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex.: Joao da Silva"
            }
        ),


    )
    email= forms.EmailField(
        label="Email do Cadastro: ",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
           attrs={ "class" : "form-control", "placeholder" : "na@na.com.br"}
        )
    )

    senha = forms.CharField(
        label= "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Digite a senha'
        }),

    )

    confirmacao_senha = forms.CharField(
        label="Confirmação da senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Digite a sua senha de novamente' }
        ),
    )



