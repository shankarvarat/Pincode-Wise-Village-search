# Generated by Django 2.1 on 2019-08-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pincodeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pincode',
            name='Pincode',
            field=models.CharField(max_length=50),
        ),
    ]