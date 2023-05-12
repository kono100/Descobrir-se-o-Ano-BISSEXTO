from datetime import date

while True:
    ano = int(input('\nQual Ano quer analisar ? '))
    if ano == 0:
        break

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

        print("\033[0;32;40m\nO ano de {} é BISSEXTO!\n\033[0m".format(ano))
    else:
        print('\033[0;31;40m\nO ano de {} NÃO é BISSEXTO!\n\033[0m'.format(ano))




