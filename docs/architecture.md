# Arquitetura

## Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12+ |
| Framework | Django |
| Templates | Django Template Language (DTL) |
| Estilo | TailwindCSS |
| Banco de dados | SQLite (padrão do Django) |
| Autenticação | Sistema nativo do Django, com login por e-mail |
| Views | Class Based Views (`django.views.generic`) |
| Formulários | Django Forms / ModelForms |

As dependências Python do projeto estão em [`requirements.txt`](../requirements.txt), na raiz do repositório.

## Apps Django e responsabilidades

O sistema é dividido em apps independentes, cada uma responsável por um domínio específico:

| App | Responsabilidade |
|---|---|
| `core` | Configurações globais do projeto (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`) e views públicas do site |
| `users` | Model de usuário customizado, autenticação, login, cadastro e logout |
| `profiles` | Perfil complementar do usuário |
| `accounts` | Contas bancárias do usuário |
| `categories` | Categorias de receita/despesa |
| `transactions` | Lançamentos financeiros (entradas e saídas) |

Cada app segue a estrutura padrão gerada pelo `django-admin startapp` (`models.py`, `views.py`, `admin.py`, `apps.py`, `migrations/`, `tests.py`), com a adição de um `signals.py` quando a app precisar de signals (veja [padrões de código](coding-standards.md)).

## Estrutura de pastas

```
finanpy/
├── core/            # configuração do projeto (settings, urls, wsgi, asgi)
├── users/           # app de usuários e autenticação
├── profiles/         # app de perfil
├── accounts/        # app de contas bancárias
├── categories/       # app de categorias
├── transactions/     # app de transações
├── manage.py
├── requirements.txt
├── db.sqlite3
└── docs/            # esta documentação
```

Cada app fica na raiz do projeto (não em uma subpasta `apps/`), e `core` funciona exclusivamente como pasta de configuração do projeto Django — não concentra regras de negócio de domínio.
