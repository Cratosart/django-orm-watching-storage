# Пуль охраны хранилища банка

Пульт охраны хранилища банка, позволяет определить общее количество активных пропусков.
Кто находится в хранилище.
Подозрительно долгое время проведённое в хранилище.

### Как установить

Python3 должен быть уже установлен.

Требуется провести настройку приложения для запуска в файле settings.py расположенного в дерриктории ./project требуется добавить следующие данные

```
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
```

Затем воспользуйтесь 'pip' для установки зависимостей.



```
pip install -r requirements.txt
```
```
py main.py
```



### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).