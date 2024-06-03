from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
from datetime import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class DaysOfTheWeek(models.TextChoices):
    MONDAY =   "MO", _("Monday") 
    TUESDAY =  "TU", _("Tuesday")
    WEDNESDAY= "WE", _("Wednesday")
    THURSDAY=  "TH", _("Thursday")
    FRIDAY=    "FR", _("Friday")
    SATURDAY=  "SA", _("Saturday")
    SUNDAY=    "SU", _("sunday")

class RecurrenceType(models.TextChoices):
        DAILY   = "DAILY",_("Daily") 
        WEEKLY  = "WEEKLY",_("Weekly") 
        MONTHLY = "MONTHLY",_("Monthly")
        YEARLY  = "YEARLY",_("Yearly")


class Event(models.Model):
    title = models.CharField(max_length=256, null= True, blank= True)
    location = models.CharField(max_length=256,blank= True , null= True)
    description = models.TextField(blank=True , null= True)

    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True, default= timezone.now)

    all_day = models.BooleanField(default= True)
    
    start_time = models.TimeField(null= True , blank= True)
    end_time = models.TimeField(null=True, blank=True)
    
    doesnot_repeat = models.BooleanField(default=True)

    repeat_every = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(1000)],null=True , blank= True, default= 1)
    repeataion_type = models.CharField(max_length=50 , choices= RecurrenceType.choices , default= "DAILY")

    repeat_on = models.CharField(max_length=50)

    never_end = models.BooleanField(default= True)
    end_on = models.DateField( null= True , blank=True)
    end_after = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(1000)] , null=True , blank=True)

    recurrence = models.CharField(max_length=256)
    google_calendar_event_id = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title