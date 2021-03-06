# Generated by Django 3.2 on 2021-04-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diabetes1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eating', models.TextField()),
                ('exercises', models.TextField()),
                ('protect', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dobesity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eat', models.CharField(max_length=200)),
                ('exercise', models.CharField(max_length=200)),
                ('feel', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dyslipidemia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eat', models.TextField()),
                ('exercises', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EatQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.CharField(max_length=200)),
                ('typename1', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='exerciseQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score2', models.CharField(max_length=200)),
                ('typename2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='hypertention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit', models.TextField()),
                ('exercises', models.TextField()),
                ('feeling', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NameHospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('provinces', models.CharField(max_length=200)),
                ('Phonenumber', models.CharField(max_length=200)),
                ('Desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=200)),
                ('typename', models.CharField(max_length=200)),
            ],
        ),
    ]
