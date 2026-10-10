# Contribuindo

[← Início](../README.md)

## Onde colocar um script?

Use uma única pasta canônica, normalmente por **linguagem** (`python/`, `go/` etc.), **plataforma** (`macos/`, `windows/`, `mainframe/`) ou **tarefa principal** (`osint/`, `web-scripts/`, `gpo/`). Evite duplicação: para scripts que cabem em mais de uma categoria, use links cruzados entre READMEs.

## Padrões

- Nomes em `kebab-case` quando possível, com extensão correta.
- Inclua descrição, compatibilidade, dependências, parâmetros, saída esperada e riscos relevantes.
- Não use exemplos com dados pessoais reais, credenciais ou URLs internas.
- Trate dados de terceiros e integrações externas de forma legal, proporcional e verificável.
- Novos exemplos devem ser autocontidos quando possível e acompanhados por testes ou instruções reprodutíveis.
- Não promova arquivos `legacy/` a scripts estáveis sem correção e validação explícitas em PR separado.

## Convenção de status

**Exemplo novo:** pequeno programa introduzido na reorganização, ainda sujeito a revisão por ambiente.

**Legado:** arquivo conservado bit a bit, com problemas eventualmente conhecidos.

**Validado:** só use esta classificação após documentar ambiente, comandos de teste e resultado verificável.

Para mover arquivos legados, atualize `docs/migration-map.json` e o catálogo mantendo rastreabilidade dos hashes originais.
