# Generated by Django 4.0.3 on 2022-03-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workpage', '0003_alter_document_file_alter_document_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
