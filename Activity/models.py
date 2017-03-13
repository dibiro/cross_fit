from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    REPEATS_CHOICES = (
        ("1", "Weekly"),
        ("2", "Monthly"),
        ("3", "Yearly")
    )
    BOTTON_LABEL_CHOICES = (
        ("1", "Donate"),
        ("2", "Tithe"),
    )
    ASSIGNEE_TYPE_CHOICES = (
        ("1", "Instructor"),
        ("2", "Troinor"),
        ("3", "Umpire"),
        ("4", "Baby Sitter")
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    #date 
    star_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    star_day = models.DateField(blank=True, null=True)
    end_day = models.DateField(blank=True, null=True)
    is_recurring = models.BooleanField(default=False)
    is_all_day = models.BooleanField(default=False)
    repeats = models.CharField(
        max_length=2,
        choices=REPEATS_CHOICES,
        blank=True,
        null=True
    )
    every = models.IntegerField(blank=True, null=True)
    #location
    location = models.TextField()
    #payment
    is_reserve = models.BooleanField(default=False)
    is_pay = models.BooleanField(default=False)
    is_call_bussiness = models.BooleanField(default=False)
    amount = models.FloatField(blank=True, null=True)
    quantily_number = models.FloatField(blank=True, null=True)
    botton_label = models.CharField(max_length=2,
        choices=BOTTON_LABEL_CHOICES,
        blank=True,
        null=True
    )
    #settings
    is_visibility = models.BooleanField(default=True)
    is_schedule_required = models.BooleanField(default=True)
    is_documentation_required = models.BooleanField(default=True)
    is_digital_signature = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    auto_check_in = models.BooleanField(default=True)
    assignee_type = models.CharField(max_length=2,
        choices=ASSIGNEE_TYPE_CHOICES,
        blank=True,
        null=True
    )
    assignee_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Activity'

    def __unicode__(self):
        return 'Title: %s, Description: %s, Location: %s' % (
            self.title,
            self.description,
            self.location,
        )
