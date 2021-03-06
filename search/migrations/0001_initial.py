# Generated by Django 2.2.3 on 2021-04-14 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0003_auto_20210414_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=100)),
                ('phone_numer', models.CharField(max_length=20, verbose_name='Telefon raqam')),
                ('mode', models.CharField(max_length=200)),
                ('kimlar', models.CharField(max_length=200)),
                ('kishilar', models.CharField(max_length=200)),
                ('topshirilgan', models.CharField(max_length=200)),
                ('moneyc', models.CharField(max_length=200)),
                ('floor', models.CharField(max_length=200)),
                ('floormany', models.CharField(blank=True, max_length=200)),
                ('rooms', models.CharField(max_length=200)),
                ('money', models.CharField(max_length=100, verbose_name='Pul muomilasini kiriting')),
                ('tartiblar', models.TextField(verbose_name='Uyingizdagi tartiblarni kiriting')),
                ('ish', models.TextField(verbose_name='Ijarachiga ish taklif qila olasizmi')),
                ('sovuq_suv', models.CharField(max_length=200)),
                ('issiq_suv', models.CharField(max_length=200)),
                ('svet', models.CharField(max_length=200)),
                ('gaz', models.CharField(max_length=200)),
                ('additional2', models.TextField(verbose_name="Qo'shimcha kiriting")),
                ('wifi', models.CharField(max_length=200)),
                ('sovutgich', models.CharField(max_length=200)),
                ('kondisioner', models.CharField(max_length=200)),
                ('additional3', models.TextField(verbose_name="Qo'shimcha kiriting")),
                ('hammom', models.CharField(max_length=200)),
                ('additional4', models.TextField(verbose_name="Qo'shimcha kiriting")),
                ('xafsiz', models.CharField(max_length=200)),
                ('additional5', models.TextField(verbose_name="Qo'shimcha kiriting")),
                ('likes', models.ManyToManyField(blank=True, related_name='announcement_like', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.Householder')),
            ],
            options={
                'verbose_name': "1. E'lonlar",
                'verbose_name_plural': "1. E'lonlar",
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nechanchi qavat')),
            ],
            options={
                'verbose_name': '3. Uy Nechanchi qavat tanlashlar',
                'verbose_name_plural': '3. Uy Nechanchi qavat tanlashlar',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Honalar soni')),
            ],
            options={
                'verbose_name': '3. Honalar soni',
                'verbose_name_plural': '3. Honalar soni',
            },
        ),
        migrations.CreateModel(
            name='Streets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streets', models.CharField(max_length=500, verbose_name='Eslatmali qisqa manzilni kiriting')),
            ],
            options={
                'verbose_name': '4. Manzillarni eslatuvchi manzillar',
                'verbose_name_plural': '4. Manzillarni eslatuvchi manzillar',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('announcements', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search.Announcement')),
            ],
        ),
    ]
