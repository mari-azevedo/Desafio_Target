# 5) Escreva um programa que inverta os caracteres de um string.
string = "Desafio Target!"
listaval = [j for j in string]

print("String invertida com slicing: ",*listaval[::-1], sep="")

def com_loop(s):
  tamanho = len(s)
  string_invertida = ""

# range(start, stop, step)
  # start: início da sequência (opcional, padrão é 0)
  # stop: fim da sequência (obrigatório)
  # step: passo da sequência (opcional, padrão é 1)
  
  for i in range(tamanho - 1, -1, -1):
    string_invertida += s[i]

  return string_invertida

resultado = com_loop(string)

print("String invertida com loop:",resultado)
