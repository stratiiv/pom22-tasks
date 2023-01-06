# Generated by Django 4.1 on 2022-08-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_count_book_description_book_name_alter_book_id'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='book.book'),
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='author',
            name='patronymic',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='author',
            name='surname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
