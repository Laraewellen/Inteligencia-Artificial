def simbolismo_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    else:
        return "Adulto"

print(simbolismo_idade(15))  # Saída: Adolescente