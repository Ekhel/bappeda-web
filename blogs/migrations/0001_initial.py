# Generated by Django 3.2.7 on 2022-03-04 16:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('aricle_image', models.ImageField(blank=True, default='article_images/default.png', null=True, upload_to='article_images/')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('id_article', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
    ]