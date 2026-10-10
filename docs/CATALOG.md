# Catálogo de scripts

[← Início](../README.md) · [Mapa de migração](./migration-map.json)

**Critérios de status:** **Exemplo novo** = criado nesta reorganização, sem promessa de validação em todos os ambientes; **Legado** = preservado do histórico, sem auditoria funcional; **Revisão obrigatória** = problema conhecido ou impacto operacional.

## Novos exemplos (11)

| Arquivo | Categoria | Estado |
| :--- | :--- | :--- |
| [`cobol/hello-world.cbl`](../cobol/hello-world.cbl) | cobol | Exemplo novo |
| [`go/hello-world.go`](../go/hello-world.go) | go | Exemplo novo |
| [`gpo/inventory-gpos.ps1`](../gpo/inventory-gpos.ps1) | gpo | Exemplo novo |
| [`javascript/hello-world.js`](../javascript/hello-world.js) | javascript | Exemplo novo |
| [`macos/system-report.sh`](../macos/system-report.sh) | macos | Exemplo novo |
| [`mainframe/hello.jcl`](../mainframe/hello.jcl) | mainframe | Exemplo novo |
| [`osint/normalize-indicators.py`](../osint/normalize-indicators.py) | osint | Exemplo novo |
| [`python/hello-world.py`](../python/hello-world.py) | python | Exemplo novo |
| [`shell/check-disk-space.sh`](../shell/check-disk-space.sh) | shell | Exemplo novo |
| [`typescript/hello-world.ts`](../typescript/hello-world.ts) | typescript | Exemplo novo |
| [`web-scripts/extract-links.py`](../web-scripts/extract-links.py) | web-scripts | Exemplo novo |

## Acervo histórico (25)

| Novo arquivo | Origem | Avaliação |
| :--- | :--- | :--- |
| [`assembly/legacy/calculator.asm`](../assembly/legacy/calculator.asm) | `Testes/Assembly/Caculator.asm` | ⚠️ Exemplo ilustrativo com operações/sistema não validados. |
| [`c/legacy/buscadados.c`](../c/legacy/buscadados.c) | `Testes/C/buscadados.c` | 🧪 Legado não validado |
| [`cobol/legacy/olamundo.cpy`](../cobol/legacy/olamundo.cpy) | `Testes/cobol/Olamundo.cpy` | ⚠️ Código de programa armazenado com extensão de copybook (.cpy). |
| [`csharp/legacy/servicesextension.cs`](../csharp/legacy/servicesextension.cs) | `Testes/c#/Servicesextension.cs` | 🧪 Legado não validado |
| [`go/legacy/buscacpf.go`](../go/legacy/buscacpf.go) | `Testes/GO/buscacpf.go` | 🧪 Legado não validado |
| [`java/legacy/buscadados.java`](../java/legacy/buscadados.java) | `Testes/Java/buscadados.java` | ⚠️ Nome da classe não corresponde ao nome do arquivo; requer correção. |
| [`javascript/legacy/busca-namett.js`](../javascript/legacy/busca-namett.js) | `Testes/Java_script/Busca namett.js` | ⚠️ Depende de credenciais e endpoint externo; não validado. |
| [`javascript/legacy/buscadados.js`](../javascript/legacy/buscadados.js) | `Testes/Java_script/buscadados.js` | 🧪 Legado não validado |
| [`javascript/legacy/buscanamefb.js`](../javascript/legacy/buscanamefb.js) | `Testes/Java_script/buscanamefb.js` | ⚠️ Contém texto explicativo não comentado; JavaScript inválido. |
| [`pascal/legacy/calculator.pas`](../pascal/legacy/calculator.pas) | `Testes/Pascal/caculator.pas` | 🧪 Legado não validado |
| [`php/legacy/buscadado.php`](../php/legacy/buscadado.php) | `Testes/php/buscadado.php` | 🧪 Legado não validado |
| [`python/legacy/busca-cpf-web.py`](../python/legacy/busca-cpf-web.py) | `Testes/Python/Busca-cpf-web.py` | ⚠️ Usa endpoint fictício; não é ferramenta de consulta pronta. |
| [`python/legacy/buscacpf2.py`](../python/legacy/buscacpf2.py) | `Testes/Python/buscacpf2.py` | 🧪 Legado não validado |
| [`python/legacy/buscadado.py`](../python/legacy/buscadado.py) | `Testes/Python/buscadado.py` | 🧪 Legado não validado |
| [`python/legacy/buscasdados.py`](../python/legacy/buscasdados.py) | `Testes/Python/buscasdados.py` | 🧪 Legado não validado |
| [`python/legacy/comportamento-suspeito-xls.py`](../python/legacy/comportamento-suspeito-xls.py) | `Testes/Python/Comportamento_Supeito_XLS.py` | 🧪 Legado não validado |
| [`r/legacy/buscadados.r`](../r/legacy/buscadados.r) | `Testes/R/buscadados.r` | 🧪 Legado não validado |
| [`ruby/legacy/buscasdados.rb`](../ruby/legacy/buscasdados.rb) | `Testes/Ruby/buscasdados.rb` | 🧪 Legado não validado |
| [`ruby/legacy/calculator.rb`](../ruby/legacy/calculator.rb) | `Testes/Ruby/Calculator.rb` | 🧪 Legado não validado |
| [`ruby/legacy/ola-mundo.rb`](../ruby/legacy/ola-mundo.rb) | `Testes/Ruby/Olámundo.rb` | 🧪 Legado não validado |
| [`shell/legacy/wazuh-disable-cache.sh`](../shell/legacy/wazuh-disable-cache.sh) | `linux/Wazuh desabilit cache` | ⚠️ Modifica configuração do Wazuh; comportamento e sintaxe exigem revisão. |
| [`sql/legacy/buscadados.sql`](../sql/legacy/buscadados.sql) | `Testes/sql/buscadados.sql` | 🧪 Legado não validado |
| [`swift/legacy/buscadados.swift`](../swift/legacy/buscadados.swift) | `Testes/Swift/buscadados.swift` | 🧪 Legado não validado |
| [`typescript/legacy/buscadados.ts`](../typescript/legacy/buscadados.ts) | `Testes/TypeScript/buscadados.ts` | ⚠️ Arquivo truncado/incompleto; não compila. |
| [`windows/legacy/wazuh-disable-cache.bat`](../windows/legacy/wazuh-disable-cache.bat) | `Rwindows/Wazuh desabilit cache` | ⚠️ Modifica arquivo de configuração; não executar sem revisão e backup. |

O conteúdo dos arquivos migrados foi mantido por SHA de blob do Git. Renomeações não constituem correção de código. Nenhum script foi executado nesta migração.
