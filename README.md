# ONNET Website (личный кабинет)
Сайт провайдера связи, с возможностью оставления заявок на подключение. На сайте отображаются: новости, страницы подключения по районам, сетевые устройства на продажу, и т.д

Имеется админ панель для гибкого построения контента на сайте

#### Остальные связанные репозитории:
* [|onnet_cabinet| + |onnet_web|+ |nginx| (Docker)](https://github.com/sita8281/onnet_services)
* [onnet_cabinet](https://github.com/sita8281/onnet_cabinet_demo.git)

#### Backend:
* Flask
* Flask BasicAuth (админка)
* SQLAlchemy, Alembic
* SQLite

#### Frontend:
* JavaScript (jquery)

#### Возможности админ панели
* редактирование страниц
* создание новых страниц
* редактирование списка устройств на продажу
* удаление, добавление картинок
* создание, удаление пользователей админки
* редактирование списка новостей
* просмотр заявок на подключение
* и т.д


## Установка и запуск
клонируем
```
git clone https://github.com/sita8281/onnet_cabinet_demo.git
```

собираем Docker-image
```
sudo docker build -t onnet_web:v1 <путь к проекту>
```

запуск (interactive)
```
sudo docker run -it -p 80:8000 onnet_web:v1
```

## Demo






