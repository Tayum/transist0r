from typing import List, Optional


class EmailMessage:
    def __init__(self, to: str, body: str, copies: Optional[List[str]] = None) -> None:
        self.to = to
        self.body = body
        self.reply_to = copies or []
        self._recipients: Optional[List[str]] = None

    @property
    def recipients(self) -> List[str]:
        if self._recipients is None:
            recipients = self.reply_to.copy()
            recipients.append(self.to)
            self._recipients = recipients
        return self._recipients
