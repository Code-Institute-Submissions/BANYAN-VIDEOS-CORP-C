# Generated by Django 3.1.2 on 2020-11-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_account', '0002_remove_userpurchasehistory_ph_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpurchasehistory',
            name='ph_purchase_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
