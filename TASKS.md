## 13. Lista de tarefas

> Legenda: `[ ]` pendente · `[X]` concluído

### Sprint 0 — Setup do projeto

- [x] **T0.1 — Estrutura inicial do projeto**
  - [x] T0.1.1 Criar ambiente virtual Python e instalar Django.
  - [x] T0.1.2 Criar projeto Django `core` com `django-admin startproject`.
  - [x] T0.1.3 Ajustar estrutura de pastas conforme arquitetura definida (apps na raiz, `core` como pasta de configuração).
  - [x] T0.1.4 Configurar `.gitignore` (ambiente virtual, `db.sqlite`, `__pycache__`, etc).
  - [x] T0.1.5 Criar arquivo `requirements.txt` com as dependências iniciais (Django).
- [x] **T0.2 — Criação das apps Django**
  - [x] T0.2.1 Criar app `users` com `startapp`.
  - [x] T0.2.2 Criar app `profiles` com `startapp`.
  - [x] T0.2.3 Criar app `accounts` com `startapp`.
  - [x] T0.2.4 Criar app `categories` com `startapp`.
  - [x] T0.2.5 Criar app `transactions` com `startapp`.
  - [x] T0.2.6 Registrar todas as apps em `INSTALLED_APPS` no `settings.py`.
- [ ] **T0.3 — Configuração base do settings**
  - [ ] T0.3.1 Configurar `TEMPLATES` para buscar templates em pasta global `templates/` na raiz do projeto.
  - [ ] T0.3.2 Configurar `STATICFILES_DIRS` e `STATIC_URL` para arquivos estáticos globais.
  - [ ] T0.3.3 Configurar idioma padrão (`LANGUAGE_CODE = 'pt-br'`) e timezone (`TIME_ZONE = 'America/Sao_Paulo'`).
  - [ ] T0.3.4 Configurar `LOGIN_URL`, `LOGIN_REDIRECT_URL` e `LOGOUT_REDIRECT_URL`.
- [ ] **T0.4 — Base model compartilhada**
  - [ ] T0.4.1 Criar model abstrato `TimeStampedModel` na app `core` com os campos `created_at` (auto_now_add) e `updated_at` (auto_now).
- [ ] **T0.5 — Configuração do TailwindCSS**
  - [ ] T0.5.1 Definir estratégia de integração do Tailwind (CDN para simplicidade do projeto).
  - [ ] T0.5.2 Criar `templates/base.html` incluindo o script/link do Tailwind.
  - [ ] T0.5.3 Definir paleta de cores e componentes base do design system no `base.html`.
- [ ] **T0.6 — Templates e partials base**
  - [ ] T0.6.1 Criar pasta `templates/partials/` com `_navbar.html`, `_sidebar.html`, `_messages.html` e `_footer.html`.
  - [ ] T0.6.2 Criar template `base_public.html` (para landing page/login/cadastro) sem sidebar.
  - [ ] T0.6.3 Criar template `base_app.html` (para área autenticada) com sidebar e header.

### Sprint 1 — Usuários e autenticação

- [ ] **T1.1 — Model de usuário customizado**
  - [ ] T1.1.1 Criar model `User` na app `users` herdando de `AbstractUser`.
  - [ ] T1.1.2 Remover/ajustar campo `username`, definindo `email` como `USERNAME_FIELD`.
  - [ ] T1.1.3 Definir `REQUIRED_FIELDS` (ex: `first_name`).
  - [ ] T1.1.4 Criar `UserManager` customizado com métodos `create_user` e `create_superuser` baseados em e-mail.
  - [ ] T1.1.5 Adicionar `created_at` e `updated_at` herdando de `TimeStampedModel`.
  - [ ] T1.1.6 Configurar `AUTH_USER_MODEL = 'users.User'` no `settings.py`.
  - [ ] T1.1.7 Gerar e aplicar migrações iniciais do model `User`.
- [ ] **T1.2 — Admin de usuários**
  - [ ] T1.2.1 Registrar model `User` no `admin.py` da app `users`, adaptando `UserAdmin` para uso do e-mail.
- [ ] **T1.3 — Cadastro de usuários (sign up)**
  - [ ] T1.3.1 Criar `UserCreationForm` customizado (e-mail, nome, senha e confirmação de senha).
  - [ ] T1.3.2 Criar `SignUpView` (Class Based View, `CreateView`) na app `users`.
  - [ ] T1.3.3 Criar template `users/signup.html` seguindo o design system (formulário centralizado, card branco sobre fundo `bg-slate-100`).
  - [ ] T1.3.4 Adicionar validação de e-mail único e mensagens de erro amigáveis.
  - [ ] T1.3.5 Redirecionar para tela de login após cadastro bem-sucedido, com mensagem de sucesso.
- [ ] **T1.4 — Login**
  - [ ] T1.4.1 Criar `AuthenticationForm` customizado utilizando e-mail como campo de login.
  - [ ] T1.4.2 Criar `LoginView` (baseada em `django.contrib.auth.views.LoginView`) com o form customizado.
  - [ ] T1.4.3 Criar template `users/login.html` seguindo o design system.
  - [ ] T1.4.4 Configurar redirecionamento para o dashboard após login bem-sucedido.
- [ ] **T1.5 — Logout**
  - [ ] T1.5.1 Configurar `LogoutView` nativa do Django.
  - [ ] T1.5.2 Adicionar botão/link de logout na sidebar.
- [ ] **T1.6 — Proteção de rotas**
  - [ ] T1.6.1 Aplicar `LoginRequiredMixin` em todas as views internas do sistema.
  - [ ] T1.6.2 Testar manualmente o redirecionamento de usuários não autenticados para o login.
- [ ] **T1.7 — URLs de autenticação**
  - [ ] T1.7.1 Criar `users/urls.py` com rotas de `signup`, `login` e `logout`.
  - [ ] T1.7.2 Incluir `users.urls` no `core/urls.py`.

### Sprint 2 — Perfis

- [ ] **T2.1 — Model de perfil**
  - [ ] T2.1.1 Criar model `Profile` na app `profiles`, herdando de `TimeStampedModel`.
  - [ ] T2.1.2 Adicionar `OneToOneField` para `User`.
  - [ ] T2.1.3 Adicionar campos `phone`, `birth_date` e `avatar` (opcionais).
  - [ ] T2.1.4 Gerar e aplicar migrações do model `Profile`.
- [ ] **T2.2 — Criação automática de perfil**
  - [ ] T2.2.1 Criar `profiles/signals.py` com signal `post_save` do model `User` para criar `Profile` automaticamente.
  - [ ] T2.2.2 Conectar o signal no `apps.py` da app `profiles` (`ready()`).
- [ ] **T2.3 — Admin de perfis**
  - [ ] T2.3.1 Registrar model `Profile` no `admin.py` da app `profiles`.
- [ ] **T2.4 — Visualização e edição de perfil**
  - [ ] T2.4.1 Criar `ProfileDetailView` (ou reaproveitar `UpdateView`) na app `profiles`.
  - [ ] T2.4.2 Criar `ProfileForm` (ModelForm) com os campos editáveis.
  - [ ] T2.4.3 Criar template `profiles/detail.html` seguindo o design system (card com dados do usuário e do perfil).
  - [ ] T2.4.4 Garantir que o usuário só possa editar o próprio perfil (`get_object` filtrando por `request.user`).
- [ ] **T2.5 — URLs de perfil**
  - [ ] T2.5.1 Criar `profiles/urls.py` com rota de visualização/edição do perfil.
  - [ ] T2.5.2 Incluir `profiles.urls` no `core/urls.py`.
  - [ ] T2.5.3 Adicionar link "Perfil" na sidebar.

### Sprint 3 — Contas bancárias

- [ ] **T3.1 — Model de conta bancária**
  - [ ] T3.1.1 Criar model `Account` na app `accounts`, herdando de `TimeStampedModel`.
  - [ ] T3.1.2 Adicionar `ForeignKey` para `User`.
  - [ ] T3.1.3 Adicionar campos `name`, `account_type` (choices) e `initial_balance`.
  - [ ] T3.1.4 Gerar e aplicar migrações do model `Account`.
- [ ] **T3.2 — Admin de contas**
  - [ ] T3.2.1 Registrar model `Account` no `admin.py` da app `accounts`.
- [ ] **T3.3 — Listagem de contas**
  - [ ] T3.3.1 Criar `AccountListView` (Class Based View, `ListView`) filtrando por `request.user`.
  - [ ] T3.3.2 Criar template `accounts/list.html` com grid de cards seguindo o design system.
- [ ] **T3.4 — Criação de conta**
  - [ ] T3.4.1 Criar `AccountForm` (ModelForm).
  - [ ] T3.4.2 Criar `AccountCreateView` (`CreateView`) associando a conta ao usuário logado.
  - [ ] T3.4.3 Criar template `accounts/form.html` reutilizável para criação e edição.
- [ ] **T3.5 — Edição de conta**
  - [ ] T3.5.1 Criar `AccountUpdateView` (`UpdateView`), restringindo o queryset ao usuário logado.
- [ ] **T3.6 — Exclusão de conta**
  - [ ] T3.6.1 Criar `AccountDeleteView` (`DeleteView`), restringindo o queryset ao usuário logado.
  - [ ] T3.6.2 Criar template `accounts/confirm_delete.html` de confirmação, seguindo o design system.
- [ ] **T3.7 — URLs de contas**
  - [ ] T3.7.1 Criar `accounts/urls.py` com rotas de listagem, criação, edição e exclusão.
  - [ ] T3.7.2 Incluir `accounts.urls` no `core/urls.py`.
  - [ ] T3.7.3 Adicionar link "Contas" na sidebar.

### Sprint 4 — Categorias

- [ ] **T4.1 — Model de categoria**
  - [ ] T4.1.1 Criar model `Category` na app `categories`, herdando de `TimeStampedModel`.
  - [ ] T4.1.2 Adicionar `ForeignKey` para `User`.
  - [ ] T4.1.3 Adicionar campos `name`, `category_type` (choices: receita/despesa) e `color`.
  - [ ] T4.1.4 Gerar e aplicar migrações do model `Category`.
- [ ] **T4.2 — Admin de categorias**
  - [ ] T4.2.1 Registrar model `Category` no `admin.py` da app `categories`.
- [ ] **T4.3 — Listagem de categorias**
  - [ ] T4.3.1 Criar `CategoryListView` (`ListView`) filtrando por `request.user`.
  - [ ] T4.3.2 Criar template `categories/list.html` com grid de cards coloridos por tipo (receita/despesa), seguindo o design system.
- [ ] **T4.4 — Criação de categoria**
  - [ ] T4.4.1 Criar `CategoryForm` (ModelForm).
  - [ ] T4.4.2 Criar `CategoryCreateView` (`CreateView`) associando a categoria ao usuário logado.
  - [ ] T4.4.3 Criar template `categories/form.html` reutilizável para criação e edição.
- [ ] **T4.5 — Edição de categoria**
  - [ ] T4.5.1 Criar `CategoryUpdateView` (`UpdateView`), restringindo o queryset ao usuário logado.
- [ ] **T4.6 — Exclusão de categoria**
  - [ ] T4.6.1 Criar `CategoryDeleteView` (`DeleteView`), restringindo o queryset ao usuário logado.
  - [ ] T4.6.2 Criar template `categories/confirm_delete.html` de confirmação.
- [ ] **T4.7 — URLs de categorias**
  - [ ] T4.7.1 Criar `categories/urls.py` com rotas de listagem, criação, edição e exclusão.
  - [ ] T4.7.2 Incluir `categories.urls` no `core/urls.py`.
  - [ ] T4.7.3 Adicionar link "Categorias" na sidebar.

### Sprint 5 — Transações

- [ ] **T5.1 — Model de transação**
  - [ ] T5.1.1 Criar model `Transaction` na app `transactions`, herdando de `TimeStampedModel`.
  - [ ] T5.1.2 Adicionar `ForeignKey` para `User`, `Account` e `Category`.
  - [ ] T5.1.3 Adicionar campos `description` (opcional), `amount`, `transaction_type` (choices) e `transaction_date`.
  - [ ] T5.1.4 Gerar e aplicar migrações do model `Transaction`.
- [ ] **T5.2 — Admin de transações**
  - [ ] T5.2.1 Registrar model `Transaction` no `admin.py` da app `transactions`.
- [ ] **T5.3 — Listagem de transações**
  - [ ] T5.3.1 Criar `TransactionListView` (`ListView`) filtrando por `request.user`.
  - [ ] T5.3.2 Implementar filtros via query params (conta, categoria, tipo, período) no `get_queryset`.
  - [ ] T5.3.3 Criar template `transactions/list.html` em formato de tabela responsiva, seguindo o design system.
  - [ ] T5.3.4 Adicionar formulário de filtro no topo da listagem (selects e campos de data).
- [ ] **T5.4 — Criação de transação**
  - [ ] T5.4.1 Criar `TransactionForm` (ModelForm), restringindo os `querysets` de conta/categoria ao usuário logado.
  - [ ] T5.4.2 Criar `TransactionCreateView` (`CreateView`) associando a transação ao usuário logado.
  - [ ] T5.4.3 Criar template `transactions/form.html` reutilizável para criação e edição.
- [ ] **T5.5 — Edição de transação**
  - [ ] T5.5.1 Criar `TransactionUpdateView` (`UpdateView`), restringindo o queryset ao usuário logado.
- [ ] **T5.6 — Exclusão de transação**
  - [ ] T5.6.1 Criar `TransactionDeleteView` (`DeleteView`), restringindo o queryset ao usuário logado.
  - [ ] T5.6.2 Criar template `transactions/confirm_delete.html` de confirmação.
- [ ] **T5.7 — URLs de transações**
  - [ ] T5.7.1 Criar `transactions/urls.py` com rotas de listagem, criação, edição e exclusão.
  - [ ] T5.7.2 Incluir `transactions.urls` no `core/urls.py`.
  - [ ] T5.7.3 Adicionar link "Transações" na sidebar.

### Sprint 6 — Dashboard

- [ ] **T6.1 — View do dashboard**
  - [ ] T6.1.1 Criar `DashboardView` (Class Based View, `TemplateView`) na app `core`.
  - [ ] T6.1.2 Calcular saldo total somando saldo inicial das contas e transações associadas.
  - [ ] T6.1.3 Calcular total de receitas e despesas do período atual (mês corrente).
  - [ ] T6.1.4 Obter as últimas transações registradas (ex: últimas 5).
- [ ] **T6.2 — Template do dashboard**
  - [ ] T6.2.1 Criar template `core/dashboard.html` seguindo o design system.
  - [ ] T6.2.2 Criar cards de resumo (saldo total, receitas do período, despesas do período) em grid responsivo.
  - [ ] T6.2.3 Criar seção de últimas transações em formato de lista/tabela.
- [ ] **T6.3 — URL do dashboard**
  - [ ] T6.3.1 Criar rota `dashboard/` no `core/urls.py`, protegida por `LoginRequiredMixin`.
  - [ ] T6.3.2 Adicionar link "Dashboard" na sidebar (item ativo por padrão).

### Sprint 7 — Site público (landing page)

- [ ] **T7.1 — View da landing page**
  - [ ] T7.1.1 Criar `LandingPageView` (`TemplateView`) na app `core`, acessível sem autenticação.
  - [ ] T7.1.2 Redirecionar usuários já autenticados diretamente para o dashboard.
- [ ] **T7.2 — Template da landing page**
  - [ ] T7.2.1 Criar template `core/landing.html` com seção hero (título, subtítulo, gradiente de fundo).
  - [ ] T7.2.2 Adicionar seção de benefícios/funcionalidades do produto.
  - [ ] T7.2.3 Adicionar header público com botões "Cadastre-se" e "Entrar".
  - [ ] T7.2.4 Adicionar footer simples.
- [ ] **T7.3 — URL da landing page**
  - [ ] T7.3.1 Configurar rota raiz (`/`) apontando para `LandingPageView`.

### Sprint 8 — Consistência visual e refinamento do design system

- [ ] **T8.1 — Revisão geral de componentes**
  - [ ] T8.1.1 Revisar todos os templates para garantir uso consistente das classes de botões, inputs e cards definidas no design system.
  - [ ] T8.1.2 Padronizar espaçamentos (`p-`, `m-`, `gap-`) entre todas as telas.
- [ ] **T8.2 — Mensagens e feedback ao usuário**
  - [ ] T8.2.1 Padronizar exibição das mensagens do Django (`messages`) como alerts/toasts no `_messages.html`.
  - [ ] T8.2.2 Aplicar cores semânticas (sucesso, erro, alerta) conforme design system.
- [ ] **T8.3 — Responsividade**
  - [ ] T8.3.1 Validar responsividade da sidebar em telas mobile (menu off-canvas).
  - [ ] T8.3.2 Validar responsividade das listagens (tabelas viram cards em telas pequenas, quando necessário).
  - [ ] T8.3.3 Validar responsividade dos formulários em telas pequenas.
- [ ] **T8.4 — Estados vazios**
  - [ ] T8.4.1 Criar componente de "estado vazio" (empty state) para listagens sem registros (contas, categorias, transações).

### Sprint 9 (final) — Dockerização

- [ ] **T9.1 — Containerização**
  - [ ] T9.1.1 Criar `Dockerfile` para a aplicação Django.
  - [ ] T9.1.2 Criar `docker-compose.yml` para orquestrar o serviço da aplicação.
  - [ ] T9.1.3 Configurar variáveis de ambiente via arquivo `.env`.
  - [ ] T9.1.4 Documentar comandos de build e execução via Docker no `README.md`.

### Sprint 10 (final) — Testes automatizados

- [ ] **T10.1 — Testes de models**
  - [ ] T10.1.1 Escrever testes unitários para os models `User`, `Profile`, `Account`, `Category` e `Transaction`.
- [ ] **T10.2 — Testes de views**
  - [ ] T10.2.1 Escrever testes de autenticação (cadastro, login, logout).
  - [ ] T10.2.2 Escrever testes de CRUD para contas bancárias.
  - [ ] T10.2.3 Escrever testes de CRUD para categorias.
  - [ ] T10.2.4 Escrever testes de CRUD para transações.
  - [ ] T10.2.5 Escrever testes do dashboard (cálculo de saldo e totais).
- [ ] **T10.3 — Testes de permissão**
  - [ ] T10.3.1 Garantir, via testes, que um usuário não acessa/edita/exclui dados de outro usuário.
