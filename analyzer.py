
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
    '''Recebe o dicionario organizado e define uma gravidade ou unknown aos eventos. Retorna um dicionario com nome do envento, quantas vezes aconteceu e sua gravidade. Define eventos base que vão aparecerno relatorio final independdente de terem ocorrido ou não.'''
    
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
        gravidade = dicionario_gravidade.get(evento,"unknown")
        evento_e_gravidade[evento] = {
            "quantidade": quantidade,
            "gravidade": gravidade
        }

    return evento_e_gravidade # AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

def reajuste_de_gravidade(gravidade1_dos_eventos): 

    nivel_para_gravidade = { # Dicionario numero para string. "Tabela de tradução".
        0: "none",
        1: "low",
        2: "medium",
        3: "high"
    }


    gravidade_por_quantidade = {}

    for evento, info in gravidade1_dos_eventos.items():
        qtd = info["quantidade"]
        

        
        
        # Gravidade por quantidade e relevancia em numero.
        if qtd == 0: 
            nivel_atual = 0

        elif qtd >= 31:
            nivel_atual = 3
        
        elif 11 <= qtd <= 30:
            nivel_atual = 2

        elif 1 <= qtd <= 10:
            nivel_atual = 1
           
        gravidade_por_quantidade[evento] = {
            "quantidade": qtd,
            "gravidade": info["gravidade"],
            "gravidade_calculada": nivel_para_gravidade[nivel_atual]

        }
    return gravidade_por_quantidade


def relevancia_da_quantidade(gravidade2_dos_eventos):
    """
    Decide a gravidade final: usa a maior entre a base e a calculada por quantidade.
    """
    niveis = {"unknown": 0,
     "none": 0,
      "low": 1,
      "medium": 2,
       "high": 3}
    resultado_final = {}

    for evento, dados in gravidade2_dos_eventos.items():
        v_base = niveis.get(dados["gravidade"], 0)
        v_calc = niveis.get(dados["gravidade_calculada"], 0)
        
        # Escolhe o maior nível entre o pré-_definido e o baseado em volume
        maior_nivel = (v_base if v_base > v_calc else v_calc) if dados["quantidade"] > 0 else 0
        
        # Traduz de volta para string
        traducao = {0: "NONE", 1: "LOW", 2: "MEDIUM", 3: "HIGH"}
        
        resultado_final[evento] = {
            "quantidade": dados["quantidade"],
            "gravidade_base": dados["gravidade"],
            "gravidade_final": traducao[maior_nivel]
        }
    return resultado_final

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
        g1 = classificacao_de_gravidade(relatorio_de_eventos)
        g2 = reajuste_de_gravidade(g1)
        g3 = relevancia_da_quantidade(g2)
    
        # deixando bonito
        print(f"{'EVENTO':<20} | {'QTD':<5} | {'GRAVIDADE':<5} | {'FINAL'}") # {evento:<n} reserva de espaços.
        print("-" * 50) # repetir um caractere

        for evento, info in g3.items(): # evento-> Recebe a chave principal (o nome do erro). info-> Recebe o dicionário interno completo (quantidade e gravidade).
            qtd = info["quantidade"]
            grv = info["gravidade_base"]
            grvf = info["gravidade_final"]
            print(f"{evento:<20} | {qtd:<5} | {grv:<9} | {grvf.upper()}")


        
       
















