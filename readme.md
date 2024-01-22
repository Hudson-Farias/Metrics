# TT-Metrics - Análise de Métricas MRR e Churn Rate

O TT-Metrics é uma aplicação fullstack desenvolvida para a análise de métricas MRR (Monthly Recurring Revenue) e Churn Rate. Este projeto é dividido em duas partes principais: o frontend, construído em Vue.js, e o backend, implementado com FastAPI. As pastas frontend e backend contêm os respectivos códigos fonte.


## Stack utilizada

**Backend:** FastAPI, Pandas

**Frontend:** VueJS, TailwindCSS, ChartJS


## Pré-requisitos

**Docker** ou **ASDF**
## Rodando

Clone o projeto

```bash
  git clone https://github.com/Hudson-Farias/TT-Metrics.git
```

Entre no diretório do projeto 

```bash
  cd TT-Metrics
```

Gere o frontend/.env  

```bash
  cp frontend/.env.example frontend/.env
```

## Com Docker

```bash
  docker-compose up --build
```

## Com ASDF

Instale as versões especificadas

```bash
  asdf install
```

Inicie o Backend e o Frontend

```bash
  cd backend
  python -m venv venv
  source ./venv/bin/activate ## ou .\venv\Scripts\Activate
  pip install -r requirements.txt
  uvicorn main:app --reload
```
O backend estará acessível em http://localhost:8000 e https://tt-metrics.onrender.com.

```bash
  cd ../frontend
  yarn install
  npm run serve
```
O frontend estará disponível em http://localhost:8080 e https://tt-metrics.vercel.app.