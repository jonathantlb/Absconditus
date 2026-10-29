# Arquitetura — Absconditus

## Visão geral

Absconditus é um RPG indie 2D isométrico para PC, com atmosfera Noir, terror investigativo e sobrenatural. A arquitetura segue o princípio de separação de responsabilidades para que um desenvolvedor iniciante consiga manter o código com assistência de IA, sem complexidade desnecessária.

## Diretórios e responsabilidades

| Diretório | Responsabilidade |
|-----------|------------------|
| `scenes/` | Cenas do Godot (árvore de nós, layout visual, transições). Cada subpasta corresponde a um contexto do jogo. |
| `scripts/` | Lógica de jogo em GDScript. Separação entre núcleo (core), sistemas, entidades e UI. |
| `data/` | Conteúdo e dados do jogo: classes, raças, magias, armas, itens, habilidades, inimigos. Arquivos de configuração, não lógica. |
| `assets/` | Recursos visuais e sonoros: personagens, ambientes, retratos, ícones, áudio, fontes. |
| `tests/` | Testes automatizados da lógica de jogo (dados, atributos, dano, etc.). |
| `docs/` | Documentação técnica do projeto. |

## Camadas

1. **Regras e lógica do jogo:** centralizadas em `scripts/core/` e `scripts/systems/`. Cálculos de atributos, dano, rolagem de dados, progressão e magias vivem aqui.
2. **Interface do usuário:** `scripts/ui/` e `scenes/ui/`. A UI apenas consome dados expostos pelos sistemas — nunca contém cópias das regras de combate, dano, atributos ou magias.
3. **Dados e conteúdo:** `data/`. Conteúdo configurável (ex.: valores de uma classe, custo de uma magia) separado do código.
4. **Apresentação visual:** `scenes/` e `assets/`. Cenas, nós visuais, sprites e áudio.
5. **Salvamento e carregamento:** sistema dedicado (a ser implementado em etapas futuras), isolado do restante.
6. **Testes automatizados:** `tests/`. Validação da lógica pura, sem dependência de cenas do Godot sempre que possível.

## Convenções

- Nomes em português ou inglês, consistentes dentro de cada diretório.
- Scripts com nomes descritivos (`sistema_dano.gd`, `gerenciador_salvamento.gd`).
- Nenhuma dependência externa além do Godot 4 + GDScript.
