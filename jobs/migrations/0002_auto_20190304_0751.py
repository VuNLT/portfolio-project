# Generated by Django 2.1.5 on 2019-03-04 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
                ('session', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UrlHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('hits', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='hitcount',
            name='url_hit',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='jobs.UrlHit'),
        ),
    ]
