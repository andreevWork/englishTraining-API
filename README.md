# Backend for englishsusb.ru

## nginx.conf
Конфиг nignx используется для поднятия контейнера в docker-compose

## .env file
Все переменные используются docker-compose для различных контейнеров:

- postgres переменные полностью соответствуют официальному docker image базы https://hub.docker.com/_/postgres/
```
POSTGRES_USER=юзер базы данных 
POSTGRES_PASSWORD=пароль юзера
POSTGRES_DB=название бд
PGDATA=volume для хранения данных бд
```
- nginx сервер для раздачи статики фронтенда
```
FRONTEND_DIR=volume где лежат файлы фронта, после сборки фронт кладет их в данную папку
```
- app переменные для настройки Flask приложения
```
SQLALCHEMY_DATABASE_URI=урл базы формата postgresql://username:password@IP:5432/db_name
ENV=окружение Flask приложения
TESTING=окружение Flask приложения
DEBUG=окружение Flask приложения
SECRET_KEY=необходимо для работы админки, по факту не юзается
BASIC_AUTH_USERNAME=имя для base HTTP авторизации для входа в админку
BASIC_AUTH_PASSWORD=пароль админки
```

