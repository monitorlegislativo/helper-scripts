# -*- coding: utf-8 -*-
import re

numeros = re.compile(r"\n[0-9]{1,}\n")
arquivo = open("regimento-interno-2013-RC291C.txt", "r").read()

pontofinal = re.compile(r'(.{1,}\.)\n')
pontovirgula = re.compile(r'(.{1,};)\n')
doisponto = re.compile(r'(.{1,}:)\n')
maiusculas = re.compile(r'([A-Z]{1,})\n')
parenteses = re.compile(r'(\(.*\))\n')


arquivo = arquivo.replace("REGIMENTO INTERNO DA CÂMARA MUNICIPAL DE SÃO PAULO", "")
arquivo = re.sub(numeros, "", arquivo)
arquivo = re.sub(parenteses, r"\1\n\n", arquivo)
arquivo = re.sub(pontofinal, r"\1\n\n", arquivo)
arquivo = re.sub(pontovirgula, r"\1\n\n", arquivo)
arquivo = re.sub(doisponto, r"\1\n\n", arquivo)
arquivo = re.sub(maiusculas, r"\1\n\n", arquivo)
arquivo = re.sub(r"(.{1,})\n", r"\1 ", arquivo)
arquivo = re.sub(r"\n{1,}", "\n", arquivo)
arquivo = arquivo.replace("\n", "\n\n")

arquivo2 = open('regimento-novo.txt', 'w')
arquivo2.write(arquivo)
arquivo2.close()