# Generated by Django 2.1.2 on 2019-05-15 00:43

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
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Crag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=255, null=True)),
                ('number_of_routes', models.IntegerField(null=True)),
                ('rock_type', models.CharField(choices=[('granit', 'granit'), ('wapień', 'wapień'), ('piaskowiec', 'piaskowiec'), ('zlepieniec', 'zlepieniec')], max_length=50, null=True)),
                ('face', models.CharField(choices=[('N', 'N'), ('NW', 'NW'), ('NE', 'NE'), ('S', 'S'), ('SW', 'SW'), ('SE', 'SE')], max_length=6, null=True)),
                ('gps', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topo.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('grade', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('II+', 'II+'), ('III', 'III'), ('III+', 'III+'), ('IV', 'IV'), ('IV+', 'IV+'), ('V-', 'V-'), ('V', 'V'), ('V+', 'V+'), ('V+/VI-', 'V+/VI-'), ('VI-', 'VI-'), ('VI', 'VI'), ('VI+', 'VI+'), ('VI.1', 'VI.1'), ('VI.1+', 'VI.1+'), ('VI.2', 'VI.2'), ('VI.2+', 'VI.2+'), ('VI.2+/VI.3', 'VI.2+/VI.3'), ('VI.3', 'VI.3'), ('VI.3+', 'VI.3+'), ('VI.4', 'VI.4'), ('VI.4+', 'VI.4+'), ('VI.5', 'VI.5'), ('VI.5+', 'VI.5+'), ('VI.5+/6', 'VI.5+/6'), ('VI.6', 'VI.6'), ('VI.6+', 'VI.6+'), ('VI.7', 'VI.7'), ('VI.7+', 'VI.7+'), ('VI.8', 'VI.8')], max_length=10, null=True)),
                ('length', models.IntegerField(null=True)),
                ('type', models.CharField(choices=[('filar', 'filar'), ('komin', 'komin'), ('pion', 'pion'), ('połóg', 'połóg'), ('przewieszenie', 'przewieszenie'), ('zacięcie', 'zacięcie')], max_length=50, null=True)),
                ('pitches', models.IntegerField(null=True)),
                ('additional_info', models.CharField(max_length=255, null=True)),
                ('author', models.CharField(max_length=128, null=True)),
                ('crag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topo.Crag')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('number_of_crags', models.IntegerField(null=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topo.Region')),
            ],
        ),
        migrations.AddField(
            model_name='crag',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topo.Sector'),
        ),
    ]