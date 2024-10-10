#Variables globales
integral = ""
#Funciones
def run(symbol: str) -> str:
    # TODO
    global integral
    #Variables locales
    separacion = symbol.find(",")
    coeficiente = int(symbol[:separacion])
    exponente = int(symbol[separacion +1 :])

    integral = f" {coeficiente//(exponente+1)} x ^{exponente +1 }"
    
    return integral

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(integral)