# Generated by Django 4.2.3 on 2023-07-10 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='textanalysis',
            name='emotion',
        ),
        migrations.DeleteModel(
            name='Emotion',
        ),
        migrations.DeleteModel(
            name='TextAnalysis',
        ),
    ]
