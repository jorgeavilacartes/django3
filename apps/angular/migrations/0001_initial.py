# Generated by Django 3.0.1 on 2020-01-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestAngular',
            fields=[
                ('test_angular_id', models.AutoField(db_column='TEST_ANGULAR_ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('test_angular_text', models.CharField(blank=True, db_column='TEST_ANGULAR_TEXT', max_length=200, null=True, verbose_name='TEXT')),
                ('test_angular_bool', models.BooleanField(blank=True, db_column='TEST_ANGULAR_BOOL', null=True, verbose_name='BOOL')),
            ],
        ),
    ]