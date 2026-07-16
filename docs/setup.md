# Setup do ambiente local

## Pré-requisitos

- Python 3.12+

## Passos

1. Crie e ative um ambiente virtual na raiz do projeto:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Aplique as migrações do banco de dados (SQLite):

   ```bash
   python manage.py migrate
   ```

4. Rode o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

O projeto ainda não possui variáveis de ambiente ou configuração adicional além do `requirements.txt` — as dependências atuais são apenas Django e suas dependências diretas (`asgiref`, `sqlparse`).

Docker não é utilizado nas fases iniciais do projeto (veja [padrões de código](coding-standards.md)).
