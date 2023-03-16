# Generated by Django 4.1.7 on 2023-03-12 16:36

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
            name='Task',
            fields=[
                ('item_num', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=200, null=True)),
                ('quantity', models.IntegerField(blank=True, max_length=2, null=True)),
                ('in_basket', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
