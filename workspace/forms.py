from django import forms

from account.models import User
from headhunter.models import Work, Resume


class CreateWorkForm(forms.ModelForm):

    class Meta:
        model = Work
        exclude = ['user', 'created_at', 'updated_at']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Работа',
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Описание',
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'from_price': forms.NumberInput(attrs={
                'placeholder': 'Зарплата от',
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'to_price': forms.NumberInput(attrs={
                'placeholder': 'Зарплата до',
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'skill': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'country': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'city': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'address': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'education': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'test': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'employment': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'graphic': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'time': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'format': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
            'is_publish': forms.CheckboxInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3'
            }),
        }

class CreateResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ['name', 'surname', 'profession', 'experience', 'skills', 'education', 'gmail']

        widgets = {
            'name': forms.TextInput(attrs={ 'placeholder': 'Введите ваше имя', 'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию', 'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'profession': forms.TextInput(attrs={'placeholder': 'Например: Frontend разработчик','class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'gmail': forms.EmailInput(attrs={'placeholder': 'example@gmail.com','class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'experience': forms.Textarea(attrs={'placeholder': 'Опишите ваш опыт работы, предыдущие должности и достижения...','rows': 4, 'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'skills': forms.Select(attrs={'placeholder': 'JavaScript, Python, Django, React, HTML/CSS...','rows': 3, 'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'education': forms.Textarea(attrs={'placeholder': 'Укажите ваше образование, курсы, сертификаты...','rows': 3,'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})
        }

    def clean_gmail(self):
        email = self.cleaned_data['gmail']
        if Resume.objects.filter(gmail=email).exists():
            raise forms.ValidationError("Резюме с таким email уже существует")
        return email



class AuthorizationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Введите email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Введите пароль'}))


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'phone', 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Введите номер','class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите электронную почту','class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }
