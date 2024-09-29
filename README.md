<div align="center">
    <a href="https://t.me/RutubeFAQ_bot">
        <img src="https://raw.githubusercontent.com/Y1OV/project_lab/refs/heads/main/data/Logo_RUTUBE_dark_color.png" alt="Foo" style="width: 50%; height: auto;">
    </a>
    <H2 align="center">Команда Ikanam</H2> 
    <H2 align="center">Интеллектуальный помощник оператора службы поддержки"</H2> 
</div align="center">

💬 Мы разработали интеллектуальный сервис-помощник оператора службы поддержки с интеграцией в телеграм-бот. Сервис увеличит лояльность аудитории, сэкономит силы операторов и ресурсы компании, создав ещё один задел для роста аудитории.

⚙️ Как это работает? Пользователь через бота задаёт вопрос к локально развернутой LLM-модели, которая предварительно «дообучена» на базе данных вопросов-ответов, релевантной для Rutube, а модель уже генерирует ответ.

## `Технологии`

- **NLP pipeline**: multilingual-e5-base, Llama-3.1-8B-Instruct,
- **База данных и хранение**: Postgres, FAISS
- **Деплой**: Docker, FastAPI


## `Использование`

*1. Загрузите репозиторий на свой компьютер и откройте её в вашей предпочитаемой среде разработки (IDE).* 
```
git clone https://github.com/Danessely/rutube-qa-rag.git
```
*2. Положите файл с базой вопросов в search_engine/init_data ([пример](https://drive.google.com/file/d/1lPpzDEfPvKgKKfGNqKZRB_i-yUx-7M0P/view?usp=sharing)):* 

*3. Создайте `.env` файл в корневой директории по следующему примеру:*
```
# ---- SEARCH_ENGINE/PSQL ----
SEARCH_ENGINE_PORT=5041
DB_NAME=db_name
DB_USER=user
DB_PASSWORD=pass
EMBEDDER_URL=http://search_embedder:5043
NEURAL_URL=http://neural_worker:7860
DB_HOST=postgres
DB_PORT=5044

# ---- EMBEDDER ----
EMBEDDER_PORT=5043
NVIDIA_VISIBLE_DEVICES_EMB=0
TRANSFORMERS_CACHE_EMB=/cache/

# ---- NEURAL_WORKER ----
HF_TOKEN=...
WORKER_PORT=7860
NVIDIA_VISIBLE_DEVICES_LLM=0
TRANSFORMERS_CACHE_LLM=/cache/

# ---- STREAMLIT ----
SE_HOST=search_engine
SE_PORT=5041
``` 
*4. Соберите и запустите контейнеры (создание базы индексов может занять несколько минут).*
```
sudo docker-compose build
sudo docker-compose up
```
*5. Поздравляем! (API эндпоинты можно посмотреть на `http://localhost:5041/docs`.*

## `Ссылки`

Наш [Telegram-бот](https://t.me/RutubeFAQ_bot)

[Screencast](https://drive.google.com/drive/folders/1zeSSYbP7UjPTKG6UYtQt0sv_R3EVceIw?dmr=1&ec=wgc-drive-globalnav-goto) наших сервисов

## `Пример работы TG-бота`

### Видео

https://github.com/user-attachments/assets/508ab99e-198a-4539-9e04-d1be4f063c83

### Фото

<p align="center">
    <img src="https://raw.githubusercontent.com/Y1OV/project_lab/refs/heads/main/data/1p.jpg" alt="1" width="500" style="display: inline-block; vertical-align: middle; margin-right: 10px;"/>  <br/>
</p>


<p align="center">
    <img src="https://raw.githubusercontent.com/Y1OV/project_lab/refs/heads/main/data/2p.jpg" alt="2" width="500" style="display: inline-block; vertical-align: middle; margin-right: 10px;"/>  <br/>
</p>

© ikanam
