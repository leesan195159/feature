# Generated by Django 4.1 on 2023-08-04 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_alter_curriculum_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lec_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]