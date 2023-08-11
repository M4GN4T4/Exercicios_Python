def notas(*num, Show=False):
    """--> Função Para analisar notas e situações de vários alunos.
    :parametro [num]: uma ou mais notas dos alunos (aceita várias)
    :parametro [situacao]: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    no = dict()
    no['Total'] = len(num)
    no['Maior'] = max(num)
    no['Menor'] = min(num)
    no['Media'] = sum(num) / len(num)
    
    if Show:
        if no['Media'] <= 10:
            no['situacao'] = "Ótima"
        elif no['Media'] <= 7:
            no['situacao'] = "Ótima"
        elif no['Media'] <= 5:
            no['situacao'] = "Ruim"
        elif no['Media'] <= 3:
            no['situacao'] = "Pessima"
    return no  

resp = notas(3, 4, 8, 3.5, 7, 10, Show=True)
print(resp)

help(notas)

    