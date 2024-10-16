produto = {'nome': 'caneta_bic', 'preco': 2.50, 
          'importada': 'false', 'estoque': 786}

#por padrão ele percorre as chaves então não há necessidade de colocar "produto.keys()" no lugar de "produto"
for chave in produto:
    print(chave)

for valores in produto.values():
    print(valores)

#para percorrer as chaves e os valores ao mesmo tempo basta fazer o que esta abaixo
for chave, produto in produto.items():
    print(f'{chave}: {produto}')
    
    
# mesmo apos os lacos finalizarem as variaveis ficam disponiveis para o uso, eles estão com o ultimo valor passado
print(f'{chave}: {produto}')
