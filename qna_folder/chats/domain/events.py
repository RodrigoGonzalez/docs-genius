from dataclasses import dataclass

from foundation.events import Event
from foundation.value_objects import Money

from qna.chats.domain.value_objects import ChatsId


@dataclass(frozen=True)
class BidderHasBeenOverbid(Event):
    auction_id: ChatsId
    bidder_id: BidderId
    new_price: Money
    auction_title: str


@dataclass(frozen=True)
class WinningBidPlaced(Event):
    auction_id: ChatsId
    bidder_id: BidderId
    bid_amount: Money
    auction_title: str


@dataclass(frozen=True)
class ChatEnded(Event):
    auction_id: ChatsId
    winner_id: BidderId | None
    winning_bid: Money
    auction_title: str


@dataclass(frozen=True)
class ChatBegan(Event):
    auction_id: ChatsId
    starting_price: Money
    auction_title: str
