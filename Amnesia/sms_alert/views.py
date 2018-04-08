from django.shortcuts import render, HttpResponse
from .forms import UserForm
from sms_alert.models import User

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        user_form = UserForm({
            'timezone': 'America/Los_Angeles',
        })
        time_zone = user_form.cleaned_data['timezone']

        temp = User(
            name = name,
            time_zone = time_zone,
            phone_number = phone_number,
            country = country
        )

        return HttpResponse("<h1>Successfully entered</h1>")


    else:
        form = UserForm()
        return render(request, 'sms_alert/index.html', {'form': form})


def next(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        time_zone = request.POST.get('timezone')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        return render(request, 'sms_alert/next.html', {
            'name' : name,
            'phone_number' : phone_number,
            'country' : country,
            'time_zone' : time_zone,
        })

    else:
        return render(request, 'sms_alert/next.html')

def form_save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        time_zone = request.POST.get('time_zone')
        awake_time = request.POST.get('awake_time')
        sleep_time = request.POST.get('sleep_time')
        print("-----------------------------------------------------", request.POST)
        temp = User(
            name=name,
            sleep_time=sleep_time,
            wake_time=awake_time,
            time_zone=time_zone,
            phone_number=phone_number,
            country=country
        )
        temp.save()
        form = UserForm()
        return render(request, 'sms_alert/index.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'sms_alert/index.html', {'form': form})
