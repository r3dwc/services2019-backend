# Generated by Django 2.1.5 on 2019-01-19 16:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('surname', models.CharField(max_length=32, verbose_name='Surname')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('tel', models.CharField(max_length=15, null=True, verbose_name='Telephone number')),
                ('address', models.CharField(max_length=120, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_date', models.DateField(verbose_name='Date')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=36)),
                ('car_number', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='CarFuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CarList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_specifiction', models.TextField()),
                ('power', models.FloatField()),
                ('mileage', models.FloatField()),
                ('year', models.IntegerField()),
                ('fuel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.CarFuel')),
            ],
        ),
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CarTransmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('finished', models.BooleanField(default=False, verbose_name='Finished')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('answered', models.BooleanField(default=False)),
                ('answered_date', models.DateField(blank=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.CarList')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField()),
                ('price', models.FloatField()),
                ('details', models.TextField()),
                ('finished', models.BooleanField(default=False)),
                ('review', models.IntegerField()),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.Request')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('active', models.BooleanField(default=False)),
                ('car_make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.CarMake')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('company_name', models.CharField(max_length=32, verbose_name='Company Name')),
                ('reg', models.IntegerField(verbose_name='Reg')),
                ('vat', models.IntegerField(verbose_name='Vat')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=120, verbose_name='Company Name')),
                ('autoservice_name', models.CharField(max_length=120, verbose_name='Auto Service Name')),
                ('reg', models.IntegerField(verbose_name='Reg')),
                ('vat', models.IntegerField(verbose_name='Vat')),
                ('iban', models.CharField(max_length=120, verbose_name='Iban')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo_url', models.ImageField(blank=True, upload_to='', verbose_name='Photo')),
                ('approved', models.BooleanField(default=False, verbose_name='Approve')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='request',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.ServiceList'),
        ),
        migrations.AddField(
            model_name='chat',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receivers', to=settings.AUTH_USER_MODEL, verbose_name='Receiver'),
        ),
        migrations.AddField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='senders', to=settings.AUTH_USER_MODEL, verbose_name='Sender'),
        ),
        migrations.AddField(
            model_name='carlist',
            name='make',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.CarMake'),
        ),
        migrations.AddField(
            model_name='carlist',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.CarModel'),
        ),
        migrations.AddField(
            model_name='carlist',
            name='transmission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.CarTransmission'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.CarList', verbose_name='Car Type'),
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='servicelist',
            name='merchant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.Merchant'),
        ),
        migrations.AddField(
            model_name='booking',
            name='merchant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.Merchant', verbose_name='Merchant'),
        ),
    ]