from suma import sumar
import os
import sys

print("=== LAMBDA DEBUG START ===")
print("cwd:", os.getcwd())
print("files:", os.listdir("."))
print("sys.path:", sys.path)
print("=== LAMBDA DEBUG END ===")
def lambda_handler(event, context):
    a = event.get("a", 0)
    b = event.get("b", 0)

    resultado = sumar(a, b)

    return {
        "statusCode": 200,
        "result": resultado
    }