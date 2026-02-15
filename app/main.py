class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list) -> list:
    the_list = []
    Person.people.clear()
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband = Person.people[person[
                "husband"]]
        the_list.append(Person.people[person["name"]])
    return the_list
