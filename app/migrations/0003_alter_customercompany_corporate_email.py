# Generated by Django 4.0.4 on 2022-08-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customercompany_company_worker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercompany',
            name='corporate_email',
            field=models.CharField(max_length=50),
        ),
    ]
