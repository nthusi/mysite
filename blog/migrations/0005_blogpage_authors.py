# Generated by Django 4.2.16 on 2024-11-27 17:46

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="authors",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="blog.author"
            ),
        ),
    ]
