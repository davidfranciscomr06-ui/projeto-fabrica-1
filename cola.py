def calcula_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

def tabela_nota(nota):
    if nota >= 7:
        return "aprovado"
    elif 5 <= nota < 7:
        return "recuperaçao"
    else:
        return "reprovado"