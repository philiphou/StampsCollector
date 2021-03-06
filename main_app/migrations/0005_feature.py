# Generated by Django 4.0.2 on 2022-02-09 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_stamp_release_year_stamp_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.CharField(choices=[('F', 'Five Cents'), ('E', 'Eight Cents'), ('T', 'Ten Cents')], default='F', max_length=1)),
                ('stamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.stamp')),
            ],
        ),
    ]
