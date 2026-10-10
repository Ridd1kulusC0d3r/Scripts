# Primeiros passos

[← Início](../README.md)

1. Escolha uma [categoria](../README.md) e leia seu `README.md`.
2. Confira no [catálogo](./CATALOG.md) se o arquivo é novo ou legado.
3. Inspecione o código e as dependências antes de executar. Prefira ambiente isolado de testes para scripts não validados.
4. Execute somente com autorização, dados próprios ou exemplos públicos, evitando permissões elevadas desnecessárias.

## Demonstrações locais e sem requisições de rede

```bash
python3 python/hello-world.py
python3 web-scripts/extract-links.py arquivo-local.html
python3 osint/normalize-indicators.py indicadores-publicos.txt
bash shell/check-disk-space.sh
```

O comando `extract-links.py` requer um arquivo HTML local; `normalize-indicators.py` requer um arquivo TXT local com um indicador por linha. Esses programas não fazem requisições externas.

## Demais ambientes

- **macOS:** `bash macos/system-report.sh` (somente leitura, no macOS).
- **Windows/GPO:** `gpo/inventory-gpos.ps1` requer PowerShell, RSAT/GroupPolicy e acesso apropriado ao domínio.
- **Go:** `go run go/hello-world.go` com toolchain Go disponível.
- **JavaScript:** `node javascript/hello-world.js` com Node.js instalado.
- **TypeScript:** transpile `typescript/hello-world.ts` usando um compilador TypeScript instalado.
- **COBOL/Mainframe:** leia o README específico; o JCL é ilustrativo.

Scripts em `legacy/` **não** fazem parte das instruções de execução recomendadas.
