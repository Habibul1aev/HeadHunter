from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from account.manages import UserManager


class User(AbstractUser):
    ADMIN = 'admin'
    EMPLOYER = 'employer'
    CANDIDATE = 'candidate'

    ROLES = {
        (ADMIN, 'админ'),
        (EMPLOYER, 'работодатель'),
        (CANDIDATE, 'соискатель'),
    }

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-date_joined',)

    username = None
    avatar = ResizedImageField('аватарка', size=[500, 500], crop=['middle', 'center'],
                               upload_to='avatars/', force_format='WEBP', quality=90,
                               null=True, blank=True)
    phone = PhoneNumberField('номер', unique=True)
    email = models.EmailField('почта', blank=True, unique=True)
    role = models.CharField('роль', choices=ROLES, default=CANDIDATE, max_length=15)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return f'{self.get_full_name or str(self.phone)}'

