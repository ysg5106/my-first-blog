# Generated by Django 2.0.5 on 2018-06-02 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/%Y%m%d', verbose_name='파일')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y%m%d', verbose_name='이미지파일')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, verbose_name='제목')),
                ('content', models.TextField(blank=True, null=True, verbose_name='내용')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='날짜')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Posttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='구분')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Posttype'),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Post'),
        ),
        migrations.AddField(
            model_name='file',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Post'),
        ),
    ]
