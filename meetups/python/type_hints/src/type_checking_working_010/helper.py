from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.type_checking_working_010.email_message import EmailMessage


def send_message(msg: "EmailMessage", recipients: List[str]) -> None:
    for recipient in recipients:
        print(f"Message {msg.body} is sent to {recipient}")
