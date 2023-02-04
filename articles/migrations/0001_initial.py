# Generated by Django 3.2.13 on 2023-02-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100)),
                ('answer1', models.TextField(max_length=100)),
                ('answer1_letter', models.CharField(blank=True, max_length=1, null=True)),
                ('answer2', models.TextField(max_length=100)),
                ('answer2_letter', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=100)),
                ('verse', models.TextField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('personality', models.TextField(blank=True, max_length=100)),
                ('like', models.TextField(blank=True, max_length=50)),
                ('dislike', models.TextField(blank=True, max_length=50)),
                ('good_match_img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('good_match', models.CharField(blank=True, max_length=10)),
                ('bad_match_img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('bad_match', models.CharField(blank=True, max_length=10)),
                ('mbti', models.CharField(max_length=10)),
            ],
        ),
    ]
