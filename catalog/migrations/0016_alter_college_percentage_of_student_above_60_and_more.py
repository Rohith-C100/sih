# Generated by Django 4.0.3 on 2022-03-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_alter_college_id_alter_college_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='percentage_of_student_above_60',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='student_passing_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
