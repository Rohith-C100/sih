# Generated by Django 3.1.2 on 2022-03-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20220325_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegefeedback',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]