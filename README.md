# Naruto_db

![alt text](https://static.wikia.nocookie.net/voiceacting/images/d/d0/Naruto_Shippuden_new.JPG/revision/latest/scale-to-width-down/1200?cb=20211031034133)

To deploy - from the root folder:

```
docker-compose up -d --build
```

### Tables

* Hero: id, side (Шиноби/Акацуки), name, birthday
* Moto: id, hero_id, moto_id (number for hero starting with 1), moto
* Fight: id, hero_1_id, hero_1_moto_id, hero_2_id, hero_2_moto_id, winner (0, 1, 2)
* Story: id, hero_id, story

### Examples for running scripts

To add a hero 

```
python add_hero.py --name "Сасуке" --side "Акацуки" --birthday "1001-12-11"
```

To add a moto

```
python add_moto.py --name 'Наруто' --moto 'НИКОГДА НЕ СДАВАТЬСЯ'
```

To add a random fight

```
python add_fight.py
```

To delete a hero 

```
python delete_hero.py --name 'Сасуке'
```

To add a story


```
python add_story.py --name 'Наруто' --story 'Преподаватель в академии ниндзя'
```

### Logging: file.log is for info (with logging filter on fights with winner 0), errors printed out on the console.

