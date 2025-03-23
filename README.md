### Полный гайд с настройкой модуля и ссылками где купить и тд.
https://substantial-bobcat-e62.notion.site/Raspberry-sms-receiver-1bc792b9874f8069b86aec83446d2496



Файл .env для настройки фастапи и сокета

Предварительно проверь через какой сокет подключен модуль.
В моем случае `/dev/ttyAMA0`

### Установка
```bash
uv venv
uv pip install -r pyproject.toml
uv run python -m src.main
```


### Запуск
```bash
uv run python -m src.main
```
