1. Запустить docker:
```docker-compose up```
2. Установка зависимостей:
```pip install -r requirements.txt```
3. Миграции:
```
alembic revision --autogenerate -m 'start1'
alembic upgrade head
```
4. Запуск сервера:
```python ./main.py```
5. Запуск тестов:
```python ./load_tester/tester.py```
