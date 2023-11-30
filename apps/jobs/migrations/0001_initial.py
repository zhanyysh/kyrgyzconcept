# Generated by Django 4.2.6 on 2023-11-29 12:02

import ckeditor.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='user_cvs/', verbose_name='Аватар')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('citizenship', models.CharField(max_length=100, verbose_name='Гражданство')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('gender', models.CharField(default=None, max_length=10, verbose_name='Пол')),
                ('children', models.BooleanField(default=False, verbose_name='Есть ли у Вас дети?')),
                ('child_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя ребенка')),
                ('child_birthday', models.DateField(blank=True, null=True, verbose_name='День рождение ребенка')),
                ('source', models.CharField(max_length=100, verbose_name='Источник информации о вакансии')),
                ('reason', models.CharField(max_length=250, verbose_name='Почему Вы выбрали именно эту эпозицию?')),
                ('interested_position', models.CharField(max_length=250, verbose_name='Готовы ли рассматривать другие позиции в Kyrgyz Concept?')),
                ('candidate', models.BooleanField(default=False, verbose_name='Можем ли мы рассматривать Вашу кандидатуру для наших партнеров?')),
                ('republic_test', models.BooleanField(default=False, verbose_name='Проходили ли Вы общереспубликанское тестирование?')),
                ('test_year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('test_score', models.IntegerField(blank=True, null=True, verbose_name='Балл')),
                ('ielts_toefl', models.BooleanField(default=False, verbose_name='Сдавали ли Вы TOEFL/IELTS?')),
                ('exam_year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('exam_score', models.IntegerField(blank=True, null=True, verbose_name='Балл')),
                ('education', models.BooleanField(default=False, verbose_name='Собираетесь ли Вы в течение ближайших трех лет продолжить свое образование?')),
                ('education_info', models.TextField(blank=True, null=True, verbose_name='Дальнейшее обучение')),
                ('qualification', models.BooleanField(default=False, verbose_name='Повышение квалификации (участие в семинарах, тренингах, наличие сертификатов, прохождение курсов)')),
                ('qualification_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название квалификации')),
                ('qualification_country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна квалификации')),
                ('qualification_city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город квалификации')),
                ('qualification_start', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('qualification_end', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('organisation_name', models.CharField(max_length=100, verbose_name='Название организации')),
                ('organisation_address', models.CharField(max_length=100, verbose_name='Адрес организации')),
                ('job_title', models.CharField(max_length=100, verbose_name='Должность')),
                ('last_job_start', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('last_job_end', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('job_title_duty', models.CharField(max_length=100, verbose_name='Должностные обязанности')),
                ('base_moves', models.CharField(max_length=100, verbose_name='Основные движения')),
                ('dismissal_reason', models.CharField(blank=True, max_length=100, null=True, verbose_name='Причина увольнения')),
                ('advisor', models.CharField(max_length=100, verbose_name='ФИО')),
                ('advisor_organisation', models.CharField(max_length=100, verbose_name='Название организации')),
                ('advisor_start', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('advisor_end', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('advisor_address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('advisor_phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('advisor_socials', models.CharField(blank=True, max_length=250, null=True, verbose_name='Соц сети рекомендателя')),
                ('advisor_job', models.CharField(max_length=100, verbose_name='Должность рекомендателя')),
                ('internship_salary', models.CharField(max_length=100, verbose_name='Желаемый размер Вашего вознаграждения на стажерский период')),
                ('job_salary', models.CharField(max_length=100, verbose_name='Желаемый размер Вашего вознаграждения на основной период')),
                ('language', models.CharField(max_length=100, verbose_name='Знание языков')),
                ('language_knowledge', models.CharField(max_length=100, verbose_name='Степень знания')),
                ('language_years', models.CharField(max_length=100, verbose_name='Сколько лет изучал')),
                ('google_docs', models.BooleanField(blank=True, default=False, null=True, verbose_name='Google Документы')),
                ('google_tables', models.BooleanField(blank=True, default=False, null=True, verbose_name='Google Таблицы')),
                ('google_presentation', models.BooleanField(blank=True, default=False, null=True, verbose_name='Google Презентации')),
                ('prezi', models.BooleanField(blank=True, default=False, null=True, verbose_name='Prezi')),
                ('touch_typing', models.BooleanField(blank=True, default=False, null=True, verbose_name='Слепая печать')),
                ('abroad_country', models.CharField(max_length=100, verbose_name='Пребывание за границей')),
                ('abroad_start', models.BooleanField(default=False, verbose_name='Дата начала')),
                ('abroad_end', models.BooleanField(default=False, verbose_name='Дата окончания')),
                ('abroad_reason', models.CharField(max_length=100, verbose_name='Причина визита')),
                ('good_skills', models.CharField(max_length=250, verbose_name='Полезные навыки')),
                ('linkedin', models.URLField(verbose_name='Linkedin')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(verbose_name='Twitter')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, default='/jobs_image/blank_avatar.jpg', force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='jobs_image/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('money', models.CharField(blank=True, max_length=255, null=True, verbose_name='Зарплата')),
                ('work', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('oclock', models.CharField(blank=True, max_length=255, null=True, verbose_name='Часы работы')),
                ('responsiblities', ckeditor.fields.RichTextField(verbose_name='Обязанности')),
                ('expectations', ckeditor.fields.RichTextField(verbose_name='Ожидание')),
                ('experience', models.CharField(blank=True, max_length=255, null=True, verbose_name='Опыт')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='ReadyCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='user_cvs/', verbose_name='Аватар')),
                ('cv_file', models.ImageField(upload_to='CVs/', verbose_name='Резюме')),
            ],
            options={
                'verbose_name': 'Готовое Резюме',
                'verbose_name_plural': 'Готовые Резюме',
            },
        ),
    ]