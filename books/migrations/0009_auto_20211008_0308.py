# Generated by Django 3.2.8 on 2021-10-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_rename_borredbooks_borredbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Student', 'Student')], max_length=25),
        ),
    ]
