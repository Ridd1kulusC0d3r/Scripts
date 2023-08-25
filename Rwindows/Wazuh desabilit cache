@echo off

rem Caminho para o arquivo de configuração do agente Wazuh
set "config_file=C:\Program Files (x86)\ossec-agent\etc\ossec.conf"

rem Verifica se o arquivo de configuração existe
if exist "%config_file%" (
    rem Verifica se a seção [wazuh] existe no arquivo de configuração
    find "[wazuh]" "%config_file%" > nul
    if %errorlevel% == 0 (
        rem Adiciona ou ajusta o parâmetro <disabled>yes</disabled> na seção [wazuh]
        findstr /r /c:"<disabled>.*<\/disabled>" "%config_file%" > nul
        if %errorlevel% == 1 (
            echo.>> "%config_file%"
            echo ^  ^<disabled^>yes^</disabled^>> "%config_file%"
        ) else (
            findstr /r /c:"<disabled>.*<\/disabled>" "%config_file%" > "%config_file%.bak"
            findstr /v /r /c:"<disabled>.*<\/disabled>" "%config_file%.bak" > "%config_file%"
            echo ^  ^<disabled^>yes^</disabled^>> "%config_file%"
            del "%config_file%.bak"
        )
        echo Cache do agente Wazuh foi desabilitado com sucesso!
    ) else (
        echo Seção [wazuh] não encontrada no arquivo de configuração.
    )
) else (
    echo Arquivo de configuração não encontrado.
)

pause
