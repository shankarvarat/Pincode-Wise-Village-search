# Generated by Django 2.1 on 2019-08-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pincode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Village', models.CharField(max_length=50)),
                ('Pincode', models.IntegerField()),
                ('District', models.CharField(max_length=50)),
                ('StateName', models.CharField(max_length=50)),
            ],
        ),
    ]