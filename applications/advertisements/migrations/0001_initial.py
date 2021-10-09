# Generated by Django 3.2.8 on 2021-10-09 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=66)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='')),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('duration', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('not_paid', 'Not Paid'), ('expired', 'Expired')], max_length=15)),
                ('is_validated', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
