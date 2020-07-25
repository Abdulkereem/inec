# Generated by Django 3.0.8 on 2020-07-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Id_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=500)),
                ('logo', models.ImageField(blank=True, upload_to='logo')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('passport', models.ImageField(blank=True, upload_to='passport')),
                ('identity_text', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]