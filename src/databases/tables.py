from typing import Set, Dict, Any


class Record(dict):
    def __hash__(self) -> int:
        proxy = tuple(self.items())
        return hash(proxy)

    def __setitem__(self, key: Any, value: Any):
        raise NotImplemented("Modifying values is not supported.")


def make_employee(id: int, name: str, position: str, salary: int) -> Record:
    return Record({"id": id, "name": name, "position": position, "salary": salary})


def make_task(id: int, employee_id: int, completed: bool) -> Record:
    return Record({"id": id, "employee_id": employee_id, "completed": completed})


def make_client(id: int, name: str, contact_id: int) -> Record:
    return Record({"id": id, "name": name, "contact_id": contact_id})
