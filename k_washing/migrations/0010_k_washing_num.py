# Generated by Django 4.0.3 on 2023-08-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k_washing', '0009_alter_k_washing_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='k_washing',
            name='num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
