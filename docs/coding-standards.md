# Padrões de código

Estas são as convenções que todo código do projeto deve seguir.

## Idioma

- **Código em inglês**: nomes de variáveis, funções, classes, comentários e mensagens de commit devem ser escritos em inglês.
- **Interface em português**: todo texto exibido na interface (labels, mensagens, títulos) deve estar em português brasileiro.

## Estilo Python

- Seguir a **PEP8**.
- Usar **aspas simples** (`'`) sempre que possível.

## Views

- Priorizar **Class Based Views** e recursos nativos do Django (`django.views.generic`) em vez de function based views.
- Views que exigem autenticação devem usar `LoginRequiredMixin`.
- Querysets de listagem, edição e exclusão devem sempre ser filtrados pelo usuário logado (`request.user`), garantindo que um usuário nunca acesse dados de outro.

## Signals

- Quando forem utilizados, os signals devem ficar em um arquivo `signals.py` dentro da app correspondente, e conectados no método `ready()` do `apps.py` da app.

## Models

- Todo model do sistema deve possuir os campos `created_at` e `updated_at`.
- Um model abstrato (`TimeStampedModel`) centraliza esses dois campos e deve ser herdado pelos demais models, evitando repetição.
- Models de domínio (`Account`, `Category`, `Transaction`, `Profile`) devem ter uma `ForeignKey`/`OneToOneField` para `User`.

## Organização por domínio

- Cada entidade do sistema vive em sua própria app Django, isolada por responsabilidade (veja [arquitetura](architecture.md)). Evite misturar regras de negócio de domínios diferentes na mesma app.

## Banco de dados

- O projeto utiliza exclusivamente o SQLite padrão do Django. Não introduzir outros bancos de dados.

## Fora de escopo (por enquanto)

- **Docker**: não deve ser implementado nas fases iniciais do projeto.
- **Testes automatizados**: não devem ser implementados nas fases iniciais do projeto.

## Escopo

- O sistema não deve conter funcionalidades além das explicitamente definidas no [PRD.md](../PRD.md). Novas funcionalidades exigem atualização do PRD antes de serem implementadas.
