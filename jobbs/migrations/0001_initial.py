# Generated by Django 3.0.2 on 2020-02-23 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='image_jobbs')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(help_text='Address', max_length=60)),
                ('city', models.CharField(help_text='City', max_length=40)),
                ('country', models.CharField(help_text='Country', max_length=30)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]