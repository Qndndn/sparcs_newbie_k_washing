# Generated by Django 4.0.3 on 2023-08-20 14:03

from django.db import migrations, models
import k_washing.models


class Migration(migrations.Migration):

    dependencies = [
        ('k_washing', '0006_k_washing_finish_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='k_washing',
            name='moretime',
            field=k_washing.models.IntegerRangeField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='k_washing',
            name='content',
            field=models.CharField(choices=[('2', '빨래가 끝난 후 바구니에 넣어주세요.'), ('3', '세탁이 빨리 끝날 수 있습니다.'), ('4', '시간이 오래걸립니다.'), ('1', '없음')], max_length=5),
        ),
    ]
