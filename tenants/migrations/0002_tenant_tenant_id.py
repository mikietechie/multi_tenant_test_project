# Generated by Django 3.2 on 2021-06-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='tenant_id',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]