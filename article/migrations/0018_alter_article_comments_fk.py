# Generated by Django 4.0.3 on 2022-03-28 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_rename_comments_article_comments_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comments_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.comment'),
        ),
    ]
