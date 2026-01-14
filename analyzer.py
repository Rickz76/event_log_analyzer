
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

# Loop responsavel por atribuir a devida seriedade e junta-las os eventos do relatorio_de_eventos em um NOVO dicionario "eventos_e_serieade"
    
    for evento, quantidade in relatorio_de_eventos.items(): # evento vem da chave. quantidade vem do valor.
        gravidade = dicionario_gravidade.get(evento, "unknown") # .get(), Se evento existir em dicionario_seriedade -> pega o valor. Se não existir -> "unknown"
        
        evento_e_gravidade[evento] = { # “Use o valor de evento como chave no dicionário evento_e_seriedade.”
            "quantidade": quantidade,
            "gravidade": gravidade
        }
    return evento_e_gravidade

def reajuste_de_gravidade(gravidade_dos_eventos): 

    gravidade_por_quantidade = {}

    for evento, info in gravidade_dos_eventos.items():
        qtd = info["quantidade"]
        grv = info["gravidade"]
        if qtd >= 20 and grv == "low":
            gravidade_final = "medium"
            if qtd >= 70 and grv == "low":
                gravidade_final = "high"
        elif qtd >= 10 and grv == "medium":
            gravidade_final = "high"
        else:
            gravidade_final = grv
        gravidade_por_quantidade[evento] = {
            "quantidade": qtd,
            "gravidade": grv,
            "gravidade_final": gravidade_final

        }
    return gravidade_por_quantidade

if __name__ =="__main__":
    
    relatorio_de_eventos = arrumando_eventos_em_arquivos("eventos.txt") #aqui "relatorio_de_eventos" é resopnsavel por receber o valor qué retornado na funçõa, nesse caso, o diconario.
    #passar o nome do arqivo que deseja ler ^.
    
    if relatorio_de_eventos is None:
        print('Arquivo não encontrado, por favor verifique o nome do arquivo.')
    elif relatorio_de_eventos == {}:
         print('O arquivo está vazio.')
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


        
       
















