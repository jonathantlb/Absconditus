# Configuração de Desenvolvimento — Absconditus

## Ferramentas instaladas

| Ferramenta | Versão | Status |
|------------|--------|--------|
| Git | 2.53.0.windows.3 | ✅ Instalado |
| Godot 4.x | — | ❌ Não encontrado no sistema |

## Requisitos

- Windows PC/notebook (plataforma inicial).
- Godot 4.x (preferencialmente versão LTS / estável).
- Git para controle de versão.

## Comandos

### Abrir o projeto
Após instalar o Godot, abra o editor e selecione "Importar" ou "Abrir projeto", apontando para a pasta que contém o `project.godot`.

### Executar
No editor do Godot, clique em "Executar Projeto" (ou F5).

### Testar
Os testes automatizados ficam em `tests/`. A execução depende do framework de testes a ser definido (GDUnit ou similar, a confirmar).

### Exportar para Windows
No Godot: Projeto > Exportar > adicionar preset Windows > exportar. A configuração de exportação será detalhada nas próximas etapas.

## Observações

- Não instale C#, C++, Unity, Unreal Engine ou bancos de dados externos. A stack oficial é Godot 4 + GDScript.
- Não sobrescreva arquivos existentes sem verificar seu conteúdo.
