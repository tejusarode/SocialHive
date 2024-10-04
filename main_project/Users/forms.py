from django import forms
from django.core.exceptions import ValidationError
from .models import*


class EditProfileForm(forms.ModelForm):
    class Meta:
        model =RegisterUser
        fields = ['username', 'first_name', 'last_name', 'email','phone', 'avatar', 'gender','custom_avatar']
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # Make fields optional
        self.fields['email'].required = False
        self.fields['phone'].required = False
        self.fields['avatar'].required = False
        self.fields['custom_avatar'].required = False
        self.fields['gender'].required = False
    




class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form',
            'placeholder': 'Enter your password',
            'id': 'password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form',
            'placeholder': 'Re-enter password',
            'id': 'password2'
        })
    )
    
    dob = forms.DateField(
        label='Date of Birth',
        widget=forms.DateInput(attrs={
            'class': 'form',
            'placeholder': 'YYYY-MM-DD',
            'id': 'Dob'
        }),
        input_formats=['%Y-%m-%d']  # Ensure this matches the format expected in input
    )
    
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        widget=forms.Select(attrs={
            'class': 'form',
            'id': 'gender'
        })
    )
    
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number',
            'id': 'phone'
        })
    )
    
    avatar = forms.ChoiceField(
        choices=[
            ('avatar1.png', 'Avatar 1'),
            ('avatar2.png', 'Avatar 2'),
            ('avatar3.png', 'Avatar 3'),
            ('avatar4.png', 'Avatar 4'),
            ('', 'Custom avatar')
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form',
            'id': 'avatar'
        })
    )
    
    custom_avatar = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'id': 'custom_avatar'
        })
    )
    
    class Meta:
        model = RegisterUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'avatar', 'custom_avatar', 'password', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'Enter your username',
                'id': 'username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'Enter your first name',
                'id': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'Enter your last name',
                'id': 'last_name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form',
                'placeholder': 'Enter your email',
                'id': 'email'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if RegisterUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        avatar = cleaned_data.get("avatar")
        custom_avatar = cleaned_data.get("custom_avatar")

        # Check if passwords match
        if password and password2 and password != password2:
            self.add_error('password2', 'Passwords do not match')

        # Ensure either a default avatar or a custom avatar is provided
        if not avatar and not custom_avatar:
            raise forms.ValidationError("You must select a default avatar or upload a custom avatar.")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Email or Phone',
        'id': 'username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'id': 'password'
    }))
   



class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form',
        'placeholder': 'Enter your email',
        'id': 'email'
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form',
            'placeholder': 'Enter your new password',
            'id': 'password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form',
            'placeholder': 'Re-enter password',
            'id': 'password2'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            self.add_error('password2', 'Passwords do not match.')

        return cleaned_data




class FollowForm(forms.Form):
    user_to_follow = forms.ModelChoiceField(queryset=RegisterUser.objects.all())

