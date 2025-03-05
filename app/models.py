from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Redactor(AbstractUser):
    year_of_experience = models.IntegerField

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Topic(models.Model):
    name = models.CharField(max_length=63, unique=True)


def __str__(self):
    return f"{self.name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor)

    class Meta:
        ordering = ["published_date"]

    def __str__(self):
        return f"{self.title} was wrote on{self.published_date} by {self.publishers} about {self.topic}"
