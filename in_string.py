def check_vowels():
    # Código a implementar utilizando input.
    Nombre = input()
    nombre = Nombre.lower()
    print(f'> {Nombre}\n')
    print(f'Contiene a: {"a" in nombre}')
    print(f'Contiene e: {"e" in nombre}')
    print(f'Contiene i: {"i" in nombre}')
    print(f'Contiene o: {"o" in nombre}')
    print(f'Contiene u: {"u" in nombre} \n')
    Nombre2 = input()
    nombre2 = Nombre2.lower()
    print(f'> {Nombre2}\n')
    print(f'Contiene a: {"a" in nombre2}')
    print(f'Contiene e: {"e" in nombre2}')
    print(f'Contiene i: {"i" in nombre2}')
    print(f'Contiene o: {"o" in nombre2}')
    print(f'Contiene u: {"u" in nombre2}')
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
