from django.db import models
from django.contrib.auth.models import User

class k_washing(models.Model):
    floor = models.CharField(max_length=5, choices=(("1", "1층"), ("2", "2층"), ("3", "3층"), ("4", "4층")))
    direction = models.CharField(max_length=5, choices=(("1", "방향1"), ("2", "방향2"), ("3", "방향3"), ("4", "방향4")))
    time = models.IntegerField()
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.author} :: {self.floor} :: {self.direction} :: {self.time} :: {self.content}'
    
    def get_absolute_url(self):
        return f'/k_washing/'