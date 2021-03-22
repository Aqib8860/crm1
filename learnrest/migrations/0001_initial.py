# Generated by Django 3.1.3 on 2021-01-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('C', 'C'), ('C++', 'C++'), ('Java', 'Java'), ('Python', 'Python')], default='python', max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
