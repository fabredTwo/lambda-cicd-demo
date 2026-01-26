from suma import sumar
import os
import sys
import json

print("=== LAMBDA DEBUG START ===")
print("cwd:", os.getcwd())
print("files:", os.listdir("."))
print("sys.path:", sys.path)
print("=== LAMBDA DEBUG END ===")

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}

    try:
        a = int(params.get("a"))
        b = int(params.get("b"))
    except (TypeError, ValueError):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Parámetros inválidos. Usa ?a=NUM&b=NUM"
            })
        }

    resultado = sumar(a, b)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "resultado": resultado
        })
    }
