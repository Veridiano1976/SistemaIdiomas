from bd import *
from usuario import *
from config import *

def acesso(usuario):
	sair = False
	while not sair:
		if usuario["tipo"] == "aluno":
			print("\nBem vindo aluno "+usuario["nome"])
			print("1) Cadastrar idiomas\n")
			print("2) Cadastrar horario e dia\n")
			print("3) Cadastrar cidade e estado\n")
			print("4) Mostrar seus dados\n")
			print("5) Encerrar sessão\n")
			escolha = int(input())
			if escolha == 1:
				cadastrarIdiomas(usuario)
			elif escolha == 2:
				cadastrarHorarios(usuario)
				cadastrarDias(usuario)
			elif escolha == 3:
				cadastrarCidade(usuario)
			elif escolha == 4:
				mostrarUsuario(usuario)
			elif escolha == 5:
				sair = True
			else:
				print("Opcao invalida\n")
		else:
			print("\nBem-vindo professor "+usuario["nome"])
			print("1) Cadastrar notas\n")
			print("2) Cadastrar faltas\n")
			print("3) Cadastrar disciplina\n")
			print("4) Mostrar seus dados\n")
			print("5) Encerrar sessão\n")
			escolha = int(input())
			if escolha == 1:
				cadastrarNotas()
			elif escolha == 2:
				cadastrarFaltas()
			elif escolha == 3:
				cadastrarDisciplinas(usuario)
			elif escolha == 4:
				mostrarUsuario(usuario)
			elif escolha == 5:
				sair = True
			else:
				print("Opcao invalida\n")

def main():
	sair = False
	while not sair:
		print("\nBem vindo ao Sistema de Idiomas!\n")
		print("1) Para realizar um novo cadastro\n")
		print("2) Para fazer login no sistema\n")
		print("3) Para sair\n")
		escolha = int(input())
		if escolha == 1:
			cadastrarUsuario()
		elif escolha == 2:
			nomeUsuario = input("Digite o nome de usuario\n")
			senha = input("Digite sua senha\n")
			if login(nomeUsuario, senha):
				usuarioAtual = buscarUsuario(nomeUsuario)
				acesso(usuarioAtual)
		elif escolha == 3:
			sair = True
		else:
			print("Opcao invalida\n")

main()



