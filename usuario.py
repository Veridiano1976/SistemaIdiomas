from bd import *
from config import *

def cadastrarIdiomas(usuario):
	for c,v in idiomasDisponiveis.items():
		print("Digite "+str(c)+" para escolher "+v)
	escolha = int(input())
	if escolha in idiomasDisponiveis.keys():
		if usuario["idiomas"] == "":
			usuario["idiomas"] = idiomasDisponiveis[escolha]
		elif idiomasDisponiveis[escolha] in usuario["idiomas"]:
			print("Idioma ja cadastrado\n")
			return None
		else:
			idiomasAtuais = usuario["idiomas"] + ", " +idiomasDisponiveis[escolha]
			usuario["idiomas"] = idiomasAtuais
	else:
		print("Opcao invalida\n")
		return None

	salvarUsuario(usuario)
	print("Idioma cadastrado com sucesso\n")

def cadastrarHorarios(usuario):
	for c,v in horariosDisponiveis.items():
		print("Digite "+str(c)+" para escolher "+v)
	escolha = int(input())
	if escolha in horariosDisponiveis.keys():
		if usuario["horarios"] == "":
			usuario["horarios"] = horariosDisponiveis[escolha]
		elif horariosDisponiveis[escolha] in usuario["horarios"]:
			print("Horario ja cadastrado\n")
			return None
		else:
			horariosAtuais = usuario["horarios"] + ", " +horariosDisponiveis[escolha]
			usuario["horarios"] = horariosAtuais
	else:
		print("Opcao invalida\n")
		return None

	salvarUsuario(usuario)
	print("Horario cadastrado com sucesso\n")

def cadastrarDias(usuario):
	for c,v in diasDisponiveis.items():
		print("Digite "+str(c)+" para escolher "+v)
	escolha = int(input())
	if escolha in diasDisponiveis.keys():
		if usuario["dias"] == "":
			usuario["dias"] = diasDisponiveis[escolha]
		elif diasDisponiveis[escolha] in usuario["dias"]:
			print("Dia ja cadastrado\n")
			return None
		else:
			diasAtuais = usuario["dias"]+", "+diasDisponiveis[escolha]
			usuario["dias"] = diasAtuais
	else:
		print("Opcao invalida\n")
		return None

	salvarUsuario(usuario)
	print("Dia cadastrado com sucesso\n")

def cadastrarCidade(usuario):
	for c,v in cidadesDisponiveis.items():
		print("Digite "+str(c)+" para escolher "+v)
	escolha = int(input())
	if escolha in cidadesDisponiveis.keys():
		usuario["cidade"] = cidadesDisponiveis[escolha]

	salvarUsuario(usuario)
	print("Cidade cadastrada com sucesso\n")

def cadastrarNotas():
	print("Escolha o aluno que deseja cadastrar a nota. Alunos disponíveis:\n")
	print(listarAlunos())
	escolhido = input()
	nota = input("Digite a nota\n")
	usuario = buscarPorNome(escolhido)
	if usuario != None:
		if usuario["notas"] == "":
			usuario["notas"] = nota
		else:
			notasAtuais = usuario["notas"]+", "+nota
			usuario["notas"] = notasAtuais
	else:
		print("Usuario nao encontrado! Favor, considerar letras maiusculas e minusculas\n")
		return None
	
	salvarUsuario(usuario)
	print("Nota cadastrada com sucesso\n")

def cadastrarFaltas():
	print("Escolha o aluno que deseja cadastrar a falta. Alunos disponíveis:\n")
	print(listarAlunos())
	escolhido = input()
	usuario = buscarPorNome(escolhido)
	if usuario != None:
		quantidade = int(input("Digite a quantidade de faltas\n"))
		if usuario["faltas"] == "":
			usuario["faltas"] = str(quantidade)
		else:
			faltasAtuais = int(usuario["faltas"])+quantidade
			usuario["faltas"] = str(faltasAtuais)
	else:
		print("Usuario nao encontrado! Favor, considerar letras maiusculas e minusculas\n")
		return None
	
	salvarUsuario(usuario)
	print("Falta(s) cadastrada com sucesso\n")

def cadastrarDisciplinas(usuario):
	for c,v in idiomasDisponiveis.items():
		print("Digite "+str(c)+" para escolher "+v)
	escolha = int(input())
	if escolha in idiomasDisponiveis.keys():
		if usuario["disciplinas"] == "":
			usuario["disciplinas"] = idiomasDisponiveis[escolha]
		elif idiomasDisponiveis[escolha] in usuario["disciplinas"]:
			print("Disciplina ja cadastrada\n")
			return None
		else:
			disciplinasAtuais = usuario["disciplinas"]+", "+idiomasDisponiveis[escolha]
			usuario["disciplinas"] = disciplinasAtuais
	else:
		print("Opcao invalida\n")
		return None

	salvarUsuario(usuario)
	print("Disciplina cadastrada com sucesso\n")

def mostrarUsuario(usuario):
	for key in usuario.keys():
		if usuario[key] != "":
			print(str(key)+": "+usuario[key])
