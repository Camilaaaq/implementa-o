import os
import datetime


obras = []
artistas = []
estilos_artisticos = []
emprestimos = []
visitas_guiadas = []


def quicksort(lista, key=None):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return quicksort(left, key) + middle + quicksort(right, key)


def cadastrar_obra(titulo, data_criacao, tema, estilo, descricao, tecnica, autor, localizacao):
    obra = {
        "titulo": titulo,
        "data_criacao": data_criacao,
        "tema": tema,
        "estilo": estilo,
        "descricao": descricao,
        "tecnica": tecnica,
        "autor": autor,
        "localizacao": localizacao
    }
    obras.append(obra)

def cadastrar_artista(nome, data_nascimento, local_nascimento, biografia, estilos):
    artista = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "local_nascimento": local_nascimento,
        "biografia": biografia,
        "estilos": estilos
    }
    artistas.append(artista)

def cadastrar_estilo_artistico(denominacao, periodo_influencia, caracteristicas, escola_representativa):
    estilo = {
        "denominacao": denominacao,
        "periodo_influencia": periodo_influencia,
        "caracteristicas": caracteristicas,
        "escola_representativa": escola_representativa
    }
    estilos_artisticos.append(estilo)

def cadastrar_documento(obra, tipo, conteudo):
    obra["documentos"] = obra.get("documentos", [])
    obra["documentos"].append({"tipo": tipo, "conteudo": conteudo})

def cadastrar_pessoa_retratada(obra, nome, biografia):
    obra["pessoas_retratadas"] = obra.get("pessoas_retratadas", [])
    obra["pessoas_retratadas"].append({"nome": nome, "biografia": biografia})


def registrar_emprestimo(obra, periodo, evento, responsavel, tema):
    emprestimo = {
        "obra": obra,
        "periodo": periodo,
        "evento": evento,
        "responsavel": responsavel,
        "tema": tema
    }
    emprestimos.append(emprestimo)


def cadastrar_visita_guiada(tema, descricao, obras_visitadas):
    visita = {
        "tema": tema,
        "descricao": descricao,
        "obras_visitadas": obras_visitadas
    }
    visitas_guiadas.append(visita)


def consultar_obra(titulo):
    for obra in obras:
        if obra["titulo"] == titulo:
            return obra
    return None

def pesquisar_obras(criterio, valor):
    resultados = []
    for obra in obras:
        if valor.lower() in str(obra[criterio]).lower():
            resultados.append(obra)
    return resultados

def visualizar_obra(obra):
    print(f"Título: {obra['titulo']}")
    print(f"Data de Criação: {obra['data_criacao']}")
    print(f"Tema: {obra['tema']}")
    print(f"Estilo: {obra['estilo']}")
    print(f"Descrição: {obra['descricao']}")
    print(f"Técnica: {obra['tecnica']}")
    print(f"Autor: {obra['autor']}")
    print(f"Localização: {obra['localizacao']}")
    if "documentos" in obra:
        print("Documentos Relacionados:")
        for doc in obra["documentos"]:
            print(f"- {doc['tipo']}: {doc['conteudo']}")
    if "pessoas_retratadas" in obra:
        print("Pessoas Retratadas:")
        for pessoa in obra["pessoas_retratadas"]:
            print(f"- {pessoa['nome']}: {pessoa['biografia']}")


def ler_dados_de_arquivo(arquivo):
    with open(arquivo, "r") as f:
        dados = f.read()
    return dados

def gravar_dados_em_arquivo(arquivo, dados):
    with open(arquivo, "w") as f:
        f.write(dados)


cadastrar_obra(
    "Guernica", "1937-05-01", "Guerra", "Cubismo", "Obra-prima do Cubismo", "Óleo sobre tela", "Pablo Picasso", "Sala 1"
)
cadastrar_artista(
    "Pablo Picasso", "1881-10-25", "Málaga, Espanha", "Pintor e escultor espanhol", ["Cubismo"]
)
cadastrar_estilo_artistico(
    "Cubismo", "1907-1919", "Desconstrução da forma em planos geométricos", "Escola de Paris"
)
cadastrar_documento(obras[0], "Carta", "Carta de Picasso sobre a obra")
cadastrar_pessoa_retratada(obras[0], "Francisco Franco", "Ditador espanhol")

obra = consultar_obra("Guernica")
visualizar_obra(obra)

resultados = pesquisar_obras("tema", "Guerra")
for obra in resultados:
    print(obra["titulo"])

gravar_dados_em_arquivo("acervo.txt", str(obras))
dados = ler_dados_de_arquivo("acervo.txt")
print(dados)

def menu_principal():
    print("== Menu Principal ==")
    print("1. Gerenciar Acervo")
    print("2. Gerenciar Empréstimos")
    print("3. Gerenciar Visitas Guiadas")
    print("4. Sair")
    opcao = input("Digite a opção desejada: ")
    return opcao

def menu_acervo():
    print("== Gerenciar Acervo ==")
    print("1. Cadastrar Obra")
    print("2. Cadastrar Artista")
    print("3. Cadastrar Estilo Artístico")
    print("4. Consultar Obra")
    print("5. Pesquisar Obras")
    print("6. Voltar ao Menu Principal")
    opcao = input("Digite a opção desejada: ")
    return opcao

def menu_emprestimos():
    print("== Gerenciar Empréstimos ==")
    print("1. Registrar Empréstimo")
    print("2. Exibir Empréstimos")
    print("3. Voltar ao Menu Principal")
    opcao = input("Digite a opção desejada: ")
    return opcao

def menu_visitas_guiadas():
    print("== Gerenciar Visitas Guiadas ==")
    print("1. Cadastrar Visita Guiada")
    print("2. Exibir Visitas Guiadas")
    print("3. Voltar ao Menu Principal")
    opcao = input("Digite a opção desejada: ")
    return opcao

def main():
    while True:
        opcao = menu_principal()
        if opcao == "1":
            while True:
                opcao_acervo = menu_acervo()
                if opcao_acervo == "1":
                    titulo = input("Digite o título da obra: ")
                    data_criacao = input("Digite a data de criação (AAAA-MM-DD): ")
                    tema = input("Digite o tema da obra: ")
                    estilo = input("Digite o estilo artístico: ")
                    descricao = input("Digite a descrição da obra: ")
                    tecnica = input("Digite a técnica utilizada: ")
                    autor = input("Digite o nome do autor: ")
                    localizacao = input("Digite a localização da obra: ")
                    cadastrar_obra(titulo, data_criacao, tema, estilo, descricao, tecnica, autor, localizacao)
                    print("Obra cadastrada com sucesso!")
                elif opcao_acervo == "2":
                    nome = input("Digite o nome do artista: ")
                    data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
                    local_nascimento = input("Digite o local de nascimento: ")
                    biografia = input("Digite a biografia do artista: ")
                    estilos = input("Digite os estilos artísticos (separados por vírgula): ").split(",")
                    cadastrar_artista(nome, data_nascimento, local_nascimento, biografia, [estilo.strip() for estilo in estilos])
                    print("Artista cadastrado com sucesso!")
                elif opcao_acervo == "3":
                    denominacao = input("Digite a denominação do estilo artístico: ")
                    periodo_influencia = input("Digite o período de influência: ")
                    caracteristicas = input("Digite as características do estilo: ")
                    escola_representativa = input("Digite a escola representativa: ")
                    cadastrar_estilo_artistico(denominacao, periodo_influencia, caracteristicas, escola_representativa)
                    print("Estilo artístico cadastrado com sucesso!")
                elif opcao_acervo == "4":
                    titulo = input("Digite o título da obra: ")
                    obra = consultar_obra(titulo)
                    if obra:
                        visualizar_obra(obra)
                    else:
                        print("Obra não encontrada.")
                elif opcao_acervo == "5":
                    criterio = input("Digite o critério de pesquisa (título, autor, tema, etc.): ")
                    valor = input("Digite o valor a ser pesquisado: ")
                    resultados = pesquisar_obras(criterio, valor)
                    if resultados:
                        print("Resultados da pesquisa:")
                        for obra in resultados:
                            print(obra["titulo"])
                    else:
                        print("Nenhum resultado encontrado.")
                elif opcao_acervo == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao == "2":
            while True:
                opcao_emprestimos = menu_emprestimos()
                if opcao_emprestimos == "1":
                    titulo_obra = input("Digite o título da obra: ")
                    obra = consultar_obra(titulo_obra)
                    if obra:
                        periodo = input("Digite o período do empréstimo: ")
                        evento = input("Digite o evento: ")
                        responsavel = input("Digite o nome do responsável: ")
                        tema = input("Digite o tema do empréstimo: ")
                        registrar_emprestimo(obra, periodo, evento, responsavel, tema)
                        print("Empréstimo registrado com sucesso!")
                    else:
                        print("Obra não encontrada.")
                elif opcao_emprestimos == "2":
                    for emprestimo in emprestimos:
                        print(f"Obra: {emprestimo['obra']['titulo']}")
                        print(f"Período: {emprestimo['periodo']}")
                        print(f"Evento: {emprestimo['evento']}")
                        print(f"Responsável: {emprestimo['responsavel']}")
                        print(f"Tema: {emprestimo['tema']}")
                        print()
                elif opcao_emprestimos == "3":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao == "3":
            while True:
                opcao_visitas = menu_visitas_guiadas()
                if opcao_visitas == "1":
                    tema = input("Digite o tema da visita guiada: ")
                    descricao = input("Digite a descrição da visita: ")
                    obras_visitadas = []
                    while True:
                        titulo_obra = input("Digite o título da obra (ou 'sair' para finalizar): ")
                        if titulo_obra.lower() == "sair":
                            break
                        obra = consultar_obra(titulo_obra)
                        if obra:
                            obras_visitadas.append(obra)
                        else:
                            print("Obra não encontrada.")
                    cadastrar_visita_guiada(tema, descricao, obras_visitadas)
                    print("Visita guiada cadastrada com sucesso!")
                elif opcao_visitas == "2":
                    for visita in visitas_guiadas:
                        print(f"Tema: {visita['tema']}")
                        print(f"Descrição: {visita['descricao']}")
                        print("Obras Visitadas:")
                        for obra in visita['obras_visitadas']:
                            print(f"- {obra['titulo']}")
                        print()
                elif opcao_visitas == "3":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()