#!/bin/bash

# Caminho para o arquivo de configuração do agente Wazuh
config_file="/var/ossec/etc/ossec.conf"

# Verifica se o arquivo de configuração existe
if [ -f "$config_file" ]; then
    # Verifica se a seção [wazuh] existe no arquivo de configuração
    if grep -q "\[wazuh\]" "$config_file"; then
        # Adiciona ou ajusta o parâmetro <disabled>yes</disabled> na seção [wazuh]
        sed -i '/\[wazuh\]/a \  <disabled>yes<\/disabled>' "$config_file"
        echo "Cache do agente Wazuh foi desabilitado com sucesso!"
    else
        echo "Seção [wazuh] não encontrada no arquivo de configuração."
    fi
else
    echo "Arquivo de configuração não encontrado."
fi
