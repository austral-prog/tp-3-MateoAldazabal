def slice_simple():
    texto = "Awesome"
    texto = texto.lower()
    mitad = int(len(texto)/2)
    print(texto[0:3])
    print(texto[ mitad-1: mitad + 2])
    print(f'{texto[0:4]}{texto[-3:]}')

