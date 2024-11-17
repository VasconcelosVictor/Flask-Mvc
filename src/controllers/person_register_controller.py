from src.models.db.repositores.peaple_repository import PeapleRepository
class PersonRegisterController:
    def __init__(self, ) -> None:
        self.__person_repository = PeapleRepository()

    def create_person(self, person_name :str, person_age : int ) -> dict:
        self.__validate_person_registry(person_name)
        self.__insert_person(person_name, person_age)
        response = self.__format_response(person_name)
        return response

    
    def __validate_person_registry(self, person_name : str) -> None:
        person = self.__person_repository.get_person_by_name(person_name)
        if person:
            raise Exception("Person already registered")

    def __insert_person(self, person_name : str, person_age : int) -> None:
        self.__person_repository.registry_person(person_name, person_age)

    def __format_response(self, person_name : str) -> dict:
        return {
            "type" : "Person",
            "count" : 1,
            "att" : {
                "name": person_name
            }
        }    