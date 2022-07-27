from unittest import TestCase
import sys
sys.path.insert(0, '..')
from conexaoDB import *
BD = "TestBD.db"
class MockBD(TestCase):
     @classmethod
     def setUpClass(cls):
         con = conectar(BD)
         cursor = con.cursor()

        
         query_criar_tabela_disciplina = """CREATE TABLE "Disciplina" (
                        "ID"	INTEGER,
                        "Nome"	TEXT NOT NULL,
                        PRIMARY KEY("ID")
                )"""
         query_criar_tabela_aluno = """CREATE TABLE "Aluno" (
                        "ID"	INTEGER,
                        "Nome"	TEXT NOT NULL,
                        PRIMARY KEY("ID")
                )"""
         query_criar_tabela_turma = """CREATE TABLE "Turma" (
                        "ID"	INTEGER,
                        "Nome"	TEXT NOT NULL,
                        "ID_Disciplina"	INTEGER,
                        PRIMARY KEY("ID"),
                        FOREIGN KEY("ID_Disciplina") REFERENCES "Disciplina"("ID")
                )"""                                  
         query_criar_tabela_matricula = """CREATE TABLE "Matricula" (
                        "ID" INTEGER,
                        "ID_Aluno" INTEGER,
                        "ID_Turma" INTEGER,
                        PRIMARY KEY("ID"),
                        FOREIGN KEY("ID_Turma") REFERENCES "Turma"("ID"),
                        FOREIGN KEY("ID_Aluno") REFERENCES "Aluno"("ID")
                )"""                 
                          
         try:

             cursor.execute(query_criar_tabela_disciplina)
             cursor.execute(query_criar_tabela_aluno)
             cursor.execute(query_criar_tabela_turma)
             cursor.execute(query_criar_tabela_matricula)
             con.commit()
         except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
         else:
            print("Criação das tabelas: OK")
         
         query_inserir_disciplina = """INSERT INTO Disciplina (id, nome) VALUES
                 (1, "Matematica"),
                 (2, "Geografia"),
                 (3, "Português"),
                 (4, "Historia")"""

         query_inserir_aluno = """INSERT INTO Aluno (id, nome) VALUES
                 (1, "Antonio"),
                 (2, "José"),
                 (3, "Maria"),
                 (4, "Carla"),
                 (5, "Carlos"),
                 (6, "Francisco"),
                 (7, "Henrique"),
                 (8, "Frederico")"""

         query_inserir_turma = """INSERT INTO Turma (id, nome, id_disciplina) VALUES
                 (1, "5ª série", 2),
                 (2, "6ª serie", 1),
                 (3, "7ª série", 3),
                 (4, "6ª serie", 2)"""
         query_inserir_matricula = """INSERT INTO Matricula (id, id_aluno, id_turma) VALUES
                 (1, 1, 4),
                 (2, 6, 3),
                 (3, 4, 1),
                 (4, 3, 3),
                 (5, 2, 3),
                 (6, 5, 1),
                 (7, 7, 4),
                 (8, 3, 2),
                 (9, 1, 1),
                 (10, 8, 1),
                 (11, 7, 2),
                 (12, 7, 3),
                 (13, 1, 3),
                 (14, 8, 3),
                 (15, 3, 4),
                 (16, 3, 1),
                 (17, 4, 3)"""
         try:
             cursor.execute(query_inserir_disciplina)
             cursor.execute(query_inserir_aluno)
             cursor.execute(query_inserir_turma)
             cursor.execute(query_inserir_matricula)
             con.commit()
         except sqlite3.Error as error:
             print("Erro na inserção de dados:", error)
         else:
             print("Inserção dos dados: OK")
         cursor.close()
         desconectar(con)
         testconfig ={
         'bd': BD
         }
         cls.mock_db_config = testconfig
     @classmethod
     def tearDownClass(cls):
         print("TearDown")
         con = conectar(BD)
         cursor = con.cursor()
         try:
             cursor.execute("DROP TABLE aluno")
             cursor.execute("DROP TABLE turma")
             cursor.execute("DROP TABLE disciplina")
             cursor.execute("DROP TABLE matricula")
             con.commit()
             cursor.close()
             print("Removeu os dados das tabelas.")
         except sqlite3.Error as error:
             print("Banco de dados não existe. Erro na remoção do BD.", error)
         finally:
             desconectar(con)

