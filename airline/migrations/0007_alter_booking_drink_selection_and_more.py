# Generated by Django 4.0.4 on 2022-04-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0006_airplane_airplane_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='drink_selection',
            field=models.CharField(blank=True, choices=[('Aperol Spritz', 'Aperol Spritz'), ('Jack and Coke', 'Jack and Coke'), ('Rum and Coke', 'Rum and Coke'), ('White Wine', 'White Wine'), ('Red Wine', 'Red Wine'), ('Champagne', 'Champagne'), ('Aperol Spritz', 'Aperol Spritz'), ('Screwdriver', 'Screwdriver'), ('Bloody Mary', 'Bloody Mary'), ('Pilsner', 'Pilsner'), ('IPA', 'IPA')], max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='food_selection',
            field=models.CharField(choices=[('Blackened Chicken', 'Blackened Chicken'), ('New York Strip', 'New York Strip'), ('Escargot', 'Escargot'), ('Caviar', 'Caviar'), ('Oysters', 'Oysters'), ('Foie Gras', 'Foie Gras'), ('Rocky Mountain Oysters', 'Rocky Mountain Oysters'), ('Creme Brulee', 'Creme Brulee'), ('Wagu Beef', 'Wagu Beef'), ('Baby Back Ribs', 'Baby Back Ribs'), ('Chicken Parmesean', 'Chicken Parmesean'), ('Nigiri', 'Nigiri')], default='BR', max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='movie_selection',
            field=models.CharField(blank=True, choices=[('Batman', 'Batman'), ('Moonfall', 'Moonfall'), ('Interstellar', 'Interstellar'), ('Soul Plane', 'Soul Plane'), ('The Adam Project', 'The Adam Project'), ('Spiderman', 'Spiderman'), ('X', 'X'), ('Screwdriver', 'Screwdriver'), ('Choose or Die', 'Choose or Die'), ('Power Rangers', 'Power Rangers'), ('Knives Out', 'Knives Out'), ('Power Rangers', 'Power Rangers'), ('Suck on That!', 'Suck on That!'), ('My Friend Clifford', 'My Friend Clifford'), ('Dick Wildfreds Unlikely Adventure', 'Dick Wildfreds Unlikely Adventure'), ('Dwight Schrute', 'Dwight Schrute')], max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='background_title',
            field=models.CharField(choices=[('lovepik-beautiful-night-scene-outside-the-plane-window-picture_500078781.jpeg', 'lovepik-beautiful-night-scene-outside-the-plane-window-picture_500078781.jpeg'), ('fuck.jpg', 'fuck.jpg'), ('bitch.png', 'bitch.png')], max_length=100),
        ),
    ]
