# Generated by Django 4.1.2 on 2022-10-07 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seputaruntirta', '0003_alter_kelompok_keterangan_alter_kelompok_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='fakultas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seputaruntirta.kelompok'),
        ),
    ]