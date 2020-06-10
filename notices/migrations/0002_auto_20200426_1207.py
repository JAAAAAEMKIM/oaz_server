# Generated by Django 3.0.5 on 2020-04-26 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likenoticecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notices.Comment'),
        ),
        migrations.AddField(
            model_name='likenoticecomment',
            name='comment_liked_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_notice_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likenotice',
            name='notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notices.Notice'),
        ),
        migrations.AddField(
            model_name='likenotice',
            name='notice_liked_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_notice', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_comment_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notices.Notice'),
        ),
    ]
