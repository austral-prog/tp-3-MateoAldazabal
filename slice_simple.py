def slice_simple():
    texto = "Awesome"
    Texto = texto.lower()
    mitad = int(len(Texto)/2)
    print(texto[0:3])
    print(texto[ mitad-1: mitad + 2])
    print(f'{texto[0:4]}{texto[-3:]}')

