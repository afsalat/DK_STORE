# Generated by Django 3.2.19 on 2023-05-21 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0007_footer_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_pro_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=150)),
                ('pro_desc', models.TextField()),
                ('pro_img', models.ImageField(null=True, upload_to='all_products')),
                ('pro_sizes', models.IntegerField()),
                ('pro_colors', models.CharField(max_length=150)),
                ('pro_price', models.IntegerField()),
                ('pro_stock', models.IntegerField()),
                ('pro_cate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
