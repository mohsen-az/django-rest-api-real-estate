# Generated by Django 3.2.12 on 2022-02-23 19:36

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+989210000000', max_length=13, region=None, verbose_name='Phone Number')),
                ('about_me', models.TextField(default='Say something about yourself', verbose_name='About me')),
                ('licence', models.CharField(blank=True, max_length=20, null=True, verbose_name='Real Estate Licence')),
                ('photo', models.ImageField(default='simple_images/profile_default.png', upload_to='', verbose_name='Profile Photo')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default='OTHER', max_length=20, verbose_name='Gender')),
                ('country', django_countries.fields.CountryField(default='KE', max_length=2, verbose_name='Country')),
                ('city', models.CharField(blank=True, default='Nairobi', max_length=120, null=True, verbose_name='City')),
                ('is_buyer', models.BooleanField(default=False, help_text='Are you looking to buy a property?', verbose_name='Buyer')),
                ('is_seller', models.BooleanField(default=False, help_text='Are you looking to sell a property?', verbose_name='Seller')),
                ('is_agent', models.BooleanField(default=False, help_text='Are you an agent?', verbose_name='Agent')),
                ('top_agent', models.BooleanField(default=False, verbose_name='Top Agent')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Rating')),
                ('reviews', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Number of Reviews')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
