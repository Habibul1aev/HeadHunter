import random

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.defaultfilters import first
from django.urls import reverse
from django.views.decorators.cache import never_cache

from account.models import User
from headhunter.filter import SearchWork
from headhunter.forms import HelpForm
from headhunter.models import Work, Country, Category, Resume, City
from django.contrib import messages

from django.db.models import Min, Max, Count

from project import settings
from workspace.forms import CreateResumeForm


def currentUser(request):
    if request.user.is_authenticated:
        return request.user.first_name[0] if request.user.first_name else None
    return None
@never_cache
def main(request):
    if request.user.is_authenticated:
        return redirect('cards')

    works = Work.objects.filter(is_publish=True).order_by('-created_at')

    user1 = currentUser(request)

    countries = Country.objects.all()
    search_query = request.GET.get('search_city')

    country = ''

    if search_query:
        country = countries.filter(countries=search_query).first()
        if country:
            works = works.filter(country=country)


    filters = SearchWork(request.GET, queryset=works)
    filterwork = filters.qs

    vacancies = works.count()
    company = Category.objects.filter(name='Компания').count()
    resume = Resume.objects.all().count()

    search = request.GET.get('search')
    if search:
        if request.user.is_authenticated:
            return redirect('/cards/')
        else:
            pass

    #Вход с email без пароля но с кодом потверждения
    if request.method == 'POST':
        action = request.POST.get('action')
        email = request.POST.get('email')
        if action == 'send_code':
            if User.objects.filter(email = email).exists():
                code = str(random.randint(100000, 999999))
                request.session['email'] = email
                request.session['code'] = code
                send_mail(
                    'Код подтверждения',
                    f'Ваш код: {code}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                )

                return render(request, 'main/body.html', {'context': True, 'show_error_modal': False})

            else:
                return render(request, 'main/body.html', {'context': True, 'show_error_modal': True})

        elif action == 'verify_code':
            input_code = request.POST.get('code')
            session_code = request.session.get('code')
            session_email = request.session.get('email')

            if input_code == session_code:

                user2 = User.objects.get(email = session_email)

                login(request, user2)
                del request.session['code']
                del request.session['email']
                return redirect('/cards/')

            else:
                return render(request, 'main/body.html', {
                    'context': True,
                    'email': session_email,
                    'show_error_modal': True
                })



    category_stats = []
    categories = Category.objects.all()

    for category in categories:
        work_in_category = Work.objects.filter(category=category, is_publish=True)

        cat_count = work_in_category.count()

        min_price = work_in_category.aggregate(Min('from_price'))['from_price__min']
        max_price = work_in_category.aggregate(Max('to_price'))['to_price__max']

        category_stats.append({
            'category': category,
            'cat_count': cat_count,
            'min_price': min_price if min_price else 0,
            'max_price': max_price if max_price else 0,
        })

    work_prices = list(works.values_list('from_price', 'to_price'))
    if work_prices:
        min_price_all = min(work_prices, key=lambda x: x[0] if x[0] is not None else float('inf'))[0]
        max_price_all = max(work_prices, key=lambda x: x[1] if x[1] is not None else float('-inf'))[1]
    else:
        min_price_all = None
        max_price_all = None

    return render(request, 'main/body.html', {
        'countries': countries,
        'country': country,
        'min': min_price_all,
        'max': max_price_all,
        'categories': categories,
        'works': works,
        'filterwork': filterwork,
        'vacancies': vacancies,
        'company': company,
        'resume': resume,
        'category_stats': category_stats,
        'user1': user1,
        'content': False,
    })

@never_cache
@login_required(login_url='admin-main')
def cards(request):
    user1 = currentUser(request)
    work = Work.objects.all()

    search = request.GET.get('search')
    if search:
        work = work.filter(name__contains=search)


    return render(request, 'cards/body.html', {'user1': user1, 'work':work})


def employer(request):
    search = request.GET.get('search')
    if search:
        return redirect('/cards/')

    return render(request, 'employers/body.html')

@never_cache
def help(request):
    user = User.objects.all()
    user1 = currentUser(request)
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            send_mail(
                subject=f"Помощь: {recipient} от {name}",
                message=f"{topic} ({email})\n\n{message}",
                from_email=email,
                recipient_list=['hhabibullaevfirdavs@gmail.com'],
            )

            return render(request, 'help/successfully.html')
    else:
        form = HelpForm()

    return render(request, 'help/help.html', {'form':form, 'user':user, 'user1': user1,})


@login_required(login_url='admin-main')
def myResume(request):
    user = request.user
    user1 = currentUser(request)

    if request.method == 'POST':
        form = CreateResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)

            if request.user.is_authenticated:
                resume.user = request.user

            resume.save()
            messages.success(request, 'Резюме успешно создано!')
            # return redirect('resume_success')  # Перенаправляем на страницу успеха
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = CreateResumeForm()

    return render(request, 'myresume/body.html', {'user1': user1, 'user':user, 'form': form})


def agreement(request):


    return render(request, 'agreement/base.html')