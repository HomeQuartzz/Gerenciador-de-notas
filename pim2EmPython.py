import re
import unicodedata

# ==========================
# Classe que representa o aluno
# ==========================
class Aluno:
    def __init__(self, nome, turma, notas, disciplina_nome):
        self.nome = nome
        self.turma = turma
        self.notas = notas
        self.disciplina = disciplina_nome
        self.media = self.calcular_media()
        self.situacao = self.definir_situacao()

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def definir_situacao(self):
        return "Aprovado" if self.media >= 6.0 else "Reprovado"

    def __str__(self):
        notas_formatadas = " | ".join(f"{nota:.1f}" for nota in self.notas)
        return (
            f"Aluno: {self.nome}\n"
            f"Turma: {self.turma}\n"
            f"Disciplina: {self.disciplina}\n"
            f"Notas: {notas_formatadas}\n"
            f"Media: {self.media:.2f}\n"
            f"Situacao: {self.situacao}\n"
            "---------------------------------------"
        )


# ==========================
# Classe Fila (estrutura simples para alunos)
# ==========================
class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def listar(self):
        return self.itens


# ==========================
# Classe Disciplina
# ==========================
class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.fila_alunos = Fila()

    def adicionar_aluno(self, nome, turma, notas, todos_os_alunos):
        aluno = Aluno(nome, turma, notas, self.nome)
        self.fila_alunos.enfileirar(aluno)
        todos_os_alunos.append(aluno)  # adiciona na lista global também

    def listar_alunos(self):
        if self.fila_alunos.esta_vazia():
            print("Nenhum aluno cadastrado.")
        else:
            print(f"\nAlunos da disciplina: {self.nome}")
            for aluno in self.fila_alunos.listar():
                print(aluno)

    def gerar_relatorio(self):
        alunos = self.fila_alunos.listar()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return

        # Agrupar alunos por turma
        grupos_por_turma = {}
        for aluno in alunos:
            grupos_por_turma.setdefault(aluno.turma, []).append(aluno)

        total_alunos = len(alunos)
        media_geral = sum(a.media for a in alunos) / total_alunos
        aprovados = sum(1 for a in alunos if a.situacao == "Aprovado")
        reprovados = total_alunos - aprovados

        nome_sem_acento = ''.join(
            c for c in unicodedata.normalize('NFD', self.nome)
            if unicodedata.category(c) != 'Mn'
        )
        nome_arquivo = f"relatorio_{nome_sem_acento.replace(' ', '_')}.txt"

        with open(nome_arquivo, "w", encoding="ascii", errors="ignore") as f:
            f.write(f"Relatorio da disciplina: {self.nome}\n")
            f.write("---------------------------------------\n")
            f.write(f"Total de alunos: {total_alunos}\n")
            f.write(f"Media geral (todas as turmas): {media_geral:.2f}\n")
            f.write(f"Aprovados: {aprovados}\n")
            f.write(f"Reprovados: {reprovados}\n")
            f.write("---------------------------------------\n\n")

            for turma, lista in sorted(grupos_por_turma.items()):
                media_turma = sum(a.media for a in lista) / len(lista)
                f.write(f"TURMA {turma}\n")
                f.write(f"Media geral da turma {turma}: {media_turma:.2f}\n")
                f.write("-----------------------\n")
                for aluno in lista:
                    notas_str = " | ".join(f"{n:.1f}" for n in aluno.notas)
                    f.write(f"Nome: {aluno.nome}\n")
                    f.write(f"Notas: {notas_str}\n")
                    f.write(f"Media: {aluno.media:.2f}\n")
                    f.write(f"Situacao: {aluno.situacao}\n")
                    f.write("-----------------------\n")
                f.write("\n")

        print(f"\nRelatorio salvo em: {nome_arquivo}\n")


# ==========================
# Relatório Geral
# ==========================
def gerar_relatorio_geral(todos_os_alunos):
    if not todos_os_alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    # Agrupar por disciplina e turma
    grupos = {}
    for aluno in todos_os_alunos:
        grupos.setdefault(aluno.disciplina, {}).setdefault(aluno.turma, []).append(aluno)

    nome_arquivo = "relatorio_geral_todas_as_disciplinas.txt"

    with open(nome_arquivo, "w", encoding="ascii", errors="ignore") as f:
        f.write("RELATORIO GERAL DE TODAS AS DISCIPLINAS\n")
        f.write("=======================================\n\n")

        for disciplina, turmas in sorted(grupos.items()):
            f.write(f"DISCIPLINA: {disciplina}\n")
            f.write("---------------------------------------\n")
            for turma, lista in sorted(turmas.items()):
                media_turma = sum(a.media for a in lista) / len(lista)
                f.write(f"TURMA {turma} - Media geral: {media_turma:.2f}\n")
                f.write("-----------------------\n")
                for aluno in lista:
                    notas_str = " | ".join(f"{n:.1f}" for n in aluno.notas)
                    f.write(f"Nome: {aluno.nome}\n")
                    f.write(f"Notas: {notas_str}\n")
                    f.write(f"Media: {aluno.media:.2f}\n")
                    f.write(f"Situacao: {aluno.situacao}\n")
                    f.write("-----------------------\n")
                f.write("\n")
            f.write("=======================================\n\n")

    print(f"\nRelatorio geral salvo em: {nome_arquivo}\n")


# ==========================
# Menus
# ==========================
def menu_principal():
    print("\n===== Sistema de cadastro de alunos - Ensino Fundamental =====")
    print("1. Escolher/entrar em uma disciplina")
    print("9. Gerar relatorio geral de todas as disciplinas")
    print("0. Sair")


def menu_disciplina(nome):
    print(f"\n--- Disciplina: {nome} ---")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Gerar relatorio (.txt)")
    print("0. Voltar")


# ==========================
# Função principal
# ==========================
def main():
    disciplinas = {}
    todos_os_alunos = []

    opcoes_disciplinas = {
        "1": "Lingua Portuguesa",
        "2": "Matematica",
        "3": "Ciencias",
        "4": "Historia",
        "5": "Geografia",
        "6": "Arte",
        "7": "Educacao Fisica",
        "8": "Lingua Inglesa"
    }

    while True:
        menu_principal()
        opcao = input("Escolha uma opcao: ")

        if opcao == "0":
            print("Saindo do sistema...")
            break

        elif opcao == "1":
            print("\nEscolha a disciplina:")
            for chave, nome in opcoes_disciplinas.items():
                print(f"{chave}. {nome}")

            escolha = input("Digite o numero da disciplina: ").strip()

            if escolha not in opcoes_disciplinas:
                print("Opcao invalida. Tente de novo.")
                continue

            nome_disc = opcoes_disciplinas[escolha]

            if nome_disc not in disciplinas:
                disciplinas[nome_disc] = Disciplina(nome_disc)

            disciplina = disciplinas[nome_disc]

            while True:
                menu_disciplina(nome_disc)
                subopcao = input("Escolha uma opcao: ")

                if subopcao == "0":
                    break

                elif subopcao == "1":
                    # Cadastro de aluno
                    while True:
                        nome = input("Digite o nome do aluno: ").strip()
                        if nome == "":
                            print("Nome nao pode estar em branco.")
                            continue
                        if nome.replace(" ", "").isalpha():
                            break
                        else:
                            print("Nome invalido. Use apenas letras e espacos.")
                            continue

                    while True:
                        turma = input("Turma (ex: 9A, 9B, 6A): ").strip().upper()
                        if turma == "":
                            print("Turma nao pode estar em branco.")
                            continue
                        if re.fullmatch(r'(?:[1-9]|10)[A-Z]', turma):
                            break
                        else:
                            print("Formato invalido. Use numero da serie seguido de uma letra (ex: 9A, 6C).")
                            continue

                    while True:
                        print("\nDigite as 4 notas separadas por espaco (ex: 7.5 8.0 9.2 6.5)")
                        notas_input = input("Notas: ").replace(",", ".").strip().split()
                        if len(notas_input) != 4:
                            print("Tem que digitar exatamente 4 notas.")
                            continue
                        try:
                            notas = list(map(float, notas_input))
                            if any(n < 0 or n > 10 for n in notas):
                                print("Todas as notas devem estar entre 0 e 10.")
                                continue
                        except ValueError:
                            print("Notas invalidas! Use apenas numeros (ex: 7.5).")
                            continue
                        break

                    disciplina.adicionar_aluno(nome, turma, notas, todos_os_alunos)
                    print("Aluno cadastrado com sucesso!")

                elif subopcao == "2":
                    disciplina.listar_alunos()

                elif subopcao == "3":
                    disciplina.gerar_relatorio()

                else:
                    print("Opcao invalida. Tente de novo.")

        elif opcao == "9":
            gerar_relatorio_geral(todos_os_alunos)

        else:
            print("Opcao invalida. Tente de novo.")


# ==========================
# Executar o programa
# ==========================
if __name__ == "__main__":
    main()
