# Generated by Django 4.1.4 on 2022-12-27 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem')),
            ],
        ),
    ]
