# Generated by Django 3.2.21 on 2024-02-21 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('name_ja', models.CharField(blank=True, max_length=255, null=True)),
                ('name_ja_hiragana', models.CharField(blank=True, max_length=255, null=True)),
                ('another_name', models.CharField(blank=True, max_length=255, null=True)),
                ('group_name', models.CharField(blank=True, max_length=255, null=True)),
                ('background', models.TextField(blank=True, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('count_rep', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('count_cou', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.CharField(max_length=100, null=True, unique=True)),
                ('twitter_name', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_follow', models.PositiveIntegerField(blank=True, null=True)),
                ('twitter_follower', models.PositiveIntegerField(blank=True, null=True)),
                ('homepage', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_id', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_name', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_follower', models.PositiveIntegerField(blank=True, null=True)),
                ('youtube_video_num', models.PositiveIntegerField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seizi.people')),
            ],
        ),
        migrations.CreateModel(
            name='Representatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_proportional', models.BooleanField()),
                ('block', models.CharField(blank=True, max_length=50, null=True)),
                ('nd', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('expire', models.DateTimeField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seizi.people')),
            ],
        ),
        migrations.CreateModel(
            name='HouseOfCouncillors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_proportional', models.BooleanField()),
                ('block', models.CharField(blank=True, max_length=50, null=True)),
                ('nd', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('expire', models.DateTimeField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seizi.people')),
            ],
        ),
    ]
