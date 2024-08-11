# Generated by Django 4.2 on 2024-08-11 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=10, unique=True)),
                ('brand', models.CharField(max_length=45)),
                ('model', models.CharField(max_length=45)),
                ('color', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('Bajos', 'Bajos'), ('Guitarras Electro Acusticas', 'Guitarras Electro Acusticas'), ('Guitarras Acusticas', 'Guitarras Acusticas'), ('Guitarras Electricas', 'Guitarras Electricas'), ('Guitarras Clasicas', 'Guitarras Clasicas')], max_length=45)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_selling', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('picture', models.ImageField(upload_to='guitars_images')),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
