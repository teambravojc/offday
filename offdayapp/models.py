# Create your models here.
from django.db import models
from django.utils import timezone


class TeamMember(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OffDay(models.Model):
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)  # Assuming you have a TeamMember model
    day = models.CharField(max_length=10)  # Monday, Tuesday, etc.
    date_added = models.DateTimeField(default=timezone.now)  # Automatically stores when the record is created

    def __str__(self):
        return f"{self.team_member.name} - {self.day}"