# Generated by Django 3.0 on 2019-12-03 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Административная область')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Страна происхождения')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Регион происхождения')),
                ('country', models.ManyToManyField(related_name='region', to='wino.Country', verbose_name='Страна происхождения')),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Марка качества')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quality', to='wino.Area')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quality', to='wino.Country')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quality', to='wino.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Напиток')),
                ('classification', models.CharField(blank=True, max_length=1, null=True)),
                ('quality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='drink', to='wino.Quality')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='area', to='wino.Region'),
        ),
    ]
