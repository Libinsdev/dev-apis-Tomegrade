# Generated by Django 4.0.5 on 2023-04-14 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apis', '0007_delete_usercart'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercart',
            fields=[
                ('uuid', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=300)),
                ('quantity', models.IntegerField(verbose_name=1)),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
