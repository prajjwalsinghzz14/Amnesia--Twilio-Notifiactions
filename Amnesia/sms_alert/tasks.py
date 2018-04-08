from __future__ import absolute_import, unicode_literals
from celery import shared_task
from twilio.rest import Client
from django.conf import settings
from .models import User
import arrow

client = Client()
@shared_task
def send_sms_reminder(message_id):

    try:
        user = User.objects.get(pk=message_id)
    except User.DoesNotExist:
        return
    
    i = 0
    body=["Good morning {0}, did you get enough rest?",
           "Hi {0}, how about doing something new this morning?",
           "Hi {0}, how about a glass of water?",
           "Hi {0}, how do you imagine completing the task in your mind?",
           "Hi {0}, why don’t you have a fruit before lunch?",
           "Hi {0}, is there something you forgot to keep back in place?",
           "Hi {0}, how about a walk?",
           "Hi {0}, is there any grocery you had planned on buying today?",
           "Hi {0}, is there a birthday around the corner?",
           "Hi {0}, is there something you forgot to keep back in place?",
           "Hi {0}, how about a glass of water?",
           "Hi {0}, what was the best thing that happened today?",
           "This seems like a good time to get to bed. Goodnight {0}."
           ]

    body1 = body[i].format(
        user.name,
    )

    account_sid = "" #enter an auth_sid your Twillio Account here
    auth_token = "" #enetr aut?_token from your Twillio Account here
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        body=body1,
        to="+91947959730",
        from_=settings.TWILIO_NUMBER,

    )
