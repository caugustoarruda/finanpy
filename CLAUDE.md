# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Finanpy is a personal finance management web app: Python + Django, server-rendered with Django Template Language (DTL) and styled with TailwindCSS. Full-stack Django only — no separate API, no decoupled/SPA frontend. SQLite is the only database. Authentication is Django's native auth, customized for email-based login.

The project is in its initial setup phase: the `core` project and five domain apps (`users`, `profiles`, `accounts`, `categories`, `transactions`) exist and are registered in `INSTALLED_APPS`, but none have models, views, forms, or templates implemented yet. See [PRD.md](PRD.md) for the full requirements, sprint roadmap, data model, and design system spec, and [docs/README.md](docs/README.md) for the documentation index (architecture, coding standards, design system, setup).

## Commands

```bash
# activate the virtualenv (already created at .venv)
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# create migrations after model changes
python manage.py makemigrations

# run the dev server
python manage.py runserver

# create a superuser
python manage.py createsuperuser

# run tests (all, or a single app / test case / test method)
python manage.py test
python manage.py test accounts
python manage.py test accounts.tests.SomeTestCase
python manage.py test accounts.tests.SomeTestCase.test_something
```

There is no build step and no linter/formatter configured — just PEP8 by convention (see below). Docker and automated tests are explicitly out of scope until the final sprints (see PRD §7, §13).

## Architecture

**Apps are split by domain, one responsibility each** (not by layer). `core` is configuration-only (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`) plus public views (landing page) — it must not hold domain business logic.

| App | Responsibility |
|---|---|
| `core` | Project settings/urls, public/landing views |
| `users` | Custom `User` model (`AbstractUser`, email as `USERNAME_FIELD`), signup, login, logout |
| `profiles` | One-to-one profile complementing `User` |
| `accounts` | User's bank accounts |
| `categories` | Income/expense categories |
| `transactions` | Financial transactions, linked to an `Account` and a `Category` |

Domain relations (see PRD §8.3 for full field list): `User` 1—1 `Profile`, `User` 1—N `Account`/`Category`/`Transaction`, `Transaction` N—1 `Account`, `Transaction` N—1 `Category`.

Every domain model must inherit from an abstract `TimeStampedModel` (`created_at`/`updated_at`) — this base model belongs in `core`. Every domain model (`Account`, `Category`, `Transaction`, `Profile`) has a `ForeignKey`/`OneToOneField` to `User`.

## Conventions

- **Language split**: all code (variables, functions, classes, comments) is in English; all user-facing UI text is in Brazilian Portuguese.
- **PEP8**, single quotes preferred over double quotes.
- **Class Based Views** and native Django generics (`django.views.generic`) are preferred over function-based views. Protected views use `LoginRequiredMixin`, and any queryset (list/update/delete) must be filtered by `request.user` — never expose another user's data.
- **Signals** live in a `signals.py` inside the owning app and are wired up in that app's `apps.py` `ready()` method (e.g. auto-creating a `Profile` on `User` post_save).
- Templates follow a shared-base pattern once implemented: `templates/base.html` (+ `base_public.html`/`base_app.html`), `templates/partials/` for reusable includes (`_navbar.html`, `_sidebar.html`, `_messages.html`, `_footer.html`), and each app owns `templates/<app_name>/` with `list.html`/`form.html`/`detail.html`/`confirm_delete.html`. See [docs/design-system.md](docs/design-system.md) for the Tailwind color palette, typography, and component markup to reuse (buttons, inputs, cards, sidebar).
- Scope discipline: don't add functionality beyond what's in PRD.md — new features require updating the PRD first.
