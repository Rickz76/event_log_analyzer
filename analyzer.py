
def arrumando_eventos_em_arquivos(caminho_do_arquivo):
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


if __name__ =="__main__":
    
    relatorio_de_eventos = arrumando_eventos_em_arquivos("eventos.txt") #aqui "relatorio_de_eventos" é resopnsavel por receber o valor qué retornado na funçõa, nesse caso, o diconario.
    #passar o nome do arqivo que deseja ler ^.
    
    if relatorio_de_eventos is None:
        print('Arquivo não encontrado, por favor verifique o nome do arquivo.')
    elif relatorio_de_eventos == {}:
         print('O arquivo está vazio')
    else:
        # Só classifica se o relatório existir e não estiver vazio
        gravidade_dos_eventos = classificacao_de_gravidade(relatorio_de_eventos)

        # deixando bonito
        print(f"{'EVENTO':<20} | {'QTD':<5} | {'GRAVIDADE'}") # {evento:<n} reserva de espaços.
        print("-" * 40) # repetir um caractere

        for evento, info in gravidade_dos_eventos.items(): # evento-> Recebe a chave principal (o nome do erro). info-> Recebe o dicionário interno completo (quantidade e gravidade).
            qtd = info["quantidade"]
            grv = info["gravidade"]
            print(f"{evento:<20} | {qtd:<5} | {grv.upper()}")


        
       
















