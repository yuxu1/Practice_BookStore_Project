# Generated by Django 4.2.13 on 2024-07-02 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="pic",
            field=models.ImageField(default="untitled_book.png", upload_to="books"),
        ),
    ]
