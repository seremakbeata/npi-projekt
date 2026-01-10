# DevOps Project - To-Do API

## Autor
Beata Seremak, 54176

## Opis
Prosta aplikacja To-Do API z pełnym pipeline'em CI/CD.

## Instrukcja uruchomienia
```bash
# 1. Sklonuj repozytorium
git clone https://github.com/seremakbeata/npi-projekt.git
cd npi-projekt

# 2. Uruchom z Docker Compose
docker-compose up --build

# 3. Przetestuj API
curl http://localhost:5000/tasks