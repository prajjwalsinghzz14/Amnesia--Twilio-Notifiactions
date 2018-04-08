from django.db import models
from Amnesia import celery_app
from datetime import datetime, time
from django.conf import settings
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from datetime import datetime
from timezone_field.fields import TimeZoneField
import arrow
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    sleep_time = models.TimeField(blank=False, default=datetime.now())
    wake_time = models.TimeField(blank=False, default=datetime.now())
    time_zone = TimeZoneField(default='US/Pacific')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    country = CountryField()
    
    # Additional fields not visible to users
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + ' - ' + self.phone_number



    def schedule_reminder(self):
       
        # Calculate the correct time to send this sms-alert
        sms_time = arrow.get(self.wake_time, self.time_zone.zone)
        reminder_time = sms_time.replace(minutes=+settings.REMINDER_TIME)

        # Schedule the Celery task
        from .tasks import send_sms_reminder
        result = send_sms_reminder.apply_async((self.pk,), eta=reminder_time)

        return result.id
    
        
