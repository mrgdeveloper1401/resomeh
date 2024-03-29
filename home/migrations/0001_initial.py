# Generated by Django 4.2.7 on 2023-11-06 16:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('auther', models.CharField(max_length=100, verbose_name='auther')),
            ],
            options={
                'verbose_name': 'authore',
                'verbose_name_plural': 'authore',
                'db_table': 'authore',
            },
        ),
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('full_name', models.CharField(max_length=100, verbose_name='full_name')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('mobile_phone', models.CharField(blank=True, max_length=11, verbose_name='mobile_phone')),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name': 'content us',
                'verbose_name_plural': 'contents us',
                'db_table': 'contents',
            },
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('skill_name', models.CharField(max_length=50, verbose_name='skill_name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='skill', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='SciolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('sciol_name', models.CharField(max_length=20, verbose_name='sciol name')),
                ('sciol_url', models.CharField(max_length=255, verbose_name='sciol url')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sciol', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'sciol',
                'verbose_name_plural': 'sciols',
                'db_table': 'sciol',
            },
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('title', models.CharField(max_length=50, verbose_name='title project')),
                ('explain_project', models.TextField(max_length=300, verbose_name='explain project')),
                ('project_url', models.URLField(blank=True, verbose_name='project url')),
                ('image', models.ImageField(blank=True, null=True, upload_to='project/%Y/%m/%d')),
                ('from_date', django_jalali.db.models.jDateField(verbose_name='from date')),
                ('up_to_date', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='up to date')),
                ('status_project', models.CharField(choices=[('s', 'start'), ('d', 'doing'), ('c', 'complate')], default='c', max_length=1, verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='ExpreienceWorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('job_title', models.CharField(max_length=50, verbose_name='job title')),
                ('organization_name', models.CharField(max_length=50, verbose_name='organization name')),
                ('explain_your_duties', models.TextField(help_text='Tell me something about your work experience.', max_length=500, verbose_name='explain your duties')),
                ('link_company', models.URLField(blank=True, null=True, verbose_name='link to company')),
                ('at_date_exprence', django_jalali.db.models.jDateField(verbose_name='at date')),
                ('to_date_exprence', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='to date')),
                ('status_work', models.CharField(choices=[('b', 'I am busy now'), ('d', 'I dont work here'), ('f', 'looking for work')], default='d', max_length=1, verbose_name='status work')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='experience', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'exprence',
                'verbose_name_plural': 'exprences',
                'db_table': 'exprences',
            },
        ),
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('fields_of_study', models.CharField(max_length=100, verbose_name='field of study')),
                ('university', models.CharField(max_length=100, verbose_name='university')),
                ('score', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='score')),
                ('explain_education', models.TextField(help_text='Describe where you were trained and educated', max_length=500, verbose_name='explain education')),
                ('at_education', django_jalali.db.models.jDateField(verbose_name='at time')),
                ('to_education', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='to time')),
                ('status_education', models.BooleanField(blank=True, default=False, verbose_name='studying')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='education', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'education',
                'verbose_name_plural': 'educations',
                'db_table': 'educations',
            },
        ),
        migrations.CreateModel(
            name='BoookArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='title')),
                ('year', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='year')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'book artiles',
                'verbose_name_plural': 'book artiles',
                'db_table': 'book_article',
            },
        ),
        migrations.CreateModel(
            name='AwardsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('awards_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='awards_name')),
                ('explain_awards', models.TextField(blank=True, max_length=500, null=True, verbose_name='explain awards')),
                ('year_awards', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='year')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='awards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'awards',
                'verbose_name_plural': 'awards',
                'db_table': 'awards',
            },
        ),
        migrations.CreateModel(
            name='AboutMeModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 6, 16, 10, 59, 31252, tzinfo=datetime.timezone.utc))),
                ('image', models.ImageField(blank=True, upload_to='aboutme/%Y/%m/%d')),
                ('explain', models.TextField(help_text='Write something about yourself', max_length=500, verbose_name='explain')),
                ('job', models.CharField(help_text='What is your current job?', max_length=50, verbose_name='job')),
                ('marital_status', models.CharField(choices=[('single', 'single'), ('married', 'married')], default='single', max_length=7, verbose_name='marital status')),
                ('gender_choose', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6, verbose_name='gender')),
                ('address', models.TextField(max_length=500)),
                ('birth_day', django_jalali.db.models.jDateField(verbose_name='birth day')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='about', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'about me',
                'verbose_name_plural': 'abouts me',
                'db_table': 'about_me',
            },
        ),
    ]
