# Generated by Django 4.0.3 on 2023-08-20 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('k_washing', '0015_alter_k_washing_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='k_washing',
            name='num',
        ),
    ]
