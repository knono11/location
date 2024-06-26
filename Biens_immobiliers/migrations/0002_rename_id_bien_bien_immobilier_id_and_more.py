# Generated by Django 5.0.4 on 2024-04-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biens_immobiliers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bien_immobilier',
            old_name='id_bien',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='locataire',
            old_name='id_locataire',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='proprietaire',
            old_name='id_proprietaire',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='bien_immobilier',
            name='prix',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='contratlocation',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='demandereparation',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paiement',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
