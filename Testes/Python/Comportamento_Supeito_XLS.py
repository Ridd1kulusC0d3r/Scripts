import pandas as pd

# Carregar o arquivo XLS com os dados de vendas
xls_file = 'caminho/do/arquivo.xls'
df = pd.read_excel(xls_file)

# Verificar comportamento suspeito
def verificar_comportamento_suspeito(row):
    if row['valor_venda'] > 10000 and row['quantidade'] > 10:
        return 'Possível fraude'
    else:
        return 'Normal'

# Aplicar a função de verificação em cada linha do DataFrame
df['classificacao'] = df.apply(verificar_comportamento_suspeito, axis=1)

# Salvar o novo DataFrame com a classificação
df.to_excel('dados_classificados.xls', index=False)

print('Dados classificados e salvos com sucesso.')
