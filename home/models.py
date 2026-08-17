from django.db import models


class Opportunity(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    how_to_apply = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    deadline = models.DateField()
    application_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
