# Generated by Django 4.0.3 on 2023-08-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k_washing', '0021_alter_k_washing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='k_washing',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]