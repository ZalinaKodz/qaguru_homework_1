### 📦 `qa_homework_1`

Учебный проект для  QA Guru
---

### 🔧 Стек технологий

* Python 3.10+
* [FastAPI](https://fastapi.tiangolo.com/)
* [Pytest](https://docs.pytest.org/)
* [Requests](https://requests.readthedocs.io/)
* Uvicorn

---

### 📁 Структура проекта

```
.
├── main.py               # FastAPI-сервис (имитация https://reqres.in)
├── test_requests.py      # Набор автотестов
├── test_user.py          # Данные для создания пользователя
└── README.md             # Документация проекта
```

---

### 🚀 Как запустить

#### 1. Клонировать репозиторий

```bash
git clone https://github.com/Andreyshabalinn/python-fast-api-tests.git
cd python-fast-api-tests
```

#### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

#### 3. Запустить FastAPI-сервер

```bash
uvicorn main:app --reload
```

Основной URL: [http://127.0.0.1:8000](http://localhost:8000/api)

#### 4. Запустить тесты

В новом терминале (не останавливая сервер):

```bash
pytest test_requests.py
```

---

### ✅ Что покрыто в тестах

* Проверка корректного ответа для существующего пользователя
* Проверка, что при передаче нечислового user_id возвращается ошибка валидации
* Проверка несуществующего пользователя
* Проверка, что у пользователя в ответе есть все необходимые поля.
