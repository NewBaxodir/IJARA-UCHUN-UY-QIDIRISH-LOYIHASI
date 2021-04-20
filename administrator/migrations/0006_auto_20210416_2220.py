# Generated by Django 2.2.3 on 2021-04-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
        ('administrator', '0005_auto_20210414_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='householder',
            name='addd',
        ),
        migrations.AddField(
            model_name='user',
            name='addd',
            field=models.ManyToManyField(blank=True, related_name='announcement_add', to='search.Announcement'),
        ),
    ]