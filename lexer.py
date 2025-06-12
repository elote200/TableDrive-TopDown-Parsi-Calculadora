import re

TOKEN_REGEX = [
    ('(', r'\('),
    (')', r'\)'),
    ('id', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('number', r'\b\d+\b'),
    ('+', r'\+'),
    ('-', r'-'),
    ('*', r'\*'),
    ('/', r'/'),
    ('ESPACIO', r'\s+'),
    ('DESCONOCIDO', r'.')
]

def tokenizar(string):
    tokens = []

    while string:
        for tipo, patron in TOKEN_REGEX:
            match = re.match(patron, string)
            if match:
                valor = match.group()
                if tipo != 'ESPACIO':

                    tokens.append([tipo, valor])  # Guarda el token como string
                    
                string = string[len(valor):]
                break
    return tokens
