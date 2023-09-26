# Generated by Django 4.2.5 on 2023-09-21 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.TextField(blank=True, null=True)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stylists', to='salons.salon')),
                ('services', models.ManyToManyField(blank=True, related_name='stylists', to='salons.service')),
            ],
        ),
        migrations.AddField(
            model_name='salon',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='salons', to='salons.service'),
        ),
    ]