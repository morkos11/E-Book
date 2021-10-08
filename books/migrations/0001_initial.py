# Generated by Django 3.2.8 on 2021-10-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('cover', models.ImageField(upload_to='books-images')),
                ('book_file', models.FileField(upload_to='books-files')),
                ('is_borred', models.BooleanField(default=False)),
                ('return_date', models.DateField(blank=True)),
            ],
        ),
    ]
