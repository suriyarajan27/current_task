from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODOTASK(models.Model):
    task_name = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
