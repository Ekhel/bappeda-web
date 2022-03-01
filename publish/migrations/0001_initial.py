# Generated by Django 3.2.7 on 2022-03-01 15:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('kategori', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dokumen',
            fields=[
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('tgl_produksi', models.DateField(blank=True, null=True)),
                ('tgl_buat', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publish.kategori')),
            ],
        ),
    ]
