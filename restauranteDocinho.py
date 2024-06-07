import os
import random

def BuscadorArquivo(RelatorioRestaurante):
  if not os.path.isfile(RelatorioRestaurante):
   with open(RelatorioRestaurante, w) as arquivo:
    arquivo.write("numeroPedido;prato;TempoPreparo;Valor\n")
   print(f"Arquivo{RelatorioRestaurante}criado")
   return False
  return True

def gerar_numero_pedido(RelatorioRestaurante):
  numero_pedido = random.randint(1000, 9999)
  if not BuscadorArquivo(RelatorioRestaurante):
    return numero_pedido
  with open(RelatorioRestaurante, 'r') as arquivo:
        linhas = arquivo.readlines()
        numeros_existentes = {linha.split(';')[0] for linha in linhas[1:]} 
  while str(numero_pedido) in numeros_existentes:
        numero_pedido = random.randint(1000, 9999)
  return numero_pedido

def RegistraDados(RelatorioRestaurante, numeroPedido, prato, TempoPreparo, Valor):
  if not BuscadorArquivo(RelatorioRestaurante):
   return
  with open(RelatorioRestaurante, "a") as arquivo:
   arquivo.write(f"{numeroPedido};{prato};{TempoPreparo};{Valor}\n")


def ListaPedidos(RelatorioRestaurante):
  if not BuscadorArquivo(RelatorioRestaurante):
   return
  with open(RelatorioRestaurante, "r") as arquivo:
   line = arquivo.readlines()
   print(f"{'N° pedido'>15};{'Prato'>20};{'Tempo de preparo'>15};{'valor'>10}")
   print("-" * 60)
   for line in lines[1:]:
    numero_pedido, prato, TempoPreparo, Valor = line.strip().split(';')
    print(f"{numero_pedido:>15} {prato:>20} {TempoPreparo:>15} {Valor:>10}")
   print(F"\nTotal de itens cadastrato: {len(linhas) - 1}")
   if len(linhas) > 1:
    valor_total = [float(linha.strip().split(';')[3]) for line in lines[1:]]
    print(f"Valor total do pedido: R${sum(valor_total):.2f}")

def AlterarPedido(RelatorioRestaurante, line_num, prato=None, TempoPreparo=None, Valor=None):
  if not BuscadorArquivo(RelatorioRestaurante):
   return
   with open(RelatorioRestaurante, "r") as arquivo:
    lines= arquivo.readlines()
   if line_num < 1 or line_num >= len(lines):
    print("Numero de linha invalida")
    return
   data = lines[line_num].strip().split(';')
   


def ExcluirRegistro(RelatorioRestaurante):

def TrasferirPedido(RelatorioRestaurante):

 def menu():
  print("----------Resturante Docinho------------")
  print("| 1°----- Registro de Pedido-----------|")
  print("| 2°----- Lista de pedidos  -----------|")
  print("| 3°----- Alterar Pedido    -----------|")
  print("| 4°----- Cancelar Pedido   -----------|")
  print("| 5°----- Trasferir Pedido  -----------|")
  print("| 6°----- Trasferir Pedido  -----------|")
  print("----------------------------------------")