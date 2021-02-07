from typing import List, Optional


class EmailMessage:
    def __init__(self, to, body, copies=None):
        # type: (str, str, Optional[List[str]]) -> None
        self.to = to
        self.body = body
        self.reply_to = copies or []
        self._recipients = None  # type: Optional[List[str]]

    @property
    def recipients(self):
        # type: () -> List[str]
        if self._recipients is None:
            recipients = self.reply_to.copy()
            recipients.append(self.to)
            self._recipients = recipients
        return self._recipients
