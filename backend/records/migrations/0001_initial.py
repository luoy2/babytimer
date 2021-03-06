# Generated by Django 3.1 on 2021-06-11 10:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('record_type', models.CharField(max_length=128)),
                ('start_time', models.DateTimeField()),
                ('duration', models.FloatField(default=0)),
                ('comments', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
        migrations.AddIndex(
            model_name='record',
            index=models.Index(fields=['start_time', 'record_type'], name='records_rec_start_t_e454a6_idx'),
        ),
    ]
