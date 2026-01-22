from suma import sumar

def lambda_handler(event, context):
    a = event.get("a", 0)
    b = event.get("b", 0)

    resultado = sumar(a, b)

    return {
        "statusCode": 200,
        "result": resultado
    }