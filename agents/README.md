# Agentes de IA — Finanpy

Esta pasta define os agentes especialistas de um time de desenvolvimento de software focado exclusivamente na stack do **Finanpy**: Python + Django, Django Template Language (DTL), TailwindCSS e SQLite (ver [PRD.md](../PRD.md) e [docs/README.md](../docs/README.md)).

Cada agente é um arquivo `.md` com frontmatter (`name`, `description`, `tools`, `model`) no formato de subagente do Claude Code. Foram criados **apenas os agentes necessários para produzir e validar código** neste projeto — nada de papéis genéricos (PM, designer, etc.) que não implementam ou validam código diretamente.

## Como ativar

Estes arquivos vivem em `agents/` (raiz do projeto) como especificação versionada, e não são carregados automaticamente pelo Claude Code. Para transformá-los em subagentes reais e acionáveis, copie (ou link) o(s) arquivo(s) desejado(s) para `.claude/agents/` na raiz do projeto:

```bash
mkdir -p .claude/agents
cp agents/*.md .claude/agents/
```

Os agentes que usam Context7 (`django-backend-engineer`, `django-tailwind-frontend`, `qa-tester-playwright`) exigem o MCP server **context7** configurado. O agente de QA também exige o MCP server **playwright** configurado (ferramentas `mcp__playwright__*`) para conseguir abrir e interagir com o navegador.

## Índice de agentes

| Agente | Descrição | Quando usar |
|---|---|---|
| [django-backend-engineer](django-backend-engineer.md) | Especialista em backend Django: models (`TimeStampedModel`), Class Based Views, `ModelForm`s, `urls.py`, `admin.py`, `signals.py`, migrations e o model de usuário customizado com login por e-mail. Usa Context7 para validar a API atual do Django antes de escrever código. | Ao criar ou alterar qualquer model, view, form, signal, rota ou regra de negócio no servidor — ex.: implementar o CRUD de contas/categorias/transações, o `UserManager` customizado, ou o cálculo do dashboard. |
| [django-tailwind-frontend](django-tailwind-frontend.md) | Especialista em frontend: templates DTL e TailwindCSS seguindo à risca o [design system](../docs/design-system.md) do projeto (paleta índigo/roxo, cards, botões, sidebar). Usa Context7 para validar sintaxe atual de Tailwind/DTL. | Ao criar ou alterar qualquer template `.html`, `base.html`/`base_public.html`/`base_app.html`, partials (`_navbar`, `_sidebar`, `_messages`, `_footer`), ou ao ajustar responsividade e consistência visual entre telas. |
| [qa-tester-playwright](qa-tester-playwright.md) | QA/tester que navega o app de verdade no navegador via Playwright MCP, validando as user stories do PRD (US01-US12), o isolamento de dados entre usuários, a responsividade e a aderência ao design system. Não escreve testes automatizados nem código de produção. | Depois que uma feature (model + view + template) estiver implementada, antes de considerá-la pronta — para validar o fluxo real end-to-end e reportar bugs de comportamento ou de design. |

## Fluxo típico de uma feature

1. **django-backend-engineer** implementa model, view, form, url e admin (com migrations aplicadas).
2. **django-tailwind-frontend** implementa os templates da feature seguindo o design system.
3. **qa-tester-playwright** valida o fluxo completo no navegador contra o PRD e reporta problemas encontrados de volta aos dois agentes anteriores.

## Fora de escopo (por design)

Não foram criados agentes de DevOps/Docker nem de testes automatizados, pois o [PRD.md](../PRD.md) (RNF12, RNF13) reserva essas frentes para as sprints finais (9 e 10) do projeto. Quando essas sprints começarem, novos agentes podem ser adicionados aqui seguindo o mesmo padrão.
