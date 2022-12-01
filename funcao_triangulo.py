def is_triangle(x,y,z):

    """Essa classe avalia se três comprimentos podem ser um triângulo ou não"""

    if((x + y) < z or (x + z) < y or (y + z) < x):
        print("No")
    else: 
        print("Yes")

if __name__ == "__main__": ## usar sempre quando voce quiser testar um trecho do código
    print("Teste")
    is_triangle(2.2,2.2,2.0) 