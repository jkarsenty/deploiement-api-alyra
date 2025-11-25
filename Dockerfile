# image de base
FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml .

# COPY uv.lock ./

COPY . .

# installation des dépendances dans un environnement gérer par uv
RUN uv sync --no-dev

# Variable d'env Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

# on utilise uv pour lancer l'application flask dans l'environnement géré par uv
CMD ["uv", "run", "flask", "run"]

