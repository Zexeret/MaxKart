# Generated by Django 3.1.2 on 2020-11-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_haircut'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'CurrentOrder',
            },
        ),
        migrations.AlterField(
            model_name='haircut',
            name='card_id',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
    ]
