# Generated by Django 2.1 on 2018-10-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameJackpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet', models.IntegerField()),
                ('amount_for_bet', models.DecimalField(decimal_places=2, default=10.0, max_digits=20)),
                ('amount_won', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('amount_credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('spin', models.BooleanField(default=False)),
            ],
        ),
    ]