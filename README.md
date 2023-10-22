## Инструкция по запуску:

Клонировать репозиторий:

```
git@github.com:SaInekK/build_service.git`
```

Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```

Установить зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Запустить:
```
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Запуск тестов:
```
pytest
```


### Пример запроса:
POST: http://127.0.0.1:8000/get_tasks 
```
{
    "build": "{build_name}"
}
```
RESPONSE:
```
[
    "task_1",
    "task_2",
    "task_3",
    "task_4",
    "task_5"
]
```