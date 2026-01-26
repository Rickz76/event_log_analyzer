
def arrumando_eventos_em_arquivos(caminho_do_arquivo):
    '''Organiza os eventos de um arquivo (parametro), o nome do arquivo é inserido na main. Retorna um dicionario com os eventos e suas quantidades de ocorrencia ou um dicionario vazio se assim for o arquivo, se o arquivo nao existir retorna None.'''
    
    try: #tente executar o seguinte código...
        with open(caminho_do_arquivo,"r") as eventos_do_arquivo: #Abre o arquivo e da a permissao de ler(r)
        #O arquivo vai precisar ter um apelido. (...as apelido:)
            dicionario_de_eventos = {}


            for evento in eventos_do_arquivo: 
                evento = evento.strip().lower().replace(" ", "_")

                if evento: #Python está perguntando: "Essa variável tem algum conteúdo?"
                    if evento in dicionario_de_eventos:
                        dicionario_de_eventos[evento] += 1
                    else:
                        dicionario_de_eventos[evento] = 1
        
            return dicionario_de_eventos

    except FileNotFoundError: #...se nao conseguir, significa que o arquivo não foi encontrado. retorne None.
        return None

def classificacao_de_gravidade(relatorio_de_eventos):
    '''Recebe o dicionario organizado e define uma gravidade ou unknown aos eventos. Retorna um dicionario com nome do envento, qunatas vezes aconteceu e sua gravidade.'''
    
    dicionario_gravidade = { #base.
        "login_failed": "low",
        "access_denied": "medium",
        "root_access": "high"
    }
    
    evento_e_gravidade = {}

# Loop responsavel por atribuir a devida seriedade e junta-las os eventos do relatorio_de_eventos em um NOVO dicionario "eventos_e_gravidade"
    
    for evento_base, gravidade in dicionario_gravidade.items(): # evento vem da chave. quantidade vem do valor.
        quantidade = relatorio_de_eventos.get(evento_base, 0) 
        evento_e_gravidade[evento_base] = { # “Use o valor de evento como chave no dicionário evento_e_gravidade.”
            "quantidade": quantidade,
            "gravidade": gravidade
        }
    for evento, quantidade in relatorio_de_eventos.items():
        gravidade = dicionario_gravidade.get(evento,"unknonw")
        evento_e_gravidade[evento] = {
            "quantidade": quantidade,
            "gravidade": gravidade
        }

    return evento_e_gravidade # AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

def reajuste_de_gravidade(gravidade_dos_eventos): 

    nivel_gravidade = { #Dicionario string pra numero. "Tabela de tradução".
        "unknown":0,
        "low": 1,
        "medium": 2,
        "high": 3
    }

    nivel_para_gravidade = { # Dicionario numero para string. "Tabela de tradução".
        0: "unknonw",
        1: "low",
        2: "medium",
        3: "high"
    }


    gravidade_por_quantidade = {}

    for evento, info in gravidade_dos_eventos.items():
        qtd = info["quantidade"]
        grv = info["gravidade"]

        # converter gravidade (string) para número
        nivel_atual = nivel_gravidade.get(grv, 0) # "Se essa chave existir, me dá o valor. Se não existir, considera nível 0.”
        
        # Gravidade por quantidade e relevancia em numero, não mais em string.
        if nivel_atual == 1 and qtd >= 70:
            nivel_atual = 3
            
        elif nivel_atual == 1 and qtd >= 20:
            nivel_atual = 2
         
        elif nivel_atual == 2 and  qtd >= 10:
            nivel_atual = 3

        else:
            nivel_atual = 0
            
        # Converte numero para string.
        gravidade_final = nivel_para_gravidade.get(nivel_atual)

        gravidade_por_quantidade[evento] = {
            "quantidade": qtd,
            "gravidade": grv,
            "gravidade_final": gravidade_final

        }
    return gravidade_por_quantidade

if __name__ =="__main__":
    #nome_arquivo = input("Digite o nome do arquivo que deseja verificar: ")
    relatorio_de_eventos = arrumando_eventos_em_arquivos("eventos.txt") #aqui "relatorio_de_eventos" é resopnsavel por receber o valor qué retornado na funçõa, nesse caso, o diconario.
    #passar o nome do arqivo que deseja ler ^.
    
    if relatorio_de_eventos is None:
        print('\nArquivo não encontrado, por favor verifique o nome do arquivo.')
    elif relatorio_de_eventos == {}:
         print('\nO arquivo está vazio.')
    else:
        # Só classifica se o relatório existir e não estiver vazio
        gravidade1_dos_eventos = classificacao_de_gravidade(relatorio_de_eventos)
        gravidade2_dos_eventos = reajuste_de_gravidade(gravidade1_dos_eventos)
    
        # deixando bonito
        print(f"{'EVENTO':<20} | {'QTD':<5} | {'GRAVIDADE':<5} | {'FINAL'}") # {evento:<n} reserva de espaços.
        print("-" * 50) # repetir um caractere

        for evento, info in gravidade2_dos_eventos.items(): # evento-> Recebe a chave principal (o nome do erro). info-> Recebe o dicionário interno completo (quantidade e gravidade).
            qtd = info["quantidade"]
            grv = info["gravidade"]
            grvf = info["gravidade_final"]
            print(f"{evento:<20} | {qtd:<5} | {grv:<9} | {grvf.upper()}")


        
       
















