# Visão geral

## O que é

**Finanpy** é um sistema web de gestão de finanças pessoais, desenvolvido em **Python + Django**, com frontend renderizado via **Django Template Language (DTL)** estilizado com **TailwindCSS**.

O objetivo é permitir que uma pessoa registre contas bancárias, categorize seus lançamentos financeiros e acompanhe entradas e saídas em um dashboard central.

## Propósito

Oferecer uma solução simples e visualmente moderna para que pessoas físicas organizem sua vida financeira, sem a complexidade de planilhas ou de sistemas financeiros corporativos.

## Público-alvo

- Pessoas físicas que desejam controlar receitas e despesas pessoais.
- Usuários que buscam uma alternativa simples a planilhas de controle financeiro.
- Usuários que preferem um sistema web leve, sem necessidade de instalar aplicativos.

## Abordagem

O projeto segue uma abordagem enxuta, sem over engineering:

- Banco de dados **SQLite**.
- Autenticação **nativa do Django**, com login por e-mail.
- Sistema **full stack Django**: sem API separada e sem frontend desacoplado (SPA). Toda a renderização é feita no servidor.
- Domínios do sistema separados em **apps Django independentes**, cada uma com uma responsabilidade única.

## Estado atual do projeto

O projeto está em fase inicial de setup: o projeto Django (`core`) e as cinco apps de domínio (`users`, `profiles`, `accounts`, `categories`, `transactions`) já foram criadas e registradas em `INSTALLED_APPS`, mas ainda não possuem models, views, formulários ou templates implementados. Consulte o [PRD.md](../PRD.md) para o roadmap completo de sprints e o que falta ser construído.
