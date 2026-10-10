# Segurança, qualidade e limitações

[← Início](../README.md)

## Não executar legacy indiscriminadamente

Todo código originalmente encontrado em `Testes/`, `Rwindows/` e `linux/` foi migrado **sem alterações funcionais** para preservar a proveniência. Isso **não é uma validação de segurança**.

### Problemas observados na inspeção estática

- O TypeScript `typescript/legacy/buscadados.ts` está incompleto (termina no meio de um callback).
- O JavaScript `javascript/legacy/buscanamefb.js` contém texto não comentado, logo não é um script JS válido.
- Alguns scripts de busca usam `example.com`, `exemplo.com` ou chaves fictícias. Não representam integrações reais e não comprovam dados de terceiros.
- Os scripts `windows/legacy/wazuh-disable-cache.bat` e `shell/legacy/wazuh-disable-cache.sh` tentam alterar configuração do agente Wazuh; não foram testados. É proibido pressupor que a mensagem de sucesso corresponda à alteração pretendida.
- O arquivo COBOL histórico com extensão `.cpy` se parece com um programa, não com um copybook convencional.
- Exemplos de buscas por identificadores e redes exigem avaliação de privacidade, base legal e permissão apropriada.

## Regras de contribuição

1. Nunca introduza credenciais, cookies, tokens ou dados pessoais reais em commits e logs.
2. Prefira somente leitura, entradas locais e comportamento explícito por padrão.
3. Se alterar arquivos, serviços, políticas ou rede: documente exatamente os efeitos, requisitos e reversão.
4. Defina timeout, erros e validação de entradas em scripts que fazem requisições de rede.
5. Execute testes em ambientes controlados antes de considerar qualquer script pronto para uso.
6. Evite mensagens de sucesso quando não houver verificação real da operação.

A CI verifica integridade organizacional e sintaxe dos **novos exemplos Python**; isso não equivale a testes completos de execução nem a revisão de segurança dos programas legados.
