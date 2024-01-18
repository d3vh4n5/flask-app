variable = "caca"

match variable:
    case "pedo":
        print('Salud culito')
    case "caca":
        print("Tomá papel")
    case _: # Esto sería el default
        print("No reconozco el ruido")