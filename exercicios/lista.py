# etapa 1 criar uma lista
Objetos= ['estojo', 'bolsa', 'carteira', 'mesa', 'notebook']
print("Lista de Objetos")
print(Objetos)
print("-"*25)



#2. Adicionando mais um objeto a lista
Objetos.append('ipad')
print(Objetos)
print("objeto adicionada")
print("-"*25)



#3. Acesse o Objeto queesta na 2°posição
print(f'segundo Objeto {Objetos[2]}')
print("-"*25)


#4. Remova um Objetos na lista
Objetos.remove("mesa")
print("objeto removido")


#5. exibindo o tamanho da lista
for objeto in Objetos:
    print(objeto)
print("-"*25)

#6. monstrando todos os itens na lista
for n in range(5):
    print(n)
print("-"*25)


#7. verificando se a cadeira está na lista
if"cadeira" in Objetos:
    Objetos.remove("cadeira")
    print("cadeira removida")
    print("-"*25)
else:
    Objetos.append("cadeira")
    print("cadeira adicionada")
    print("-" * 25)


#8. Ordene a lista em ordem alfabetica
Objetos.sort()
print("Objetos em Ordem")
print("-"*25)



#9. Exiba o primeiro e ultimo numero
primeiros = Objetos[0]
ultimo = Objetos[5]
print(f"primeiro objeto {primeiros}",f"a ultima Objeto {ultimo}")



#10.limpando toda a lista
Objetos.clear()
print("objeto removido")
print("-"*25)

for fruta in Objetos:
    print(fruta)
