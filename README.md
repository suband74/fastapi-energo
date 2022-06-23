# Приложение подключается к PostgreSQL и Redis и реализует следующие API:

1. Проверка анаграммы - принимает две строки, определяет являются ли они анаграммами.
   Если являются - увеличивает счетчик в Redis. Возвращает JSON
   являются ли они анаграммами и счетчик из Redis.

2. Заносит в базу данных 10 устройств (таблица devices), тип (dev_type) определяется
   случайно из списка: emeter, zigbee, lora, gsm. Поле dev_id - случайные 48 бит в hex-
   формате (MAC-адрес). К пяти устройствам из добавленных привязываются endpoint (таблица endpoints).
   После записи возвращается HTTP код состояния 201.

3. В базе получает список всех устройств, которые не привязаны к
   endpoint. Возвращает количество, сгруппированное по типам устройств.

## Установка проекта на локальный компьютер:

1. Клонировать репозиторий:

```
https://github.com/suband74/fastapi-energo
```

2. Установить docker и docker-compose. Инструкции по установке доступны в официальной документации.

3. В папке с проектом выполнить команду:

```
docker-compose up
```

4. Сервис доступен по адресу:

```
http://127.0.0.1:8000/docs
```
