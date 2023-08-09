# Generated by Django 4.1 on 2023-08-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='chapter_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='idx',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='lecture_idx',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='pages',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='remark',
            field=models.CharField(max_length=150, null=True),
        ),
    ]