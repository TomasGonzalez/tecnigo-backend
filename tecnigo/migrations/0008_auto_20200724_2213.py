# Generated by Django 3.0.7 on 2020-07-24 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecnigo', '0007_auto_20200724_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='ADDRESS',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='AGE',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='CELL_PHONE',
            new_name='cell_phone',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='EDUCATION',
            new_name='education',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='FIRST_NAME',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='HOME_LOCATION_LATITUDE',
            new_name='home_location_latitude',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='HOME_LOCATION_LONGITUDE',
            new_name='home_location_longitude',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='LAST_NAME',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='ID',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='PHONE_OS',
            new_name='phone_os',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='PROFESSION',
            new_name='profession',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='Q1_ANSWER',
            new_name='q1_answer',
        ),
        migrations.RenameField(
            model_name='tecnicalsupportstaff',
            old_name='STORY',
            new_name='story',
        ),
        migrations.RemoveField(
            model_name='tecnicalsupportstaff',
            name='PHONE',
        ),
    ]