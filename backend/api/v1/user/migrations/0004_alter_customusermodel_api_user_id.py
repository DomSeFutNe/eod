# Generated by Django 5.1.6 on 2025-02-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_customusermodel_client_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='api_user_id',
            field=models.CharField(default='user_c0b897d5-795c-408f-9460-007d8e503cd0', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
