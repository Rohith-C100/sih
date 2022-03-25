# Generated by Django 3.1.2 on 2022-03-24 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20220325_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lrating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.IntegerField()),
                ('r2', models.IntegerField()),
                ('r3', models.IntegerField()),
                ('r4', models.IntegerField()),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.lecturerfeedback')),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Crating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.IntegerField()),
                ('r2', models.IntegerField()),
                ('r3', models.IntegerField()),
                ('r4', models.IntegerField()),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.collegefeedback')),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.college')),
            ],
        ),
    ]
