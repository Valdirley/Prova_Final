from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries import *
class TestDB(MockBD):
# def test_select_all(self):
#
#     retorno_esperado = [(1, 'Antonio'),
#                 (2, 'José'),
#                 (3, 'Maria'),
#                 (4, 'Carla'),
#                 (5, 'Carlos'),
#                 (6, 'Francisco'),
#                 (7, 'Henrique'),
#                 (8, 'Frederico')]
#     self.assertEqual(ler_todos_alunos(self.mock_db_config.get('bd')),
#retorno_esperado)

# def test_select_all(self):

#     retorno_esperado = [
#                (1, 'Matematica'),
#                (2, 'Geografia'),
#                (3, 'Português'),
#                (4, 'Historia')]
#     self.assertEqual(ler_todas_Disciplinas(self.mock_db_config.get('bd')),
#retorno_esperado)




 def test_filtro_nome(self):
     retorno_esperado =  [4, 'Carla']
     self.assertEqual(ler_aluno_nome(self.mock_db_config.get('bd'), 'Carla'), 
     retorno_esperado)
     
