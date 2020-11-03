# Generated by Django 3.1.2 on 2020-11-02 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(blank=True, max_length=254, null=True)),
                ('genre_friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Genre',
            },
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_sku', models.CharField(blank=True, max_length=100, null=True)),
                ('film_title', models.CharField(blank=True, max_length=254, null=True)),
                ('film_friendly_title', models.CharField(blank=True, max_length=254, null=True)),
                ('film_box_cover_url', models.URLField(default='', max_length=254)),
                ('film_description', models.TextField(blank=True, max_length=2000, null=True)),
                ('film_price', models.DecimalField(decimal_places=2, default=9.99, max_digits=5)),
                ('film_product_discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('film_stock_available', models.BooleanField(default=True)),
                ('film_global_sale', models.BooleanField(default=True)),
                ('film_clip_link', models.URLField(blank=True, max_length=254, null=True)),
                ('film_genre', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='films.genre')),
            ],
            options={
                'verbose_name': 'Films',
            },
        ),
    ]
