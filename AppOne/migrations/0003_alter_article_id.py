# Generated by Django 3.2 on 2021-04-11 15:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0002_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
