# Decisões Técnicas — Absconditus

## 1. Motor e linguagem: Godot 4 + GDScript

**Motivo:** stack oficial definida pelo criador. Godot 4 é leve, adequado a jogos 2D isométricos, roda bem em PC e o GDScript é acessível para um desenvolvedor iniciante com assistência de IA.

## 2. Plataforma inicial: Windows PC/notebook

**Motivo:** público-alvo e ambiente de desenvolvimento do criador. Exportação para outras plataformas pode ser avaliada depois.

## 3. Estratégia de desenvolvimento incremental

**Motivo:** evitar implementar todos os sistemas de uma vez. A Etapa 1 (esta) entrega apenas a fundação técnica: estrutura de pastas, projeto Godot, Git e documentação. Sistemas de movimento, combate, magias, inventário e criação de personagem virão em etapas posteriores.

## 4. Arquitetura modular com separação de responsabilidades

**Motivo:** facilitar manutenção, testes automatizados e evitar acoplamento entre UI e regras de jogo.

## 5. Nenhuma dependência externa

**Motivo:** reduzir atrito de instalação, build e exportação. Apenas Godot + GDScript.

## 6. Local do projeto

`/d/TLB/Absconditus/Absconditus Game/` — subpasta da pasta existente do Absconditus, preservando materiais anteriores (ficha, site, docs, imagens) sem sobrescrevê-los.
