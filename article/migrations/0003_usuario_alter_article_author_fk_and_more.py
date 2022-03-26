# Generated by Django 4.0.3 on 2022-03-25 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_rename_author_article_author_fk_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='author_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.usuario'),
        ),
        migrations.AlterField(
            model_name='commemt_second_level',
            name='author_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.usuario'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.usuario'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
