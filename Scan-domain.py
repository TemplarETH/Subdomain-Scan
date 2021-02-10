from os import path
import requests
import argparse
import sys

#Definiendo valores parse para el objetivo y la base de busqueda
valor = argparse.ArgumentParser()
valor.add_argument('-D','--Dominio',help="Dominio objetivo",)
valor.add_argument('-sD',help="Archivo origen de subdominios")


dominio = valor.parse_args()

#Si existe un dominio definido, se ejecuta el script
if dominio.Dominio:
#Si existe una base de busqueda, se ejecuta el script
	if path.exists(dominio.sD):
		lista_dominios = open(dominio.sD,'r')
		lista_dominios = lista_dominios.read().split('\n')
		for sub_dom in lista_dominios:
			#Definiendo url
			url = 'http://{}.{}'.format(sub_dom,dominio.Dominio)			
			try:
				#Comprobando conexión a url
				requests.get(url)			
				print("Respuesta desde: {}".format(url))
				salida = open("Subdominios_{}.txt".format(dominio.Dominio),'a')
				salida.write(url+'\n')
				salida.close()
			except requests.ConnectionError:
			#En caso de error, continue ejecutando el ciclo			
				#print("No hay respuesta desde {}".format(url))
				pass
	else:
		print("Seleccione lista de subdominios")	
else:
	print("Ingrese dominio valido")
lista_dominios.close()
sys.exit()

