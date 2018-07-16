import os
from config import *

def salvarUsuario(usuario):
	arq = open(caminho+usuario["login"], "w")
	for key in usuario.keys():
		arq.write(usuario[key])
		arq.write("\n")


def buscarUsuario(login):
	arq = open(caminho+login, "r")
	dados = arq.read()
	listaDados = dados.split("\n")
	if "aluno" in dados:
		usuario = modeloAluno
	else:
		usuario = modeloProfessor
	cont = 0
	for key in usuario.keys():
		usuario[key] = listaDados[cont]
		cont+=1
	return usuario

def usuarioExiste(nomeUsuario):
	try:
		arquivo = open(caminho+nomeUsuario, "r")
		return True
	except FileNotFoundError:
		return False

def pegarSenha(nomeUsuario):
	arquivo = open(caminho+nomeUsuario, "r")
	dados = buscarUsuario(nomeUsuario)
	return dados["senha"]

def cadastrarUsuario():
	if not os.path.exists(caminho):
		os.makedirs(caminho)
	usuario = criarUsuario()
	if usuarioExiste(usuario["login"]):
		print("Login ja cadastrado\n")
		return False

	if usuario["tipo"] == "aluno":
		novoUsuario = modeloAluno
	else:
		novoUsuario = modeloProfessor

	for key in novoUsuario.keys():
		if key in usuario:
			novoUsuario[key] = usuario[key]
	salvarUsuario(novoUsuario)
	return novoUsuario

def login(nomeUsuario, senha):
	if usuarioExiste(nomeUsuario) == False:
		print("Usuário não cadastrado")
		return False

	senhaCorreta = pegarSenha(nomeUsuario)
	if senha != senhaCorreta:
		print("Senha incorreta")
		return False

	return True

def criarUsuario():
	usuario = {}
	usuario["nome"] = input("Digite seu nome\n")
	usuario["email"] = input("Digite seu email\n")
	usuario["login"] = input("Digite seu login\n")
	usuario["senha"] = input("Digite sua senha\n")
	opcoes = ["aluno", "professor"]
	tipo = input("Vc é um professor ou um aluno?\n")
	while tipo not in opcoes:
		tipo = input("Vc é um professor ou um aluno?\n")
	usuario["tipo"] = tipo
	return usuario

def listarAlunos():
	arquivos = os.listdir(caminho)
	alunos = []
	for i in range(len(arquivos)):
		atual = buscarUsuario(arquivos[i])
		if atual["tipo"] == "aluno":
			alunos.append(atual["nome"])

	return alunos

def listarProfessores():
	arquivos = os.listdir(caminho)
	professores = []
	for i in range(len(arquivos)):
		atual = buscarUsuario(arquivos[i])
		if atual["tipo"] == "professor":
			professores.append(atual["nome"])

	return professores

def buscarPorNome(nome):
	arquivos = os.listdir(caminho)
	for i in range(len(arquivos)):
		atual = buscarUsuario(arquivos[i])
		if atual["nome"] == nome:
			return atual


