# Generated by Django 3.1.2 on 2022-03-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegefeedback',
            name='four',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='collegefeedback',
            name='three',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='collegefeedback',
            name='w1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='collegefeedback',
            name='w2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='collegefeedback',
            name='w3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='collegefeedback',
            name='w4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='lecturerfeedback',
            name='four',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lecturerfeedback',
            name='three',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lecturerfeedback',
            name='w1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='lecturerfeedback',
            name='w2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='lecturerfeedback',
            name='w3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='lecturerfeedback',
            name='w4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='collegefeedback',
            name='one',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='collegefeedback',
            name='two',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lecturerfeedback',
            name='one',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lecturerfeedback',
            name='two',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
