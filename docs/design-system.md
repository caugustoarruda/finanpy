# Design system

Guia visual a ser seguido em todas as telas do projeto, para manter uma identidade consistente: gradientes suaves, paleta harmônica e fundo claro (não totalmente branco). Sempre que possível, componentes devem ser reutilizados via templates base e `{% include %}` / `{% block %}` do Django.

## Paleta de cores

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

## Tipografia

- Fonte padrão: `font-sans` (stack padrão do Tailwind).
- Títulos de página: `text-2xl md:text-3xl font-bold text-slate-800`.
- Subtítulos de seção: `text-lg font-semibold text-slate-700`.
- Texto corrido: `text-sm text-slate-600`.
- Labels de formulário: `text-sm font-medium text-slate-700`.

## Botões

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

## Inputs e formulários

```html
<div class="mb-4">
  <label class="block text-sm font-medium text-slate-700 mb-1">Nome</label>
  <input type="text" class="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent">
</div>
```

- Inputs sempre com `rounded-lg`, `border-slate-300` e `focus:ring-2 focus:ring-indigo-500`.
- Mensagens de erro: `text-rose-600 text-xs mt-1`.
- Formulários organizados em `<form>` com `space-y-4`.

## Cards / painéis

```html
<div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
  <!-- conteúdo -->
</div>
```

## Grid e layout

- Container principal: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`.
- Grid de cards de resumo (dashboard): `grid grid-cols-1 md:grid-cols-3 gap-4`.
- Grid de listagens: `grid grid-cols-1 gap-4` com cards empilhados ou tabela responsiva.

## Menu / navegação

Sidebar (área autenticada), fixa em desktop e colapsável/off-canvas em mobile:

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

## Padrão de templates Django

- `templates/base.html`: layout base com Tailwind, blocos `{% block content %}` e `{% block title %}`.
- `templates/partials/`: componentes reutilizáveis (`_navbar.html`, `_sidebar.html`, `_messages.html`, `_footer.html`).
- Cada app possui sua própria pasta `templates/<app_name>/`, com templates próprios (`list.html`, `form.html`, `detail.html`, `confirm_delete.html`).
- Mensagens do Django (`django.contrib.messages`) devem ser exibidas como toasts/alerts, com cores semânticas (verde para sucesso, vermelho para erro).

> Nota: este design system ainda não foi implementado nos templates do projeto — ele define o padrão visual a ser seguido conforme as telas forem construídas.
