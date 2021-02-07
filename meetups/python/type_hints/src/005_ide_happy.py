class Company:
    employees: int


class Orty(Company):
    employees = 5
    website = "orty.io"


class NCSoft(Company):
    employees = 1000


def transfer_employees(receiver: Company, sender: Company, amount: int) -> None:
    if sender.employees < amount:
        raise Exception("Not enough employees")

    sender.employees -= amount
    receiver.employees += amount
