# Куда пойти

Проект представляет собой сайт, на котром можно посмотреть куда сходить. Просмотреть достопримечательности и их описание.

## Как запустить

Чтобы запустить проект должен быть установлен python 3.10.

Необходимо создать файл `env` куда поместить следующую информацию:

```
SECRET_KEY='<Ваш секретный ключ проекта Django>'
DEBUG=<Режим отладки>
ALLOWED_HOSTS=<Используемный адрес хоста>
```

Далее нужно установить необходимые зависимости командой

```
pip install -r requriments.txt
```

Командной `python3 manage.py runserver` можно запустить сайт.

## Как наполнить сайт контентом

Чтобы попасть в админ панель, где можно добавлять достопримечательности, необходимо создать суперпользователя `pyton3 manage.py createsuperuser `и перейти по ссылке

`http://<ip:порт>/admin/`

Где можно сорздать новую достопримечательность:

![1729525013543](.gitbook\assets\1729525013543.png "Пример заполненого места")