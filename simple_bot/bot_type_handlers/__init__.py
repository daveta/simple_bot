from bot_type_handlers.contractRelationUpdate import ContractRelationUpdateHandler
from bot_type_handlers.conversationUpdate import ConversationUpdateHandler
from bot_type_handlers.endOfConversation import EndOfConversationHandler
from bot_type_handlers.event import EventHandler
from bot_type_handlers.message import MessageHandler
from bot_type_handlers.ping import PingHandler
from bot_type_handlers.typing import TypingHandler


__type_handlers_map__ = [
    ('event', EventHandler), 
    ('contractRelationUpdate', ContractRelationUpdateHandler),
    ('conversationUpdate', ConversationUpdateHandler),
    ('endOfConversation', EndOfConversationHandler),
    ('event', EventHandler),
    ('message', MessageHandler),
    ('ping', PingHandler),
    ('typing', TypingHandler)
    ]