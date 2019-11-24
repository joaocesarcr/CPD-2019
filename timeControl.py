################
# TIME CONTROL #
################
# 20 requests every 1 seconds(s)
# 100 requests every 2 minutes(s)

# Recebe uma funcao e um parametro para ser utilizado nela. Retorna o tempo de decorrimento da funcao e seu retorno
# str + generic -> int, generic
# TO-D0 : Transformar parameter em uma lista
def functionTime(functionName, parameter):
    initTime = time.time()
    retorno = functionName(parameter)
    endTime = time.time()
    return (endTime - initTime), retorno



