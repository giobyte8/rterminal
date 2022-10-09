from enum import Enum
from pydantic import BaseModel

class ConversationStatus(Enum):
    WAITING_USER_PASSPHRASE = "WAITING_USER_PASSPHRASE"
    UNKNOWN = "UNKNOWN"

    # ? Neither user nor bot are waiting for response
    STANDBY = "STANDBY"

class TGChat(BaseModel):
    id: int
    first_name: str
    type: str

class TGMessage(BaseModel):
    message_id: int
    chat: TGChat
    date: int
    text: str

class TGResponseMsg(BaseModel):
    chat_id: int
    text: str
