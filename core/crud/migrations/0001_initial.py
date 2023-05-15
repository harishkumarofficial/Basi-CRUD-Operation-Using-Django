# Generated by Django 4.2.1 on 2023-05-15 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'BooksCategory',
            },
        ),
        migrations.CreateModel(
            name='BookDeatils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, max_length=250, null=True)),
                ('author_name', models.CharField(max_length=50)),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updtated_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Book_category_name', to='crud.bookcategory')),
            ],
            options={
                'verbose_name_plural': 'BookDeatils',
            },
        ),
    ]
