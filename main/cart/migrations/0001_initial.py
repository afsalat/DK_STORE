# Generated by Django 3.2.19 on 2023-06-22 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0012_auto_20230613_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=150)),
                ('pro_desc', models.TextField()),
                ('pro_img', models.ImageField(null=True, upload_to='leatest_products')),
                ('pro_sizes', models.IntegerField(null=True)),
                ('pro_colors', models.CharField(max_length=150, null=True)),
                ('pro_price', models.IntegerField(null=True)),
                ('pro_stock', models.IntegerField(null=True)),
                ('person_id', models.CharField(max_length=150, null=True)),
                ('pro_cate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]