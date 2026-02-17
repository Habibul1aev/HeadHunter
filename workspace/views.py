from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from account.models import User
from headhunter.models import Work, Category, Resume
from workspace.forms import CreateWorkForm, AuthorizationForm, RegistrationForm, CreateResumeForm
from django.contrib import messages
from django.core.mail import send_mail

class Main(View):
    template_name = 'workspace/body.html'
    def get(self, request):
        user1 = ''
        for name in User.objects.all():
            user1 = name.first_name[0:1]

        return render(request, self.template_name, {'user1': user1})


class Create(View):
    template_name = 'workspace/body.html'

    def get(self, request):
        work = Work.objects.all()
        category = Category.objects.all()
        form = CreateWorkForm()

        return render(request, self.template_name, {
            'work': work,
            'category': category,
            'form': form,
        })

    def post(self, request):
        work = Work.objects.all()
        category = Category.objects.all()
        form = CreateWorkForm(request.POST)

        if form.is_valid():
            work_instance = form.save(commit=False)
            work_instance.user = request.user
            work_instance.save()
            messages.success(request, f'Вы создали вакансию {work_instance.name}')
            return redirect('/workspace/')

        return render(request, self.template_name, {
            'work': work,
            'category': category,
            'form': form,
        })


class CreateResume(View):
    template_name = 'workspace/resume/body.html'

    def get(self, request):
            
        form = CreateResumeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  # если в модели есть user
            resume.save()
            return redirect('main')  # куда отправить после успешного создания

        return render(request, self.template_name, {'form': form})


class Authorization(View):
    template_name = 'workspace/auth/authorization/body.html'

    def get(self, request):
        form = AuthorizationForm()

        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = AuthorizationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, f'Добро пожаловать {email}')
                return redirect('/cards/')

            messages.error(request, 'Аккаунт не найден (')

        return render(request, self.template_name, {'form':form})


class Registration(View):
    template_name = 'workspace/auth/registration/body.html'
    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user1 = form.save()
            login(request, user1)

            messages.success(request, f'Вы успешно создали аккаунт')
            return redirect('/cards/')

        return render(request, self.template_name, {'form': form})