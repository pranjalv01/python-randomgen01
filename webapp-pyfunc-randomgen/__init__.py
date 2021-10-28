import logging
import random
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('filename')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('filename')

    if name:
        result = randomgen(name)

        return func.HttpResponse(result)
        

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

def randomgen(name):
    public_score = round(random.uniform(0.001, 0.999), 3)
    private_score = round(random.uniform(0.001, 0.999), 3)
    public_score = "."+str(public_score).split(".")[-1]
    private_score = "."+str(private_score).split(".")[-1]

    rand_dict = {}
    for var in ["public_score", "private_score"]:
        rand_dict[var] = eval(var)
        scores = json.dumps(rand_dict)
    return (scores)