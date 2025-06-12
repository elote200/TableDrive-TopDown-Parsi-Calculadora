from parser import parse


from lexer import tokenizar

def main():
    # Print the results
    texto = "5 + 3"
    tokens = tokenizar(texto)
    print("Tokens:", tokens)

    print("Starting parser...")


    if parse(tokens):
        print("Cadena aceptada. ✅")
    else:
        print("Cadena no aceptada. ❌")




if __name__ == "__main__":
    main()
    
    
    