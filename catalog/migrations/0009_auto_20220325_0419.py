# Generated by Django 3.1.2 on 2022-03-24 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20220325_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crating',
            name='r1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='crating',
            name='r2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='crating',
            name='r3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='crating',
            name='r4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='lrating',
            name='r1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='lrating',
            name='r2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='lrating',
            name='r3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='lrating',
            name='r4',
            field=models.IntegerField(default=0, null=True),
        ),
    ]