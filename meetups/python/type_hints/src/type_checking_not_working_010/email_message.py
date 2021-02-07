# email_message.py
from src.type_checking_not_working_010.helper import send_message


class EmailMessage:
    def __init__(self, body: str) -> None:
        self.body = body


if __name__ == "__main__":
    message = EmailMessage("ENCRYPTED")
    send_message(message, ["hacker@hackernoon.com", "dont@Stop.Believing"])
