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

3. Copie o arquivo de variáveis de ambiente e ajuste os valores se necessário:

   ```bash
   cp .env.example .env
   ```

4. Aplique as migrações do banco de dados (SQLite):

   ```bash
   python manage.py migrate
   ```

5. Rode o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

## Variáveis de ambiente

Configuração sensível do `core/settings.py` é lida do arquivo `.env` (na raiz do projeto, não versionado) via `django-environ`. O `.env.example` documenta as variáveis esperadas:

| Variável | Descrição | Exemplo |
|---|---|---|
| `SECRET_KEY` | Chave secreta do Django (nunca reutilize a de produção localmente) | `django-insecure-...` |
| `DEBUG` | Liga/desliga o modo debug | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos, separados por vírgula | `localhost,127.0.0.1` |

Nunca commite o arquivo `.env` — ele já está no `.gitignore`. Ao adicionar uma nova variável de configuração, atualize também o `.env.example`.

Docker não é utilizado nas fases iniciais do projeto (veja [padrões de código](coding-standards.md)).
