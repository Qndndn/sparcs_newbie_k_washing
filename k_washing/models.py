from django.db import models
from django.contrib.auth.models import User

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class k_washing(models.Model):
    floor = models.CharField(max_length=5, choices=(("1", "1층"), ("2", "2층"), ("3", "3층"), ("4", "4층")))
    direction = models.CharField(max_length=5, choices=(("1", "방향1"), ("2", "방향2"), ("3", "방향3"), ("4", "방향4")))
    time = models.IntegerField()
    moretime = IntegerRangeField(min_value=0, max_value=10, null=True)
    content = models.CharField(max_length=25, choices=( ("없음", "없음"), ("빨래가 끝난 후 바구니에 넣어주세요.", "빨래가 끝난 후 바구니에 넣어주세요."), ("세탁이 빨리 끝날 수 있습니다.", "세탁이 빨리 끝날 수 있습니다."), ("시간이 오래걸립니다.", "시간이 오래걸립니다."), ("향긋한 빨래 되세요:)", "향긋한 빨래 되세요:)"), ("K세탁 폼 미쳤다.", "K세탁 폼 미쳤다.")))
    finish_time = models.CharField(null=True, max_length=1000)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.author} :: {self.floor} :: {self.direction} :: {self.time} :: {self.content}'
    
    def get_absolute_url(self):
        return f'/k_washing/'
    
class k_washing_state(models.Model):
    floor_1 = models.IntegerField(null=True)
    direction_1 = models.IntegerField(null=True)
    time_first = models.IntegerField(null=True)
    state = models.IntegerField(null=True)
    pk_1 = models.IntegerField(null=True)