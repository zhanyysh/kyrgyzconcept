# Generated by Django 4.2.6 on 2023-11-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_cv_abroad_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='abroad_end',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='advisor_end',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='birthday',
            field=models.DateField(max_length=100, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='child_birthday',
            field=models.DateField(max_length=100, verbose_name='День рождение'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='internship_salary',
            field=models.IntegerField(verbose_name='Желаемый размер Вашего вознаграждения на стажерский период'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='job_salary',
            field=models.IntegerField(verbose_name='Желаемый размер Вашего вознаграждения на основной период'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='job_title_duty',
            field=models.DateField(verbose_name='Должностные обязанности'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='last_job_end',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='qualification_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
    ]