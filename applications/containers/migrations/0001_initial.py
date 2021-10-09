# Generated by Django 3.2.8 on 2021-10-09 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.JSONField()),
                ('password', models.CharField(max_length=4)),
                ('add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toilets', to='advertisements.advertisement')),
            ],
        ),
    ]
