# Generated by Django 3.1.2 on 2022-03-24 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20220325_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='percentage_of_student_above_60',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='student_passing_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='percentage_of_student_above_60',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='student_passing_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
