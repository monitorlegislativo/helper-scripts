# -*- coding: utf-8 -*-
import re

'''
Código para limpar o txt produzido pela conversão de um PDF de Lei
(ex. http://www2.camara.sp.gov.br/RegimentoInterno/regimento-interno-2013-RC291C.pdf)
Para converter use o pdftotext do pacote xpdf-utils.
'''

def parse(filename="regimento-interno-2013-RC291C.txt"):
	'''Retorna um novo texto acertando as quebras de linha e removendo o cabeçalho das páginas'''
	arquivo = open(filename, "r").read()

	#Define as regras de regex
	#TODO: Criar uma lista iteravel de regras
	numeros = re.compile(r"\n[0-9]{1,}\n") #numeracao das paginas
	pontofinal = re.compile(r'(.{1,}\.)\n') #linhas termindas em ponto final
	pontovirgula = re.compile(r'(.{1,};)\n') #linhas terminadas em ponto e vírgula
	doisponto = re.compile(r'(.{1,}:)\n') #linhas terminadas em dois pontos
	maiusculas = re.compile(r'([A-Z]{1,})\n') #linhas terminadas maiusculas
	parenteses = re.compile(r'(\(.*\))\n') #linhas terminadas em parentes

	arquivo = arquivo.replace("REGIMENTO INTERNO DA CÂMARA MUNICIPAL DE SÃO PAULO", "") #remove o texto do cabeçalho
	arquivo = re.sub(numeros, "", arquivo) #remove a numeração das paginas
	arquivo = re.sub(parenteses, r"\1\n\n", arquivo) #da uma quebra de linha adicional em caso de parenteses
	arquivo = re.sub(pontofinal, r"\1\n\n", arquivo) #da uma quebra de linha adicional em caso de ponto final
	arquivo = re.sub(pontovirgula, r"\1\n\n", arquivo) #da uma quebra de linha adicional em caso ponto e virgula
	arquivo = re.sub(doisponto, r"\1\n\n", arquivo) #da uma quebra de linha adicional em caso de dois pontos
	arquivo = re.sub(maiusculas, r"\1\n\n", arquivo) #da uma quebra de linha adicional em caso de maiusculas
	arquivo = re.sub(r"(.{1,})\n", r"\1 ", arquivo) #remove uma quebra e transforma em espaço (conecta sentenças no mesmo paragrafo)
	arquivo = re.sub(r"\n{1,}", "\n", arquivo) #remove quebras de linhas extras
	arquivo = arquivo.replace("\n", "\n\n") #recoloca a quebra de linha adicional p/ ter paragrafo no wordpress

	arquivo2 = open('parsed_'+filename, 'w')
	arquivo2.write(arquivo)
	arquivo2.close()