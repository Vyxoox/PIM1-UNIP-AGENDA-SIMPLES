import calendar
from datetime import datetime

#dicionário para armazenar a agenda
agenda = {}

#função1 adicionar aula
def adicionar_aula(professor, data, disciplina, conteudo, horario):
    """
    Addicionar uma aula à agenda

    parametros:
    -professor: nome do professor
    data: data no formato DD/MM
    disciplina: nome da matéria
    conteudo: conteúdo da aula
    horario: horário da aula
    """

    #se não existir professor na agenda ele cria
    if professor not in agenda:
        agenda[professor] = {}

    #se a data não existir pro professor ele cria
    if data not in agenda[professor]:
        agenda[professor][data] = []

    #criar o dicionário da aula
    aula = {
        "disciplina": disciplina,
        "conteudo": conteudo,
        "horario": horario
    }

    #adicionar aula à lista
    agenda[professor][data].append(aula)
    print(f"Aula adicionada! {disciplina} - {professor} em {data}")



#função2 remover aula
def remover_aula(professor, data, indice_aula):
    """
    Remover uma aula da agenda

    Parâmetros:
    professor:  nome do professor
    data: data no formato DD/MM
    indice_aula: posição da aula na lista(0, 1, 2, ...)
    """

    #verificar se professor existe
    if professor not in agenda:
        print("Professor não encontrado!")
        return

    #verificar se data existe para esse professor
    if data not in agenda[professor]:
        print("Nenhuma aula nessa data!")
        return

    #verificar se o indice é válido
    if indice_aula < 0 or indice_aula >= len(agenda[professor][data]):
        print("Aula não encontrada!")
        return

    #remove aula
    aula_removida = agenda[professor][data].pop(indice_aula)
    print(f"Aula removida! {aula_removida['discplina']} - {professor}")


#função3 lista aulas por dia
def listar_aulas_dia(data):
    """
    Lista todas as aulas de um dia específico (de todos os professores)

    Parâmetros:
    data: data no formato DD/MM
    """

    encontrou = False

    #percorrer cada professor na agenda
    for professor in agenda:
        #verificar se o professor tem aula no dia
        if data in agenda[professor]:
            encontrou = True
            print(f"{data} -  professor: {professor}")

            #percorre cada aula do professor nessa data
            for i, aula in enumerate(agenda[professor][data]):
                print(f"  {i+1} - {aula['disciplina']} - {aula['conteudo']} às {aula['horario']}")

    if not encontrou:
        print(f"Nenhuma aula nessa data!")


#função4 listar aula por professor
def listar_aulas_professor(professor):
    """
    Lista todas as aulas de um professor específico

    Parâmetro:
    - professor: nome do professor
    """

    # Verificar se professor existe
    if professor not in agenda:
        print(f"❌ Professor {professor} não encontrado!")
        return

    print(f"\n👨‍🏫 Aulas do Professor: {professor}")
    print("=" * 50)

    # Percorrer cada data desse professor
    for data in agenda[professor]:
        print(f"\n📅 {data}:")

        # Percorrer cada aula nessa data
        for i, aula in enumerate(agenda[professor][data]):
            print(f"  {i + 1}. {aula['disciplina']} - {aula['conteudo']} às {aula['horario']}")


#função5 mostrar o mês completo
def mostrar_mes(ano, mes):
    """
    Mostra todas as aulas do mês em formato de calendário

    Parâmetros:
    - ano: ex: 2024
    - mes: ex: 4 (abril)
    """

    # Pegar a matriz do calendário
    cal = calendar.monthcalendar(ano, mes)

    # Nomes dos dias da semana
    dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

    print(f"\n📆 Calendário de {calendar.month_name[mes]} de {ano}")
    print("=" * 70)
    print("  ".join(dias_semana))
    print("-" * 70)

    # Percorrer cada semana
    for semana in cal:
        # Mostrar os dias
        dias_str = ""
        for dia in semana:
            if dia == 0:
                dias_str += "    "  # Dia vazio
            else:
                dias_str += f"{dia:2d}  "
        print(dias_str)

        # Mostrar as aulas abaixo dos dias
        aulas_str = ""
        for dia in semana:
            if dia == 0:
                aulas_str += "     "
            else:
                data_formatada = f"{dia:02d}/{mes:02d}"
                tem_aula = False

                # Verificar se há aula nesse dia
                for professor in agenda:
                    if data_formatada in agenda[professor]:
                        tem_aula = True
                        aulas_str += "* "
                        break

                if not tem_aula:
                    aulas_str += "  "

        print(aulas_str)
        print()


#função6 editar aula já cadastrada
def editar_aula(professor, data, indice_aula, campo, novo_valor):
    """
    Edita uma aula existente

    Parâmetros:
    - professor: nome do professor
    - data: data no formato DD/MM
    - indice_aula: qual aula (0, 1, 2...)
    - campo: qual campo editar ('disciplina', 'conteudo', 'horario')
    - novo_valor: novo valor
    """

    # Verificações
    if professor not in agenda:
        print("❌ Professor não encontrado!")
        return

    if data not in agenda[professor]:
        print("❌ Nenhuma aula nessa data!")
        return

    if indice_aula < 0 or indice_aula >= len(agenda[professor][data]):
        print("❌ Aula não encontrada!")
        return

    if campo not in agenda[professor][data][indice_aula]:
        print("❌ Campo não existe!")
        return

    # Pegar valor antigo
    valor_antigo = agenda[professor][data][indice_aula][campo]

    # Editar
    agenda[professor][data][indice_aula][campo] = novo_valor

    print(f"✅ Aula editada!")
    print(f"  Campo: {campo}")
    print(f"  De: {valor_antigo}")
    print(f"  Para: {novo_valor}")



#função7 MENU PRINCIPAL

def menu():
    """
    Menu principal da agenda
    """

    while True:
        print("\n" + "=" * 50)
        print("📚 AGENDA DE AULAS")
        print("=" * 50)
        print("1. ➕ Adicionar aula")
        print("2. ➖ Remover aula")
        print("3. 📅 Ver aulas de um dia")
        print("4. 👨‍🏫 Ver aulas de um professor")
        print("5. 📆 Ver mês inteiro")
        print("6. ✏️  Editar aula")
        print("7. 🚪 Sair")
        print("=" * 50)

        opcao = input("Escolha uma opção (1-7): ")

        # ESTRUTURA CONDICIONAL: if/elif/else
        if opcao == "1":
            # Adicionar aula
            professor = input("Nome do professor: ")
            data = input("Data (DD/MM): ")
            disciplina = input("Disciplina: ")
            conteudo = input("Conteúdo: ")
            horario = input("Horário (HH:MM): ")
            adicionar_aula(professor, data, disciplina, conteudo, horario)

        elif opcao == "2":
            # Remover aula
            professor = input("Nome do professor: ")
            data = input("Data (DD/MM): ")
            listar_aulas_professor(professor)  # Mostra as aulas dele
            indice = int(input("Número da aula a remover: ")) - 1
            remover_aula(professor, data, indice)

        elif opcao == "3":
            # Ver aulas de um dia
            data = input("Data (DD/MM): ")
            listar_aulas_dia(data)

        elif opcao == "4":
            # Ver aulas de um professor
            professor = input("Nome do professor: ")
            listar_aulas_professor(professor)

        elif opcao == "5":
            # Ver mês inteiro
            ano = int(input("Ano (ex: 2024): "))
            mes = int(input("Mês (1-12): "))
            mostrar_mes(ano, mes)

        elif opcao == "6":
            # Editar aula
            professor = input("Nome do professor: ")
            data = input("Data (DD/MM): ")
            listar_aulas_professor(professor)
            indice = int(input("Número da aula a editar: ")) - 1
            campo = input("Campo a editar (disciplina/conteudo/horario): ")
            novo_valor = input("Novo valor: ")
            editar_aula(professor, data, indice, campo, novo_valor)

        elif opcao == "7":
            print("\n👋 Até logo!")
            break  # Sai do while

        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🚀 INICIANDO AGENDA DE AULAS...")
    print("=" * 60)
    print("\n✅ Programa carregado com sucesso!")
    print("Digite as opções quando o menu aparecer.\n")
    input("Pressione ENTER para começar...")
    menu()