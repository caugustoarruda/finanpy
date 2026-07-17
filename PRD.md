# PRD — Finanpy
### Product Requirement Document

---

## 1. Visão geral

**Finanpy** é um sistema web de gestão de finanças pessoais, desenvolvido em **Python + Django**, com frontend renderizado via **Django Template Language (DTL)** estilizado com **TailwindCSS**. O projeto segue uma abordagem enxuta, sem over engineering: banco de dados **SQLite**, autenticação **nativa do Django** (login por e-mail) e separação de domínios em **apps Django independentes**.

O objetivo é entregar uma ferramenta simples e funcional para que uma pessoa registre contas bancárias, categorize seus lançamentos financeiros e acompanhe entradas e saídas em um dashboard central.

---

## 2. Sobre o produto

Finanpy permite que o usuário:

- Crie uma conta e faça login usando e-mail e senha.
- Cadastre um perfil pessoal.
- Cadastre uma ou mais contas bancárias (carteira, conta corrente, poupança, etc).
- Cadastre categorias de receita e despesa, personalizadas.
- Registre transações (entradas e saídas) vinculadas a uma conta e a uma categoria.
- Visualize um dashboard com o resumo da sua situação financeira.

O sistema é **full stack Django**, sem API separada e sem frontend desacoplado (SPA). Toda a renderização é feita no servidor, com Tailwind aplicado diretamente nos templates.

---

## 3. Propósito

Oferecer uma solução simples, rápida de usar e visualmente moderna para que pessoas físicas organizem sua vida financeira, sem a complexidade de planilhas ou de sistemas financeiros corporativos.

---

## 4. Público alvo

- Pessoas físicas que desejam controlar receitas e despesas pessoais.
- Usuários que buscam uma alternativa simples a planilhas de controle financeiro.
- Usuários que preferem um sistema web leve, sem necessidade de instalar aplicativos.

---

## 5. Objetivos

- Permitir o cadastro e autenticação de usuários via e-mail.
- Permitir o gerenciamento de contas bancárias.
- Permitir o gerenciamento de categorias de transações.
- Permitir o registro e acompanhamento de transações financeiras.
- Exibir um dashboard consolidado com a situação financeira do usuário.
- Manter uma identidade visual única, moderna e consistente em todas as telas.
- Manter a base de código simples, legível e alinhada à PEP8.

---

## 6. Requisitos funcionais

### 6.1 Site público (landing page)

- RF01: Deve existir uma página inicial pública, acessível sem autenticação.
- RF02: A página inicial deve apresentar o produto (hero, benefícios, chamada para ação).
- RF03: A página inicial deve conter botões de **Cadastre-se** e **Login**.

### 6.2 Autenticação e usuários

- RF04: O usuário deve poder se cadastrar informando nome, e-mail e senha.
- RF05: O login deve ser feito através do e-mail (não do username).
- RF06: O usuário deve poder fazer logout.
- RF07: Após o login, o usuário deve ser redirecionado ao dashboard.
- RF08: Rotas internas do sistema devem exigir autenticação (redirecionar ao login se não autenticado).

### 6.3 Perfil

- RF09: O usuário deve poder visualizar e editar seu perfil (dados complementares ao usuário).

### 6.4 Contas bancárias

- RF10: O usuário deve poder cadastrar uma conta bancária (nome, tipo, saldo inicial).
- RF11: O usuário deve poder listar suas contas bancárias.
- RF12: O usuário deve poder editar uma conta bancária.
- RF13: O usuário deve poder excluir uma conta bancária.

### 6.5 Categorias

- RF14: O usuário deve poder cadastrar categorias de receita ou despesa.
- RF15: O usuário deve poder listar suas categorias.
- RF16: O usuário deve poder editar uma categoria.
- RF17: O usuário deve poder excluir uma categoria.

### 6.6 Transações

- RF18: O usuário deve poder registrar uma transação (valor, tipo, data, descrição, conta, categoria).
- RF19: O usuário deve poder listar suas transações, com filtros básicos (conta, categoria, tipo, período).
- RF20: O usuário deve poder editar uma transação.
- RF21: O usuário deve poder excluir uma transação.

### 6.7 Dashboard

- RF22: O dashboard deve exibir o saldo total consolidado das contas do usuário.
- RF23: O dashboard deve exibir o total de receitas e despesas do período.
- RF24: O dashboard deve exibir as últimas transações registradas.

### 6.8 Fluxograma de UX

```mermaid
flowchart TD
    A[Landing Page] --> B{Usuário autenticado?}
    B -- Não --> C[Cadastre-se]
    B -- Não --> D[Login]
    C --> E[Formulário de cadastro]
    E --> F[Conta criada]
    F --> D
    D --> G[Formulário de login com e-mail]
    G --> H{Credenciais válidas?}
    H -- Não --> G
    H -- Sim --> I[Dashboard]
    B -- Sim --> I[Dashboard]

    I --> J[Menu principal]
    J --> K[Contas Bancárias]
    J --> L[Categorias]
    J --> M[Transações]
    J --> N[Perfil]
    J --> O[Logout]

    K --> K1[Listar contas]
    K1 --> K2[Criar conta]
    K1 --> K3[Editar conta]
    K1 --> K4[Excluir conta]

    L --> L1[Listar categorias]
    L1 --> L2[Criar categoria]
    L1 --> L3[Editar categoria]
    L1 --> L4[Excluir categoria]

    M --> M1[Listar transações]
    M1 --> M2[Criar transação]
    M1 --> M3[Editar transação]
    M1 --> M4[Excluir transação]

    N --> N1[Visualizar perfil]
    N1 --> N2[Editar perfil]

    O --> A
```

---

## 7. Requisitos não-funcionais

- RNF01: O sistema deve utilizar Django full stack, sem frontend desacoplado.
- RNF02: O frontend deve ser construído com Django Template Language e TailwindCSS.
- RNF03: O sistema deve utilizar exclusivamente o banco de dados SQLite padrão do Django.
- RNF04: Todo model do sistema deve possuir os campos `created_at` e `updated_at`.
- RNF05: O código deve ser escrito em inglês (nomes de variáveis, funções, classes, comentários).
- RNF06: Toda informação exibida na interface deve estar em português brasileiro.
- RNF07: O código deve seguir a PEP8 e utilizar aspas simples sempre que possível.
- RNF08: O sistema deve priorizar Class Based Views e recursos nativos do Django.
- RNF09: Signals, quando utilizados, devem ficar em um arquivo `signals.py` dentro da app correspondente.
- RNF10: As entidades do sistema devem ser separadas em apps Django isoladas por responsabilidade.
- RNF11: O sistema deve ser responsivo (mobile, tablet, desktop).
- RNF12: Docker não deve ser implementado nas fases iniciais (reservado para sprint final).
- RNF13: Testes automatizados não devem ser implementados nas fases iniciais (reservado para sprint final).
- RNF14: O sistema não deve conter funcionalidades além das explicitamente solicitadas neste documento.
- RNF15: Segredos e configuração sensível (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) devem ser lidos de variáveis de ambiente via arquivo `.env` (não versionado), nunca hardcoded no código-fonte.

---

## 8. Arquitetura técnica

### 8.1 Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12+ |
| Framework | Django (última versão estável) |
| Templates | Django Template Language (DTL) |
| Estilo | TailwindCSS |
| Banco de dados | SQLite (padrão do Django) |
| Autenticação | Sistema nativo do Django (`AbstractUser` customizado, login por e-mail) |
| Views | Class Based Views (`django.views.generic`) |
| Formulários | Django Forms / ModelForms |

### 8.2 Apps Django e responsabilidades

| App | Responsabilidade |
|---|---|
| `core` | Configurações globais do projeto (settings, urls, wsgi, asgi) e views públicas (landing page) |
| `users` | Model de usuário customizado (herdando `AbstractUser`), autenticação, login, cadastro e logout |
| `profiles` | Perfil complementar do usuário |
| `accounts` | Contas bancárias do usuário |
| `categories` | Categorias de receita/despesa |
| `transactions` | Lançamentos financeiros (entradas e saídas) |

### 8.3 Modelo de dados

```mermaid
erDiagram
    USER ||--o| PROFILE : possui
    USER ||--o{ ACCOUNT : possui
    USER ||--o{ CATEGORY : possui
    USER ||--o{ TRANSACTION : possui
    ACCOUNT ||--o{ TRANSACTION : origina
    CATEGORY ||--o{ TRANSACTION : classifica

    USER {
        int id PK
        string email
        string first_name
        string last_name
        string password
        boolean is_active
        boolean is_staff
        datetime created_at
        datetime updated_at
    }

    PROFILE {
        int id PK
        int user_id FK
        string phone
        date birth_date
        string avatar
        datetime created_at
        datetime updated_at
    }

    ACCOUNT {
        int id PK
        int user_id FK
        string name
        string account_type
        decimal initial_balance
        datetime created_at
        datetime updated_at
    }

    CATEGORY {
        int id PK
        int user_id FK
        string name
        string category_type
        string color
        datetime created_at
        datetime updated_at
    }

    TRANSACTION {
        int id PK
        int user_id FK
        int account_id FK
        int category_id FK
        string description
        decimal amount
        string transaction_type
        date transaction_date
        datetime created_at
        datetime updated_at
    }
```

### 8.4 Regras técnicas gerais

- O model `User` (app `users`) substitui o `User` padrão do Django via `AUTH_USER_MODEL`, com `USERNAME_FIELD = 'email'`.
- Um `manager` customizado (`UserManager`) é necessário para criação de usuários e superusuários via e-mail.
- Todos os models de domínio (`Account`, `Category`, `Transaction`, `Profile`) devem possuir um `ForeignKey`/`OneToOneField` para `User`.
- Um `abstract base model` (`TimeStampedModel`) pode ser criado em `core` para centralizar os campos `created_at` e `updated_at`, evitando repetição.
- Configuração sensível do `core/settings.py` (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) é lida de variáveis de ambiente via `django-environ`, a partir de um arquivo `.env` na raiz do projeto (não versionado — apenas `.env.example` é commitado como referência).

---

## 9. Design system

Identidade visual moderna, com gradientes suaves, paleta harmônica e fundo claro (não totalmente branco). Todos os componentes abaixo devem ser reutilizados em todas as telas do sistema, preferencialmente via templates base e `{% include %}`/`{% block %}` do Django.

### 9.1 Paleta de cores

| Uso | Classe Tailwind | Cor |
|---|---|---|
| Fundo geral da aplicação | `bg-slate-100` | Cinza claro azulado |
| Fundo de cards/painéis | `bg-white` | Branco |
| Gradiente primário (botões, header, destaques) | `bg-gradient-to-r from-indigo-600 to-purple-600` | Índigo → Roxo |
| Gradiente hover | `hover:from-indigo-700 hover:to-purple-700` | Índigo escuro → Roxo escuro |
| Texto principal | `text-slate-800` | Cinza escuro |
| Texto secundário | `text-slate-500` | Cinza médio |
| Sucesso / Receita | `text-emerald-600` / `bg-emerald-50` | Verde esmeralda |
| Erro / Despesa | `text-rose-600` / `bg-rose-50` | Vermelho rosado |
| Alerta | `text-amber-600` / `bg-amber-50` | Âmbar |
| Bordas | `border-slate-200` | Cinza claro |

### 9.2 Tipografia

- Fonte padrão: `font-sans` (stack padrão do Tailwind, ex: Inter/system-ui).
- Títulos de página: `text-2xl md:text-3xl font-bold text-slate-800`.
- Subtítulos de seção: `text-lg font-semibold text-slate-700`.
- Texto corrido: `text-sm text-slate-600`.
- Labels de formulário: `text-sm font-medium text-slate-700`.

### 9.3 Botões

**Botão primário (ação principal):**
```html
<button class="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white font-medium px-4 py-2 rounded-lg shadow-sm transition-colors duration-200">
  Salvar
</button>
```

**Botão secundário:**
```html
<button class="bg-white border border-slate-300 text-slate-700 hover:bg-slate-50 font-medium px-4 py-2 rounded-lg transition-colors duration-200">
  Cancelar
</button>
```

**Botão de perigo (exclusão):**
```html
<button class="bg-rose-600 hover:bg-rose-700 text-white font-medium px-4 py-2 rounded-lg transition-colors duration-200">
  Excluir
</button>
```

### 9.4 Inputs e formulários

```html
<div class="mb-4">
  <label class="block text-sm font-medium text-slate-700 mb-1">Nome</label>
  <input type="text" class="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent">
</div>
```

- Inputs sempre com `rounded-lg`, `border-slate-300` e `focus:ring-2 focus:ring-indigo-500`.
- Mensagens de erro: `text-rose-600 text-xs mt-1`.
- Formulários organizados em `<form>` com `space-y-4`.

### 9.5 Cards / Painéis

```html
<div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
  <!-- conteúdo -->
</div>
```

### 9.6 Grid e layout

- Container principal: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`.
- Grid de cards de resumo (dashboard): `grid grid-cols-1 md:grid-cols-3 gap-4`.
- Grid de listagens: `grid grid-cols-1 gap-4` com cards empilhados ou tabela responsiva.

### 9.7 Menu / navegação

**Sidebar (área autenticada), fixa em desktop e colapsável/off-canvas em mobile:**
```html
<aside class="w-64 bg-white border-r border-slate-200 min-h-screen">
  <div class="p-6 bg-gradient-to-r from-indigo-600 to-purple-600">
    <span class="text-white text-xl font-bold">Finanpy</span>
  </div>
  <nav class="p-4 space-y-1">
    <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">Dashboard</a>
    <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">Contas</a>
    <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">Categorias</a>
    <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">Transações</a>
    <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">Perfil</a>
  </nav>
</aside>
```

- Item de menu ativo: adicionar `bg-indigo-50 text-indigo-700 font-medium`.
- Header público (landing page): `bg-white/80 backdrop-blur border-b border-slate-200` fixo no topo.

### 9.8 Padrão de templates Django

- `templates/base.html`: layout base com Tailwind (via CDN ou build), blocos `{% block content %}`, `{% block title %}`.
- `templates/partials/`: componentes reutilizáveis (`_navbar.html`, `_sidebar.html`, `_messages.html`, `_footer.html`).
- Cada app possui sua pasta `templates/<app_name>/` com suas próprias views (`list.html`, `form.html`, `detail.html`, `confirm_delete.html`).
- Mensagens do Django (`django.contrib.messages`) exibidas como toasts/alerts com cores semânticas (verde para sucesso, vermelho para erro).

---

## 10. User stories

### Épico 1 — Autenticação e usuários

**US01:** Como visitante, quero me cadastrar informando nome, e-mail e senha, para criar minha conta no Finanpy.
- Critérios de aceite:
  - O formulário de cadastro exige nome, e-mail e senha (com confirmação).
  - O e-mail deve ser único no sistema.
  - Após o cadastro, o usuário é redirecionado para a tela de login.

**US02:** Como usuário cadastrado, quero fazer login usando meu e-mail e senha, para acessar o sistema.
- Critérios de aceite:
  - O campo de login é o e-mail, não o username.
  - Credenciais inválidas exibem mensagem de erro.
  - Login bem-sucedido redireciona para o dashboard.

**US03:** Como usuário autenticado, quero fazer logout, para encerrar minha sessão com segurança.
- Critérios de aceite:
  - Ao clicar em "Sair", a sessão é encerrada.
  - O usuário é redirecionado para a landing page.

### Épico 2 — Perfil

**US04:** Como usuário autenticado, quero visualizar e editar meu perfil, para manter meus dados atualizados.
- Critérios de aceite:
  - A tela de perfil exibe telefone, data de nascimento e avatar (quando cadastrados).
  - As alterações são salvas e uma mensagem de sucesso é exibida.

### Épico 3 — Contas bancárias

**US05:** Como usuário autenticado, quero cadastrar uma conta bancária, para organizar meu dinheiro por origem.
- Critérios de aceite:
  - O formulário exige nome, tipo e saldo inicial.
  - A conta criada aparece na listagem do usuário.

**US06:** Como usuário autenticado, quero listar, editar e excluir minhas contas bancárias, para mantê-las atualizadas.
- Critérios de aceite:
  - A listagem exibe apenas as contas do usuário logado.
  - A exclusão exige confirmação.

### Épico 4 — Categorias

**US07:** Como usuário autenticado, quero cadastrar categorias de receita e despesa, para classificar minhas transações.
- Critérios de aceite:
  - O formulário exige nome e tipo (receita ou despesa).
  - A categoria criada aparece na listagem do usuário.

**US08:** Como usuário autenticado, quero editar e excluir minhas categorias, para mantê-las organizadas.
- Critérios de aceite:
  - A listagem exibe apenas as categorias do usuário logado.
  - A exclusão exige confirmação.

### Épico 5 — Transações

**US09:** Como usuário autenticado, quero registrar uma transação, para acompanhar minhas entradas e saídas.
- Critérios de aceite:
  - O formulário exige valor, tipo, data, conta e categoria; descrição é opcional.
  - A transação é vinculada à conta e categoria selecionadas.

**US10:** Como usuário autenticado, quero listar, filtrar, editar e excluir minhas transações, para manter meu controle financeiro correto.
- Critérios de aceite:
  - A listagem exibe apenas transações do usuário logado.
  - É possível filtrar por conta, categoria, tipo e período.
  - A exclusão exige confirmação.

### Épico 6 — Dashboard

**US11:** Como usuário autenticado, quero visualizar um dashboard com meu saldo consolidado e últimas movimentações, para ter uma visão geral da minha situação financeira.
- Critérios de aceite:
  - Exibe saldo total somando todas as contas.
  - Exibe total de receitas e despesas do período atual.
  - Exibe lista das últimas transações registradas.

### Épico 7 — Site público

**US12:** Como visitante, quero acessar uma landing page que explique o produto, para entender do que se trata antes de me cadastrar.
- Critérios de aceite:
  - A página é acessível sem login.
  - Contém botões visíveis de "Cadastre-se" e "Entrar".

---

## 11. Métricas de sucesso

### KPIs de produto

- Taxa de conclusão do cadastro (usuários que iniciam vs. finalizam o cadastro).
- Tempo médio para o primeiro lançamento de transação após o cadastro.
- Número médio de contas bancárias cadastradas por usuário.
- Número médio de transações registradas por usuário/mês.

### KPIs de usuário

- Taxa de retorno (usuários que fazem login mais de uma vez na semana).
- Taxa de abandono no fluxo de cadastro/login.
- Percentual de usuários que utilizam categorias personalizadas.

### KPIs técnicos

- Tempo médio de resposta das páginas principais (dashboard, listagens).
- Taxa de erros 4xx/5xx nas rotas autenticadas.

---

## 12. Riscos e mitigações

| Risco | Impacto | Mitigação |
|---|---|---|
| Complexidade crescente por adição de funcionalidades não previstas | Alto | Manter escopo restrito a este PRD; novas features exigem novo ciclo de planejamento |
| Inconsistência visual entre telas | Médio | Uso obrigatório de template base e componentes reutilizáveis (design system) |
| Falta de testes nas fases iniciais pode gerar regressões | Médio | Reservar sprint final dedicada exclusivamente a testes automatizados |
| Ausência de Docker pode gerar diferenças entre ambientes de desenvolvimento | Baixo | Documentar setup local claramente; Docker implementado em sprint final |
| Uso de SQLite pode limitar escalabilidade futura | Baixo | Aceitável para o escopo atual (uso pessoal); migração de banco pode ser avaliada futuramente |
| Login por e-mail exige customização do model de usuário, gerando risco de erro na migração inicial | Médio | Definir `AUTH_USER_MODEL` customizado antes da primeira migração do projeto |

---
