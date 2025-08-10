# 🎼 Maestro

Sistema web para orquestrar, executar e agendar scripts Python de forma assíncrona. Com Django, Celery e Django REST Framework, o Maestro permite que você conduza seus scripts como uma verdadeira sinfonia.

---

## 🚀 Funcionalidades

- 🎹 Cadastro de scripts com nome, caminho e descrição  
- 🥁 Execução assíncrona de scripts via Celery  
- 🎺 Registro detalhado de logs de execução (stdout, stderr, código de retorno)  
- 🎷 Agendamento de scripts com crontab usando Django Celery Beat  
- 🎧 API REST para integração com outros sistemas  

---

## 🛠️ Tecnologias

| Tecnologia             | Finalidade                          |
|------------------------|-------------------------------------|
| Django                 | Backend e ORM                       |
| Django REST Framework  | API REST                            |
| Celery                 | Execução assíncrona de tarefas      |
| Redis                  | Broker para Celery                  |
| Django Celery Beat     | Agendamento de tarefas periódicas   |
| SQLite                 | Banco de dados                      |

---

## 📦 Instalação

```bash
git clone https://github.com/pedro-meinen/maestro.git
cd maestro

python -m venv .venv
source .venv/bin/activate  # ou venv\Scripts\activate no Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver
```

---

## ⚙️ Execução do Celery

```bash
celery -A maestro worker --loglevel=info
celery -A maestro beat --loglevel=info
```

---

## 🔌 Endpoints da API

| Método | Endpoint                  | Descrição                        |
|--------|---------------------------|----------------------------------|
| GET    | `/scripts/`               | Lista todos os scripts           |
| POST   | `/scripts/`               | Cria um novo script              |
| POST   | `/scripts/{id}/execute/`  | Executa o script                 |
| POST   | `/scripts/{id}/schedule/` | Agenda execução via crontab      |
| GET    | `/logs/`                  | Lista logs de execução           |

---

## 📌 Exemplo de agendamento

```json
POST /scripts/5/schedule/

{
  "cron": {
    "minute": "0",
    "hour": "12",
    "day_of_week": "*",
    "day_of_month": "*",
    "month_of_year": "*"
  }
}
```

---

## 🤝 Contribuição

Contribuições são super bem-vindas! Para colaborar com o Maestro:

1. Faça um fork do repositório  
2. Crie uma branch com sua feature ou correção (`git checkout -b minha-feature`)  
3. Faça commits claros e objetivos  
4. Envie um pull request explicando suas mudanças  

Sinta-se à vontade para abrir issues com sugestões, bugs ou ideias de melhoria. Vamos compor juntos uma ferramenta ainda mais poderosa! 🎶

---

## 📬 Contato

Tem dúvidas, sugestões ou quer bater um papo sobre o projeto?

- 📧 Email: `pedromeinen99@gmail.com`  
- 🐙 GitHub: [pedro-meinen](https://github.com/pedro-meinen)  
- 💼 LinkedIn: [linkedin.com/in/pedro-henrique-souza-meinen](https://linkedin.com/in/pedro-henrique-souza-meinen)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
