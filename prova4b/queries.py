
from conexaoDB import *

def ler_todos_alunos(bd):
     return ler_bd(bd, "SELECT * FROM Aluno")

def ler_todas_Disciplinas(bd):
     return ler_bd(bd, "SELECT * FROM Disciplina")

def ler_aluno_nome(bd, nome):
    query = "SELECT * FROM Aluno WHERE nome = ?"  
    return ler_bd(bd, query, (nome,))
