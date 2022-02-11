from django.db import models
import os
import datetime
import django
from django.utils import timezone
from django.utils.timezone import localtime

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

def get_duration(visit):
    now = localtime().replace(microsecond=0)
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at)
    duration = leaved_at - entered_at
    return duration.total_seconds()

def get_format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    format_duration = f"{hours}ч {minutes}мин"
    return format_duration

def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    is_strange = minutes <= duration/minutes
    return is_strange