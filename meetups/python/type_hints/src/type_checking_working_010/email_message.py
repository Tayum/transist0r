from src.type_checking_working_010.helper import send_message


class EmailMessage:
    def __init__(self, body: str) -> None:
        self.body = body


if __name__ == "__main__":
    message = EmailMessage("message")
    send_message(message, ["hacker@hackernoon.com", "dont@Stop.Believing"])
