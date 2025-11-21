from random import choices
from django import forms


class HelpForm(forms.Form):
    SUPPORT = {
        ('support@gmail.com', 'Техническая поддержка'),
        ('advertising@gmail.com', 'Отдел маркетинга и рекламы'),
        ('sales@gmail.com', 'Отдел продаж'),
        ('employer@gmail.com', 'Отдел по работе с соискателями'),
        ('qualities@gmail.com', 'Отдел контроля качества'),
    }

    recipient = forms.ChoiceField(
        choices=SUPPORT,
        label="Кому адресовано сообщение",
        widget=forms.RadioSelect(attrs={
            'class': 'mt-[20px] mb-[10px]'
        })
    )

    topic = forms.CharField(
        max_length=100,
        label="Тема",
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-[600px] p-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Введите тему сообщения'
        })
    )

    message = forms.CharField(
        label="Содержание",
        widget=forms.Textarea(attrs={
            'class': 'mt-1 block w-[600px] p-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500',
            'rows': 4,
            'placeholder': 'Введите ваше сообщение...'
        })
    )

    name = forms.CharField(
        max_length=100,
        label="Имя",
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-[600px] p-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Ваше имя'
        })
    )

    email = forms.EmailField(
        label="Ваш Email",
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-[600px] p-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'example@mail.com'
        })
    )

