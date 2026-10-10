# Apenas leitura. Requer RSAT/GroupPolicy e permissões de consulta.
# Não cria, modifica nem vincula políticas.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if (-not (Get-Module -ListAvailable -Name GroupPolicy)) {
    throw 'Módulo GroupPolicy não encontrado. Instale o RSAT apropriado.'
}
Import-Module GroupPolicy
Get-GPO -All |
    Select-Object DisplayName, Id, GpoStatus, CreationTime, ModificationTime |
    Sort-Object DisplayName |
    Format-Table -AutoSize
