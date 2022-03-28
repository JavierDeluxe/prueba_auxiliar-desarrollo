# Generated by Django 4.0.3 on 2022-03-28 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_alter_article_comments_fk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comments_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_second_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.comment_second_level'),
        ),
    ]