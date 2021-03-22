# Generated by Django 3.1.3 on 2021-02-16 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learnrest', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPositions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('experience_req', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('resume', models.FileField(upload_to='')),
                ('mobile', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('recent_education', models.CharField(max_length=100, null=True)),
                ('last_exp', models.IntegerField(null=True)),
                ('job_position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='learnrest.jobpositions')),
            ],
        ),
    ]
