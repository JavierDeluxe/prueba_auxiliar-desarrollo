# Generated by Django 4.0.3 on 2022-03-28 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_alter_article_author_fk_alter_comment_author_fk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_second_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.comment_second_level'),
        ),
    ]
