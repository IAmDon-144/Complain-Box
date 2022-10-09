# Generated by Django 3.1.3 on 2022-07-08 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0004_auto_20220708_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descrioption', models.TextField()),
                ('privacy', models.CharField(choices=[('Public', 'Public'), ('Anonymous', 'Anonymous')], max_length=10)),
                ('complain_type', models.CharField(choices=[('Management', 'Management'), ('Class', 'Class'), ('Against Teacher', 'Against Teacher')], max_length=15)),
                ('suggestions', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.student')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Submitted', 'Submitted'), ('Checking', 'Checking'), ('Solved', 'Solved'), ('Closed', 'Closed')], max_length=10)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.complain')),
            ],
        ),
    ]