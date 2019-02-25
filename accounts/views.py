from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from products.models import Product, ProductTimeAssigned
from accounts.forms import UserLoginForm, UserRegistrationForm
import math
import json

@login_required
def logout(request):
    """Log the user outself."""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return render(request, 'index.html')


def login_by_email(request):
    """Return a login page."""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password'])

            if user:
                login(request, user, backend='accounts.backends.EmailAuth')
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('profile'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page."""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                login(request, user)
                messages.success(request, "You have successfully registered")
                return render(request, 'index.html')
            else:
                messages.error(
                    request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """The user's profile page showing All Features/Issues, only created by
    the Profile User & all by time for Admin User."""

    background_colour_list = [
                    'rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)']

    border_colour_list = [
        'rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)']

    user = User.objects.get(email=request.user.email)

    # my votes

    my_votes = Product.objects.values('name').filter(user_id=user.id).annotate(Count('productvote__user_id')).filter(productvote__user_id__count__gt=0)

    all_product_names_my_votes = []
    all_product_my_votes = []

    for i, q in enumerate(my_votes):
        all_product_names_my_votes.append(str(q['name']))
        all_product_my_votes.append(str(q['productvote__user_id__count']))

    if len(all_product_names_my_votes) == 0:
        all_product_names_my_votes = ['No Data']
        all_product_my_votes = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_my_votes) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_my_votes) / len(border_colour_list)))

    json_all_product_names_my_votes = json.dumps(all_product_names_my_votes)
    json_all_product_my_votes = json.dumps(all_product_my_votes)
    json_bg_colours_my_votes = json.dumps(bg_colours[:len(all_product_names_my_votes)])
    json_b_colours_my_votes = json.dumps(b_colours[:len(all_product_names_my_votes)])

    # all votes

    all_votes = Product.objects.values('name').annotate(Count('productvote__user_id')).filter(productvote__user_id__count__gt=0)

    all_product_names_all_votes = []
    all_product_all_votes = []

    for i, q in enumerate(all_votes):
        all_product_names_all_votes.append(str(q['name']))
        all_product_all_votes.append(str(q['productvote__user_id__count']))

    if len(all_product_names_all_votes) == 0:
        all_product_names_all_votes = ['No Data']
        all_product_all_votes = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_all_votes) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_all_votes) / len(border_colour_list)))

    json_all_product_names_all_votes = json.dumps(all_product_names_all_votes)
    json_all_product_all_votes = json.dumps(all_product_all_votes)
    json_bg_colours_all_votes = json.dumps(bg_colours[:len(all_product_names_all_votes)])
    json_b_colours_all_votes = json.dumps(b_colours[:len(all_product_names_all_votes)])

    # donations

    all_donations = Product.objects.values('name','total_amount_paid').filter(total_amount_paid__gt=1)

    all_product_names_donations = []
    all_product_donations = []

    for i, q in enumerate(all_donations):
        all_product_names_donations.append(str(q['name']))
        all_product_donations.append(str(q['total_amount_paid']))

    if len(all_product_names_donations) == 0:
        all_product_names_donations = ['No Data']
        all_product_donations = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_donations) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_donations) / len(border_colour_list)))

    json_all_product_names_donations = json.dumps(all_product_names_donations)
    json_all_product_donations = json.dumps(all_product_donations)
    json_bg_colours_donations = json.dumps(bg_colours[:len(all_product_names_donations)])
    json_b_colours_donations = json.dumps(b_colours[:len(all_product_names_donations)])

    # admin time spent
    time_spent = Product.objects.values('name').filter(producttimeassigned__time_minutes__gt=1).annotate(Sum('producttimeassigned__time_minutes'))

    all_product_names_time = []
    all_product_time = []

    for i, q in enumerate(time_spent):
        all_product_names_time.append(str(q['name']))
        all_product_time.append(str(q['producttimeassigned__time_minutes__sum']))

    if len(all_product_names_time) == 0:
        all_product_names_time = ['No Data']
        all_product_time = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_time) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_time) / len(border_colour_list)))

    json_all_product_names_time = json.dumps(all_product_names_time)
    json_all_product_time = json.dumps(all_product_time)
    json_bg_colours_time = json.dumps(bg_colours[:len(all_product_names_time)])
    json_b_colours_time = json.dumps(b_colours[:len(all_product_names_time)])

    # admin time spent daily
    time_spent_daily = Product.objects.values('name').filter(producttimeassigned__submitted__date=datetime.now(), producttimeassigned__time_minutes__gt=1).annotate(Sum('producttimeassigned__time_minutes'))

    all_product_names_time_daily = []
    all_product_time_daily = []
    for i, q in enumerate(time_spent_daily):
        all_product_names_time_daily.append(str(q['name']))
        all_product_time_daily.append(str(q['producttimeassigned__time_minutes__sum']))

    if len(all_product_names_time_daily) == 0:
        all_product_names_time_daily = ['No Data']
        all_product_time_daily = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_time_daily) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_time_daily) / len(border_colour_list)))

    json_all_product_names_time_daily = json.dumps(all_product_names_time_daily)
    json_all_product_time_daily = json.dumps(all_product_time_daily)
    json_bg_colours_time_daily = json.dumps(bg_colours[:len(all_product_names_time_daily)])
    json_b_colours_time_daily = json.dumps(b_colours[:len(all_product_names_time_daily)])

    # admin time spent 7days
    time_spent_7days = Product.objects.values('name').filter(producttimeassigned__submitted__date__gte=datetime.today() - timedelta(days=7) , producttimeassigned__time_minutes__gt=1).annotate(Sum('producttimeassigned__time_minutes'))
    all_product_names_time_7days = []
    all_product_time_7days = []
    for i, q in enumerate(time_spent_7days):
        all_product_names_time_7days.append(str(q['name']))
        all_product_time_7days.append(str(q['producttimeassigned__time_minutes__sum']))

    if len(all_product_names_time_7days) == 0:
        all_product_names_time_7days = ['No Data']
        all_product_time_7days = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_time_7days) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_time_7days) / len(border_colour_list)))

    json_all_product_names_time_7days = json.dumps(all_product_names_time_7days)
    json_all_product_time_7days = json.dumps(all_product_time_7days)
    json_bg_colours_time_7days = json.dumps(bg_colours[:len(all_product_names_time_7days)])
    json_b_colours_time_7days = json.dumps(b_colours[:len(all_product_names_time_7days)])

    # admin time spent monthly
    time_spent_monthly = Product.objects.values('name').filter(producttimeassigned__submitted__month=datetime.now().month, producttimeassigned__submitted__year=datetime.now().year, producttimeassigned__time_minutes__gt=1).annotate(Sum('producttimeassigned__time_minutes'))

    all_product_names_time_monthly = []
    all_product_time_monthly = []
    for i, q in enumerate(time_spent_monthly):
        all_product_names_time_monthly.append(str(q['name']))
        all_product_time_monthly.append(str(q['producttimeassigned__time_minutes__sum']))

    if len(all_product_names_time_daily) == 0:
        all_product_names_time_monthly = ['No Data']
        all_product_time_monthly = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_time_monthly) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_time_monthly) / len(border_colour_list)))

    json_all_product_names_time_monthly = json.dumps(all_product_names_time_monthly)
    json_all_product_time_monthly = json.dumps(all_product_time_monthly)
    json_bg_colours_time_monthly = json.dumps(bg_colours[:len(all_product_names_time_monthly)])
    json_b_colours_time_monthly = json.dumps(b_colours[:len(all_product_names_time_monthly)])

    args = {
            'profile': user,

            'all_product_names_my_votes': json_all_product_names_my_votes,
            'all_product_my_votes': json_all_product_my_votes,
            'background_colours_my_votes': json_bg_colours_my_votes,
            'border_colours_my_votes': json_b_colours_my_votes,

            'all_product_names_all_votes': json_all_product_names_all_votes,
            'all_product_all_votes': json_all_product_all_votes,
            'background_colours_all_votes': json_bg_colours_all_votes,
            'border_colours_all_votes': json_b_colours_all_votes,

            'all_product_names_donations': json_all_product_names_donations,
            'all_product_donations': json_all_product_donations,
            'background_colours_donations': json_bg_colours_donations,
            'border_colours_donations': json_b_colours_donations,

            'all_product_names_time': json_all_product_names_time,
            'all_product_time': json_all_product_time,
            'background_colours_time': json_bg_colours_time,
            'border_colours_time': json_b_colours_time,

            'all_product_names_time_daily': json_all_product_names_time_daily,
            'all_product_time_daily': json_all_product_time_daily,
            'background_colours_time_daily': json_bg_colours_time_daily,
            'border_colours_time_daily': json_b_colours_time_daily,

            'all_product_names_time_7days': json_all_product_names_time_7days,
            'all_product_time_7days': json_all_product_time_7days,
            'background_colours_time_7days': json_bg_colours_time_7days,
            'border_colours_time_7days': json_b_colours_time_7days,

            'all_product_names_time_monthly': json_all_product_names_time_monthly,
            'all_product_time_monthly': json_all_product_time_monthly,
            'background_colours_time_monthly': json_bg_colours_time_monthly,
            'border_colours_time_monthly': json_b_colours_time_monthly,
            }
    return render(request, 'profile.html', args)
