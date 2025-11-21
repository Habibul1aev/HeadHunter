from account.models import User
from django.db import models



class TimeStampAbstractModel(models.Model):
    created_at = models.DateTimeField('дата добавление', auto_now_add=True)
    updated_at = models.DateTimeField('дата изменения', auto_now=True)

    class Meta:
        abstract = True

class Country(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    countries = models.CharField('Страна', max_length=30)

    def __str__(self):
        return self.countries

class City(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Страна и Город'
        verbose_name_plural = 'Страны и Города'

    city = models.CharField('Город', max_length=30)
    countries = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна', related_name='city')

    def __str__(self):
        return f'{self.countries} {self.city}'

class Address(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'

    street = models.CharField('Адрес', max_length=100)
    country_city = models.ForeignKey('City' , on_delete=models.CASCADE, verbose_name='Страна и Город', related_name='address')

    def __str__(self):
        return self.street


class Category(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Категория', max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Work(TimeStampAbstractModel):
    EDUCATION = (
        ('Higher', 'Высшее'),
        ('Secondary vocational', 'Среднее профессиональное'),
        ('Without education', 'Без образования'),
    )

    TEST = (
        ('Doesn\'t matter', 'Не имеет значения'),
        ('From 1 to 2', 'От 1 года до 3 лет'),
        ('Without experience', 'Нет опыта'),
        ('From 3 to 6', 'От 3 до 6 лет'),
        ('More than 6', 'Более 6 лет'),
    )

    EMPLOYMENT = (
        ('Full-time employment', 'Полная занятость'),
        ('Partial employment', 'Частичная занятость'),
        ('Watch', 'Вахта'),
        ('Project work', 'Проектная работа'),
        ('Registration according to GPC', 'Оформление по ГПХ или по совместительству'),
        ('Probationary period', 'Стажировка'),
    )

    GRAPHICS = (
        ('5/2', '5/2'),
        ('6/1', '6/1'),
        ('Other', 'Другое'),
        ('2/2', '2/2'),
        ('Freely', 'Свободный'),
        ('Weekends', 'По выходным'),
        ('4/3', '4/3'),
        ('4/2', '4/2'),
        ('3/3', '3/3'),
        ('3/2', '3/2'),
        ('2/1', '2/1'),
        ('1/2', '1/2'),
        ('2/1', '2/1'),
        ('1/3', '1/3'),
    )

    TIME = (
        ('2 hour', '2 часов'),
        ('3 hour', '3 часов'),
        ('4 hour', '4 часов'),
        ('5 hour', '5 часов'),
        ('6 hour', '6 часов'),
        ('7 hour', '7 часов'),
        ('8 hour', '8 часов'),
        ('9 hour', '9 часов'),
        ('10 hour', '10 часов'),
        ('11 hour', '11 часов'),
        ('12 hour', '12 часов'),
        ('24 hour', '24 часа'),
        ('By agreement', 'По договору'),
        ('Other', 'Другое'),
    )

    FORMAT = (
        ('Hybrid', 'Гибрид'),
        ('Office', 'На месте работодателя'),
        ('Remotely', 'Удаленно'),
        ('Travel', 'Разъездной'),
    )

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    name = models.CharField('Работа', max_length=50,)
    description = models.TextField('Описание', max_length=600, help_text='Просто описание')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория', related_name='work')
    from_price = models.DecimalField('От', max_digits=10, decimal_places=2, default=0)
    to_price = models.DecimalField('До', max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    skill = models.ManyToManyField('Skills', verbose_name='Ключевые навыки')
    user = models.ForeignKey(User, models.CASCADE, verbose_name='Пользователь')
    country = models.ForeignKey('Country', models.CASCADE, verbose_name='Страна', related_name='work')
    city = models.ForeignKey('City', models.CASCADE, verbose_name='Город', related_name='work')
    address = models.ForeignKey('Address', models.CASCADE, verbose_name='Адрес', related_name='work')
    education = models.CharField('Образование', choices=EDUCATION, default='Without education', max_length=50)
    test = models.CharField('Опыт', max_length=50, choices=TEST, default='Doesn\'t matter')
    employment = models.CharField('Занятость', max_length=50, choices=EMPLOYMENT, default='Full-time employment')
    graphic = models.CharField('График работы', max_length=50, choices=GRAPHICS, default='Other')
    time = models.CharField('Рабочие часы', max_length=50, choices=TIME, default='By agreement')
    format = models.CharField('Формат работы', max_length=50, choices=FORMAT, default='Office')
    is_publish = models.BooleanField('Публичность',default=True)

    def __str__(self):
        return self.name

class Schedules(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'

    task = models.CharField('Работа', max_length=50)
    requirements = models.TextField('Требования', max_length=600)
    work = models.ForeignKey('Work', on_delete=models.CASCADE, verbose_name='График', related_name='schedules')

    def __str__(self):
        return self.task


class Requirements(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Требования'
        verbose_name_plural = 'Требовании'

    task = models.CharField('Задача', max_length=50)
    requirements = models.TextField('Требования', max_length=600)
    work = models.ForeignKey('Work', on_delete=models.CASCADE, verbose_name='Требования', related_name='requirements')


    def __str__(self):
        return self.task


class Skills(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Ключевой навык'
        verbose_name_plural = 'Ключевые навыки'

    name = models.CharField('Ключевые навыки', max_length=20, unique=True)

    def __str__(self):
        return self.name



class Resume(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Имя',max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    profession = models.CharField('Профессия',max_length=255)
    experience = models.TextField('Опыт',blank=True, null=True)
    skills = models.ManyToManyField('Skills', verbose_name='Навыки')
    education = models.TextField('Оброзование',blank=True, null=True)
    gmail = models.EmailField('Email')

    def __str__(self):
        return self.name