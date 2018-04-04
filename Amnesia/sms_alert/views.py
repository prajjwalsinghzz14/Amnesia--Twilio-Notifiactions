from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .forms import UserForm
from sms_alert.models import User

temp_pk=0;
temp=User()

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        #sleep_time = request.POST.get('sleep_time')
        #wake_time = request.POST.get('wake_time')
        user_form = UserForm({
            'timezone': 'America/Los_Angeles',
        })
        time_zone = user_form.cleaned_data['timezone']

        temp = User(
            name = name,
          #  sleep_time=sleep_time,
           # wake_time=wake_time,
            time_zone = time_zone,
            phone_number = phone_number,
            country = country
        )
        temp_pk = temp.pk;
        temp.save()
        return HttpResponse("<h1>Successfully entered</h1>")
        #return render(request, 'sms_alert/index.html' )

    else:
        form = UserForm()
        return render(request, 'sms_alert/index.html', {'form': form})


def next(request):

    if request.method == 'POST':

        sleep_time = request.POST.get('sleep_time')
        wake_time = request.POST.get('wake_time')

        temp = User(
            sleep_time = sleep_time,
            wake_time = wake_time,
        )
        temp.save()
        return HttpResponse("<h1>Successfully entered</h1>")

    else:
        return render(request, 'sms_alert/index.html')