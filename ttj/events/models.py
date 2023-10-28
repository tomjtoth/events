import datetime as dt
from django.db import models as m
from django.contrib.auth.models import User


class Activity(m.Model):
    name = m.CharField(max_length=100, default="something")

    def __str__(self):
        return self.name


class Event(m.Model):
    name = m.CharField(max_length=200)
    datetime = m.DateTimeField(auto_now_add=True, blank=True)
    duration = m.DurationField(default=dt.timedelta(minutes=60))
    activities = m.ManyToManyField(Activity)
    participants = m.ManyToManyField(User)

    def __str__(self):
        return f"""{
                self.duration.total_seconds() / 60
            } minutes of {
                self.name
            } at {
                self.datetime.isoformat()
            } including {
                ', '.join([ str(a) for a in self.activities.all()])
            } with {
                ', '.join([ 

                    f"@{u.username}"
                    if u.get_full_name() == "" 
                    else u.get_full_name() 
                    
                    for u in self.participants.all()
                ])
            }"""
