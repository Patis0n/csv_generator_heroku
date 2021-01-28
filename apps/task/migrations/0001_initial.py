# Generated by Django 3.1.5 on 2021-01-25 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('start', models.IntegerField(blank=True, null=True, verbose_name='From')),
                ('end', models.IntegerField(blank=True, null=True, verbose_name='To')),
                ('kind', models.CharField(choices=[('name', 'Full name'), ('job', 'Job'), ('email', 'E-mail'), ('domain', 'Domain name'), ('phone', 'Phone number'), ('company', 'Company'), ('text', 'Text'), ('int', 'Integer'), ('address', 'Address'), ('date', 'Date')], max_length=16, verbose_name='Column type')),
            ],
            options={
                'verbose_name': 'Schema',
                'verbose_name_plural': 'Schemas',
            },
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Schema',
                'verbose_name_plural': 'Schemas',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField(blank=True, null=True, verbose_name='Rows')),
                ('status', models.IntegerField(choices=[(1, 'Error'), (5, 'In process'), (10, 'Completed')], verbose_name='Status')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.schema', verbose_name='Schema')),
            ],
            options={
                'verbose_name': 'Schema',
                'verbose_name_plural': 'Schemas',
            },
        ),
    ]