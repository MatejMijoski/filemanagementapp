# Generated by Django 3.1 on 2020-12-11 15:13

import FileUpload.models
import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
            options={
                'verbose_name': 'Admin Tags',
                'verbose_name_plural': 'AdminTags',
            },
        ),
        migrations.CreateModel(
            name='AdminTagsAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fileupload_admintagsall_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fileupload_admintagsall_items', to='FileUpload.admintags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
            options={
                'verbose_name': 'User Tags',
                'verbose_name_plural': 'UserTags',
            },
        ),
        migrations.CreateModel(
            name='UserTagsAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fileupload_usertagsall_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fileupload_usertagsall_items', to='FileUpload.usertags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Uploaded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_uploaded', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, upload_to=FileUpload.models.user_directory_path)),
                ('additional_description', models.CharField(blank=True, max_length=50)),
                ('link', models.CharField(max_length=300)),
                ('admintags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='FileUpload.AdminTagsAll', to='FileUpload.AdminTags', verbose_name='Admin Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
                ('usertags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='FileUpload.UserTagsAll', to='FileUpload.UserTags', verbose_name='User Tags')),
            ],
            options={
                'verbose_name': 'File',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='FileUpload.uploaded')),
            ],
        ),
    ]
