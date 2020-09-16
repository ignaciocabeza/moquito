from fastapi import FastAPI
from makefun import create_function
from prance import ResolvingParser

parser = ResolvingParser('api-spec.yaml')
paths = parser.specification['paths'].items()

app = FastAPI()

def mock1(**kargs):
    if kargs['dataset'] == '1':
        return {'dataset1 in mock1'}
    return {'another dataset in mock1'}

def mock2(**kargs):
    return {'mock2'}

def callback_mapper(operation):
    if operation == 'list-searchable-fields':
        return mock1
    else:
        return mock2

for path, methods in paths:
    for method, definition in methods.items():

        # read parameters
        args = []
        if 'parameters' in definition:
            for parameter in definition['parameters']:
                args.append(parameter['name'])

        # create callback function
        callback_header = f"callback({','.join(args)})"
        callback_target = callback_mapper(definition['operationId'])
        callback = create_function(callback_header, callback_target)
        
        # create route
        app.router.add_api_route(path, callback, methods=[method])
