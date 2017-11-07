from numpy import binary_repr
import sys

def gerarEnderecos(enderecoOriginal, dicionarioTag, linha, tag, tamanho_palavra):
    for i in range(pow(2,tamanho_palavra)):
        final = binary_repr(i, tamanho_palavra)
        dados = enderecoOriginal[:-tamanho_palavra]
        dados = dados + final
        dicionarioTag[linha][tag].append(dados)

def memoria_direta(arquivo):
    repetir = "S"
    while repetir != 'N':
        # Menu inicial e selecao da config da cache
        print("#" * 50)
        print("Teste de gestao de memoria direta")
        print("Selecione a opcao desejada:")
        print("0) Voltar para menu anterior.")
        print("1) 3 bits para tag, 2 bits para linha e 3 bits para palavra.")
        print("2) 3 bits para tag, 3 bits para linha e 2 bits para palavra.")
        print("3) 3 bits para tag, 4 bits para linha e 1 bits para palavra.")
        opcao = -1
        while opcao < 0 or opcao > 3:
            opcao = int(input("Opcao: "))
        if (opcao == 1):
            bits = 8
            tam_palavra = 3
            tam_linha = 2
            tam_tag = bits - tam_linha - tam_palavra
            tam_cache = pow(2,tam_linha)
        elif (opcao == 2):
            bits = 8
            tam_palavra = 2
            tam_linha = 3
            tam_tag = bits - tam_linha - tam_palavra
            tam_cache = pow(2,tam_linha)
        elif opcao == 3:
            bits = 8
            tam_palavra = 1
            tam_linha = 4
            tam_tag = bits - tam_linha - tam_palavra
            tam_cache = pow(2,tam_linha)
        else:
            print("")
            import principal as prin
            prin.menu_principal(arquivo)

        # Carrega lista de acessos a memoria para uma pre lista
        with open(arquivo, 'r') as file:
            lista_acessos_pre = file.read().splitlines()

        # Cria uma lista com varias dentro para colocar o resultado do acesso
        lista_acessos = []
        for i in lista_acessos_pre:
            lista_acessos.append([i, 'to test'])

        # Deleta a lista pre
        del lista_acessos_pre

        # Cria 2 estruturas que vao ser usadas:
        #  um dicionario onde a chave eh a linha e o valor eh o bit de validade,
        #  um dicionario onde a chave eh a linha e o valor eh:
        #    um novo dicionario onde a chave eh a tag e o valor eh um array que comporta as palavras,
        dicionarioCache = {}
        for i in range(tam_cache):
            dicionarioCache[binary_repr(i, tam_linha)] = '0'

        dicionarioTag = {}
        for i in range(tam_cache):
            dicionarioTag[binary_repr(i, tam_linha)] = dict()

        for j in lista_acessos:
            tag = j[0][:tam_tag]
            linha = j[0][tam_tag:-tam_palavra]
            if linha in dicionarioCache:
                if dicionarioCache.get(linha) == '0':
                    j[1] = 'MISS'
                    dicionarioCache[linha] = 1
                    dicionarioTag[linha] = {tag: []}
                    gerarEnderecos(j[0], dicionarioTag, linha, tag, tam_palavra)
                else:
                    if tag in dicionarioTag[linha].keys():
                        if dicionarioTag[linha][tag].count(j[0]) == 1:
                            j[1] = 'HIT'
                    else:
                        j[1] = 'MISS'
                        dicionarioCache[linha] = 1
                        dicionarioTag[linha] = {tag: []}
                        gerarEnderecos(j[0], dicionarioTag, linha, tag, tam_palavra)
            else:
                sys.exit("Linha nao encontrada.")

        # Geracao das estatisticas
        hits = 0
        misses = 0
        for i in lista_acessos:
            if (i[1] == 'HIT'):
                hits = hits + 1
            elif (i[1] == 'MISS'):
                misses = misses + 1
            else:
                print("Algo deu errado.")
        total = hits + misses
        perc_hits = round(hits / float(total), 4) * 100
        perc_misses = round(misses / float(total), 4) * 100

        # Mandando pra tela os resultados
        print("#" * 50)
        print("Estatisticas")
        print(
            "Total de HIT: {}. Total de MISS: {}. Perc. de HIT: {} %. Perc. de MISS: {} %.".format(hits, misses,
                                                                                                   perc_hits,
                                                                                                   perc_misses))
        print("#" * 50)
        print("Configuracao final da cache: ")
        for k, v in sorted(dicionarioTag.items()):
            print("Linha: " + k)
            print("Tag / Dados: " + str(v))
            print("")
        print("#" * 50)
        print("Analitico de HITs e MISSes por endereco: ")
        for i in lista_acessos:
            print(i)

        print("")
        print("")
        num = 0
        while (num != 1):
            repetir = raw_input("Deseja repetir para outra configuracao? : <s> ou <n> ")
            if (repetir == 's' or repetir == 'n'):
                num = 1
            else:
                num = 0
        repetir = repetir.upper()
        print("")
        print("")

    print("")
    sys.exit("Programa encerrado.")