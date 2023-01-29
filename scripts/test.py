''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
N = int(input())

resultados = []
while(N > 0):
  entrada = input()
  A = entrada.split(" ")[0][::-1]
  B = entrada.split(" ")[1][::-1]  
  
  tamanho_B = len(B)
  resultado = "encaixa"
  
  if len(A) < tamanho_B:
    resultado = "nao encaixa"
  else:
    iterador = 0
    for numero in B:
      if A[iterador] != numero:
        resultado = "nao encaixa"
        break
      iterador += 1
  resultados.append(resultado)
  N -= 1
for valor in resultados:
  print(valor)