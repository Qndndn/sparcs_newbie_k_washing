# Generated by Django 4.0.3 on 2023-08-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k_washing', '0019_alter_k_washing_finish_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='k_washing',
            name='state',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
