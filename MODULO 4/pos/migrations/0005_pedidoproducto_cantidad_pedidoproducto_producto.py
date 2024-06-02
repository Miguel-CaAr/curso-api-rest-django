# Generated by Django 5.0.6 on 2024-05-31 03:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_alter_producto_categoria_pedido_pedidoproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoproducto',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='pos.producto'),
            preserve_default=False,
        ),
    ]