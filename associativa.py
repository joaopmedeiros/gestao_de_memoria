import sys

def memoria_associativa(arquivo):
    repetir = "S"
    while repetir != 'N':
        # Menu inicial e selecao da config da cahce
        print("#" * 50)
        print("Teste de gestao de memoria associativa")
        print("Selecione a opcao desejada:")
        print("0) Voltar para menu anterior.")
        print("1) 5 bits para tag e 3 bits para palavra.")
        print("2) 6 bits para tag e 2 bits para palavra.")
        print("3) 7 bits para tag e 1 bit para palavra.")
        opcao = -1
        while (opcao < 0 or opcao > 3):
            opcao = int(input("Opcao: "))
        if (opcao == 1):
            tam_tag = 5
            tam_cache = 4
        elif (opcao == 2):
            tam_tag = 6
            tam_cache = 8
        elif (opcao == 3):
            tam_tag = 7
            tam_cache = 16
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

        # Cria 3 estruturas que vao ser usadas, uma lista para memoria associativa, um dicionario para controlar o uso das tags e um dicionario para o cache
        lista_mem_associativa = []
        dic_cache_controle_uso = dict()
        cache = dict()

        # Loop principal dos acessos e gestao da memoria configurada
        for i in lista_acessos:
            tag = i[0][:tam_tag]
            if tag in lista_mem_associativa:
                i[1] = 'HIT'
                dic_cache_controle_uso[tag] = dic_cache_controle_uso[tag] + 1
                cache[tag].add(i[0])
            else:
                i[1] = 'MISS'
                if (len(lista_mem_associativa) < tam_cache):
                    lista_mem_associativa.append(tag)
                    dic_cache_controle_uso[tag] = 1
                    cache[tag] = set()
                    cache[tag].add(i[0])
                else:
                    for key in sorted(dic_cache_controle_uso):
                        tag_menos_usada = key
                        lista_mem_associativa[lista_mem_associativa.index(tag_menos_usada)] = tag
                        dic_cache_controle_uso.pop(tag_menos_usada)
                        dic_cache_controle_uso[tag] = 1
                        cache.pop(tag_menos_usada)
                        cache[tag] = set()
                        cache[tag].add(i[0])
                        break

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
        print("Configuracao final da memoria associativa: ")
        print(lista_mem_associativa)
        print("Configuracao final da cache: ")
        print(cache)
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