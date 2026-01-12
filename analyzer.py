
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

    

if __name__ =="__main__":
    
    relatorio_de_eventos = arrumando_eventos_em_arquivos("eventos.txt") #aqui "relatorio_de_eventos" é resopnsavel por receber o valor qué retornado na funçõa, nesse caso, o diconario.
    #passar o nome do arqivo que deseja ler ^.
    if relatorio_de_eventos is None:
        print('Arquivo não encontrado, por favor verifique o nome do arquivo.')
    elif relatorio_de_eventos == {}:
         print('O arquivo está vazio')
    else:
        for chave, valor in relatorio_de_eventos.items(): #.items() Apresentar o relatório final organizado.
            print(f'{chave} -> {valor}')
       
















