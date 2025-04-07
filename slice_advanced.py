def slice_advanced():
    # Código a implementar utilizando input.
    Texto = "awesome"
    texto = Texto.lower()
    mitad = int(len(texto)/2)

    print(texto[0:3])
    print(texto[ mitad-1: mitad + 2])
    print(f'{texto[0:4]}{texto[-3:]}')
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
