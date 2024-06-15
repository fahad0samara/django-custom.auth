# Generated by Django 5.0.6 on 2024-06-15 04:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth0", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="last_login",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
