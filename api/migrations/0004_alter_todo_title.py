# Generated by Django 4.1.3 on 2022-11-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_todo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(blank=True, default='', help_text='TODO name', max_length=30, null=True),
        ),
    ]
