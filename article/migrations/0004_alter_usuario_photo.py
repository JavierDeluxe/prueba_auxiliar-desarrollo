# Generated by Django 4.0.3 on 2022-03-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_usuario_alter_article_author_fk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]