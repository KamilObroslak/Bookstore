# Generated by Django 4.1.4 on 2022-12-30 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_ksiazki_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'verbose_name': 'Ksiażka',
                'verbose_name_plural': 'Ksiażki',
            },
        ),
        migrations.RenameField(
            model_name='category',
            old_name='opis',
            new_name='category_desc',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='nazwa',
            new_name='category_name',
        ),
        migrations.DeleteModel(
            name='Ksiazki',
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Books.category'),
        ),
    ]