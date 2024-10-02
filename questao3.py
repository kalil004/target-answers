import json

with open('/Users/ALEKS/Downloads/dados.json', 'r') as file:
    faturamento = json.load(file)

dias_faturados = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_valor = min(dias_faturados)
maior_valor = max(dias_faturados)

media = sum(dias_faturados) / len(dias_faturados)

acima_da_media = sum(1 for dia in dias_faturados if dia > media)

print(f'Menor valor: R$ {menor_valor:.2f}')
print(f'Maior valor: R$ {maior_valor:.2f}')
print(f'Dias acima da média: {acima_da_media:.2f}')



