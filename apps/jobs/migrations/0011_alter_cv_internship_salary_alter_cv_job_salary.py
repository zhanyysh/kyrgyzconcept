# Generated by Django 4.2.6 on 2023-12-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_alter_cv_test_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='internship_salary',
            field=models.CharField(max_length=255, verbose_name='Желаемый размер Вашего вознаграждения на стажерский период'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='job_salary',
            field=models.CharField(max_length=255, verbose_name='Желаемый размер Вашего вознаграждения на основной период'),
        ),
    ]