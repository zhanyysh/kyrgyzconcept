# Generated by Django 4.2.6 on 2023-12-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_alter_cv_google_docs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='google_docs',
            field=models.BooleanField(blank=True, default=False, verbose_name='Google Документы'),
        ),
    ]