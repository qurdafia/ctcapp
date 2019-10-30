from django.db import models


class Survey(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    comment = models.TextField(null=False)
    submitted = models.DateField(null=True)

    def __str__(self):
        return self.first_name
