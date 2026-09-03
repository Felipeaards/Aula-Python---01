#Trabalhando com textos

#Texto em Python pode ser com àspas ou àspas duplas
nome = "Felipe"
curso = "ADS"
idade = input("Digite sua idade:")
print(nome, curso)

#Juntar ou concatenar podemos usar o "+"
print("Nome: " + nome + " Curso: " + curso)

#Colocamos o "f" no começo para dizer que tudo em seguida deve ser formatado como string
# f-string (format string)
#Dentro de um texto formatado com o "f", podemos usar "{}" para chamar uma variável
print(f"Nome: {nome} Curso: {curso}")

#Quebra de linhas = \n
print(f"Nome: {nome}\nCurso: {curso}\nIdade: {idade}")

#Usando àspas dentro do texto
print('Nome '+nome+' "Curso"'+ curso)

#Tabulação (TAB) = \t
print("Nome\tFelipe\tAugusto\t\t\t\t\t\t hehehe")