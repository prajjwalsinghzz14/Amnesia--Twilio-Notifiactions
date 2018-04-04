from __future__ import absolute_import, unicode_literals
from celery import shared_task
from twilio.rest import Client
from django.conf import settings
from .models import User
import arrow

def add(x,y):
    return x+y

client = Client()

@shared_task
def send_sms_reminder(message_id):

    try:
        user = User.objects.get(pk=message_id)
    except User.DoesNotExist:
        return

    message_time = arrow.get(user.wake_time, user.time_zone)

    body1=["", "", "", ""]

    body = 'Hi {0}. You have an appointment coming up at {1}.'.format(
        user.name,
    )

    account_sid = "ACb574c410df67869201b7f70445975cce"
    auth_token = "1b2ec3eb28eb40a04d50949be8b6e8af"
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        body=body,
        to="+91947959730",
        from_=settings.TWILIO_NUMBER,

    )
