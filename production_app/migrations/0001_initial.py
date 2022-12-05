# Generated by Django 4.1.2 on 2022-12-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('seeding_method', models.CharField(choices=[('direct_seeding', 'Semis direct'), ('bulbs', 'Bulbilles'), ('tray', 'Plaque'), ('outsourced', 'Fournisseur')], max_length=20)),
                ('number_of_seeds_per_hole', models.IntegerField()),
                ('tray_type', models.IntegerField(choices=[('15', '15'), ('20', '20'), ('48', '48'), ('77', '77'), ('150', '15'), ('273', '273')])),
                ('planting_grid', models.CharField(choices=[('1x1', '1x1'), ('1x2', '1x2'), ('2x2', '2x2'), ('3x3', '3x3'), ('4x4', '4x4'), ('6x6', '6x6')], max_length=20)),
                ('direct_seeding_instructions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20, unique=True)),
                ('number_of_beds', models.IntegerField()),
                ('bed_length', models.FloatField()),
                ('bed_width', models.FloatField()),
                ('expected_number_of_rotations_per_year', models.FloatField()),
                ('expected_income_per_rotation', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('variety', models.CharField(max_length=20)),
                ('bed_number', models.CharField(max_length=20)),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(choices=[('kg', 'kg'), ('bottes', 'bottes'), ('pièces', 'pièces')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('event', models.CharField(choices=[('planting', 'Plantation'), ('seeding', 'Semis'), ('first_harvest', 'Première récolte'), ('last_harvest', 'Dernière récolte'), ('termination', 'Abandon')], max_length=20)),
                ('bed_number', models.IntegerField()),
                ('reason_for_termination', models.CharField(choices=[('bitten_by_frost', 'Gel'), ('went_to_seed', 'Montée en graine'), ('too_slow', 'Croissance trop lente'), ('bad_quality', 'Qualité insuffisante'), ('better_alternative', 'Sacrifié pour une autre'), ('bad_germination', 'Mauvaise germination'), ('eaten_by_pest', 'Ravageur')], max_length=20)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
