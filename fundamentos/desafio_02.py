# tv 50 os dois trabalhdo feitos
# tv 32 um trabalho feito
# sorvete um trabalho feito
# saudavel nenhum trabalho feito

trabalho_terca = True
trabalho_quinta = True

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
saudavel = not sorvete

print("tv 50 {} tv 32 {} sorvete {} saudavel {}" .format(tv_50, tv_32, sorvete, saudavel))

# sobre o format
# nele é possivel colocar o numeros, textos e variaveis, basta colcoar as chaves dentro das aspas de um print
# tambem é possivel colcoar ordem, basta colcocar uma numeração que inicia do zero dentro das chaves
print("{} + {} = {}" .format(1, 2, "tres"))
