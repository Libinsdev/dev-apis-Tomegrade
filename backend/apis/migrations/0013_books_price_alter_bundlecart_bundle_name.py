# Generated by Django 4.0.5 on 2023-04-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0012_alter_bundlecart_bundle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.IntegerField(blank=True, default=550, null=True),
        ),
        migrations.AlterField(
            model_name='bundlecart',
            name='bundle_name',
            field=models.ManyToManyField(related_name='bundle', to='apis.books'),
        ),
    ]
