# Generated by Django 4.0.3 on 2022-03-14 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='document')),
                ('tag', models.TextField(blank=True, null=True)),
                ('data', models.TimeField(auto_now_add=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='DocFile')),
                ('slug', models.SlugField(blank=True, max_length=125, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kitoblar.type')),
            ],
        ),
    ]
