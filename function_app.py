import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

def validate_cpf(cpf: str) -> bool:
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # CPF validation logic
    def calculate_digit(cpf, factor):
        total = sum(int(digit) * factor for digit, factor in zip(cpf[:-2], range(factor, 1, -1)))
        remainder = total % 11
        return '0' if remainder < 2 else str(11 - remainder)

    first_digit = calculate_digit(cpf, 10)
    second_digit = calculate_digit(cpf + first_digit, 11)

    return cpf[-2:] == first_digit + second_digit


@app.route(route="validacpf", auth_level=func.AuthLevel.FUNCTION)
def validacpf(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cpf = req_body.get('cpf')

    if cpf:
        if validate_cpf(cpf):
            return func.HttpResponse(
                json.dumps({"valid": True}),
                status_code=200
            )
        else:
            return func.HttpResponse(
                json.dumps({"valid": False}),
                status_code=400
            )
    else:
        return func.HttpResponse(
            "Please pass a CPF on the query string or in the request body",
            status_code=400
        )