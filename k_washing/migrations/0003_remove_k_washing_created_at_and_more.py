# Generated by Django 4.0.3 on 2023-08-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k_washing', '0002_remove_k_washing_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='k_washing',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='k_washing',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='k_washing',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
