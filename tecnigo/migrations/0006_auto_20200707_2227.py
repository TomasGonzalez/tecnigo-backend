# Generated by Django 3.0.7 on 2020-07-07 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnigo', '0005_auto_20200629_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='tecnicalsupportstaff',
            name='HomeLocationLatitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='tecnicalsupportstaff',
            name='HomeLocationLongitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
    ]
