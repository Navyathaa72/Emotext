# Generated by Django 4.2.3 on 2023-07-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_text_remove_textanalysis_emotion_delete_emotion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
