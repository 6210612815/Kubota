# Generated by Django 4.0.5 on 2022-06-13 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_person_delete_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_1st', models.IntegerField()),
                ('pass_2nd', models.IntegerField()),
            ],
        ),
    ]
