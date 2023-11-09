# Карта куда пойти в Москве

Сервис по просмотру мест на карте, с фото и подробным описанием. Также имеется возможность 
добавления своих мест через админ-панель.  
Фронтенд взят [здесь](https://github.com/devmanorg/where-to-go-frontend/).

## Установка

```commandline
git clone https://github.com/Weffy61/place_map.git
```

## Установка зависимостей

Переход в директорию с исполняемым файлом и установка

```commandline
cd place_map
```

Установка

Python 3.10 должен быть уже установлен. Далее используйте pip(or pip3, если имеется конфликт с Python2) 
для установки зависомостей:

```commandline
pip install -r requirements.txt
```

## Создание и настройка .env

Создайте в корне папки `place_map` файл `.env`. Откройте его для редактирования любым текстовым редактором и запишите 
туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступны следующие переменные:
- SECRET_KEY - секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- DEBUG - дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- STATIC_URL - по умолчанию это `/static/`. [Что такое STATIC_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_URL).
- MEDIA_URL - по умолчанию это `/media/`. [Что такое MEDIA_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_URL).
- ALLOWED_HOSTS - см. [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).


## Подготовка к запуску

1. Переходим, в директорию с `manage.py`, если еще не в ней.

2. Создаем миграции

```commandline
python manage.py makemigrations
```

3. Применяем миграции

```commandline
python manage.py migrate
```

4. Создаём суперпользователя

```commandline
python manage.py createsuperuser
```

## Запуск


```commandline
python manage.py runserver
```

Перейдите по адресу http://127.0.0.1:8000/admin/ и введите данные для авторизации, которые вы указали ранее.  
Сам сайт будет запущен по адресу http://127.0.0.1:8000.


### Добавление новых локаций

Для добавления новой локации необходим URL адрес JSON файла.

Пример загрузки новой локации:
```commandline
 python manage.py load_place https://url.json
```

Пример JSON:

```json
{
  "title": "Экскурсионная компания «Легенды Москвы»",
  "imgs": [
    "/media/images/0a79676b3d5e3b394717b4bf2e610a57_tQpfGA8.jpg",
    "/media/images/1e27f507cb72e76b604adbe5e7b5f315_VhYO2Ul.jpg",
    "/media/images/4f793576c79c1cbe68b73800ae06f06f_5cqg9TD.jpg",
    "/media/images/7a7631bab8af3e340993a6fb1ded3e73_HkTmqJ9.jpg"
  ],
  "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
  "description_long": "<p>Экскурсия от компании &laquo;Легенды Москвы&raquo; &mdash; простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы &mdash; классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p>\r\n<p>Компания &laquo;Легенды Москвы&raquo; сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе &mdash; это делает посадку организованной и понятной.</p>\r\n<p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p>\r\n<p>Подробности узнавайте <a class=\"\\&quot;external-link\\&quot;\" href=\"\\&quot;https:/moscowlegends.ru\" target=\"\\&quot;_blank\\&quot;\">на сайте</a>. За обновлениями удобно следить <a class=\"\\&quot;external-link\\&quot;\" href=\"\\&quot;https:/vk.com/legends_of_moscow\" target=\"\\&quot;_blank\\&quot;\">&laquo;ВКонтакте&raquo;</a>, <a class=\"\\&quot;external-link\\&quot;\" href=\"\\&quot;https:/www.facebook.com/legendsofmoscow?ref=bookmarks\" target=\"\\&quot;_blank\\&quot;\">в Facebook</a>.</p>",
  "coordinates": {
    "lng": 37.64912239999976,
    "lat": 55.77754550000014
  }
}
```

#### Обзорная версия сайта расположена по [данному url](https://weffy.pythonanywhere.com/)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).