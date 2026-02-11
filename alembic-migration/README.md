# Run locally

(Повинна бути піднята бд за адресою: postgresql://postgres:secret@localhost:5432/mydb)

```bash
python3 -m venv env
source  env/bin/activate
pip3 install -r requirements.txt
```

Запуск міграції:
```bash
alembic upgrade head
```

