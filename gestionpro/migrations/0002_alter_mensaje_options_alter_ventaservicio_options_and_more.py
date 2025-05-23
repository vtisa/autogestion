# Generated by Django 5.2 on 2025-04-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensaje',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterModelOptions(
            name='ventaservicio',
            options={'ordering': ['-fecha_venta']},
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterModelTable(
            name='categoria',
            table='categorias',
        ),
        migrations.AlterModelTable(
            name='mensaje',
            table='mensajes',
        ),
        migrations.AlterModelTable(
            name='producto',
            table='productos',
        ),
        migrations.AlterModelTable(
            name='servicio',
            table='servicios',
        ),
        migrations.AlterModelTable(
            name='ventaservicio',
            table='venta_servicios',
        ),
    ]
