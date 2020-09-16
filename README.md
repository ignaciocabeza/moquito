# Mock OpenAPI from Spec file

This is a working example (Proof of concept) of a mock api from a OpenApi file.

Install dependecies with `pipenv install`

Try it with `pipenv run uvicorn app:app --reload`

This examples has:
* GET / -> Uses mock2
* GET /{dataset}/{version}/fields?start=1 -> Uses mock1
    * if {dataset} == 1 -> returns different result
* POST /{dataset}/{version}/records -> uses mock2