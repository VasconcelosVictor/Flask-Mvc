from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.person_register_controller import PersonRegisterController

class PersonRegisterView:
    def __init__(self) -> None:
        self.__controller = PersonRegisterController()
        
    def handle(self, http_request : HttpRequest) -> HttpResponse:
        body = http_request.body
        person_name = body.get("person_name")
        person_age = body.get("person_age")
        self.__validate_inputs(person_name, person_age)
 
        response = self.__controller.create_person(person_name, person_age)
        return HttpResponse(body={"data":response}, status_code=201)

    def __validate_inputs(self, person_name : any, person_age : any) -> None:
        if (
            not person_name
            or not person_age 
            or not isinstance(person_name, str)
            or not isinstance(person_age, int)
            ):
            raise Exception("Invalid inputs for person registry")    