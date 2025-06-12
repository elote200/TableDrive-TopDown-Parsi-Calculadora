from lexer import tokenizar

# Tabla LL(1) como diccionario
parse_table = {
    'E':  {'id': ['T', "E'"], 'number': ['T', "E'"], '(': ['T', "E'"]},
    "E'": {'+': ['+', 'T', "E'"], '-': ['-', 'T', "E'"], ')': [], '$': []},
    'T':  {'id': ['F', "T'"], 'number': ['F', "T'"], '(': ['F', "T'"]},
    "T'": {'+': [], '-': [], '*': ['*', 'F', "T'"], '/': ['/', 'F', "T'"], ')': [], '$': []},
    'F':  {'id': ['id'], 'number': ['number'], '(': ['(', 'E', ')']}
}

# Simula un parser predictivo LL(1)
def parse(tokens):
    stack = ['$', 'E']  # Pila inicia con símbolo de inicio
    tokens.append(['$', '$'])  # Fin de cadena
    index = 0

    print(f"{'Stack':<50}{'Input':<50}{'Action'}")
    print("-" * 70)

    while stack:
        str = ''
        for token in tokens[index:]:
            str += f"{token[1]} "
        
        print(f"{' '.join(stack):<50}{str:<50}", end=' ')

        top = stack.pop()
        current = tokens[index][0]
       
        if top == current == '$':
            print("✓ Accepted")
            return True

        elif top == current:
            print(f"Match terminal '{current}', advance")
            index += 1

        elif top in parse_table:
            rule = parse_table[top].get(current)
            if rule is not None:
                print(f"{top} → {' '.join(rule) if rule else 'ε'}")
                # Si no es ε, agregamos los símbolos al revés
                if rule:
                    stack.extend(reversed(rule))
            else:
                print(f"Error: no rule for {top} with lookahead '{current}'")
                return False
        else:
            print(f"Error: unexpected symbol '{top}'")
            return False

    return False
