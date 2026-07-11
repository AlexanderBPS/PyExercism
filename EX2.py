EXPECTED_BAKE_TIME = 0 #tempo esperado
PREPARATION_TIME = 0 #tempo de preparação
#elapsed_bake_time = tempo decorrido

def bake_time_remaining(elapsed_bake_time) : #bake_time_remaining  = tempo restante
    EXPECTED_BAKE_TIME - elapsed_bake_time #elapsed_bake_time = tempo decorrido
    return bake_time_remaining

def preparation_time_in_minutes(number_of_layers): #numeros magicos são numeros colocados diretamente no código, sem estar atrelado a uma variavel, função ou constante.
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
