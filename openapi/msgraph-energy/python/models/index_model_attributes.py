from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class IndexModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Percent change to the last index price displayed in decimal format. Values can be positive, zero or negative numbers.
    change_pct: Optional[float] = None
    # The date the index is created for.
    created_for_date: Optional[datetime.datetime] = None
    # Difference to the last index price. Values can be positive, zero or negative numbers.
    diff_to_prev_price: Optional[float] = None
    # The date when the index was last modified.
    modified_date_time: Optional[datetime.datetime] = None
    # Number of trades.
    num_of_trades: Optional[float] = None
    # Index price.
    price: Optional[float] = None
    # Indicates why price is null.
    price_reason: Optional[str] = None
    # Traded high price.
    trade_high_price: Optional[float] = None
    # Traded low price.
    trade_low_price: Optional[float] = None
    # Total volume.
    volume: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IndexModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IndexModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IndexModel_attributes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "changePct": lambda n : setattr(self, 'change_pct', n.get_float_value()),
            "createdForDate": lambda n : setattr(self, 'created_for_date', n.get_datetime_value()),
            "diffToPrevPrice": lambda n : setattr(self, 'diff_to_prev_price', n.get_float_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "numOfTrades": lambda n : setattr(self, 'num_of_trades', n.get_float_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "priceReason": lambda n : setattr(self, 'price_reason', n.get_str_value()),
            "tradeHighPrice": lambda n : setattr(self, 'trade_high_price', n.get_float_value()),
            "tradeLowPrice": lambda n : setattr(self, 'trade_low_price', n.get_float_value()),
            "volume": lambda n : setattr(self, 'volume', n.get_float_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_float_value("changePct", self.change_pct)
        writer.write_datetime_value("createdForDate", self.created_for_date)
        writer.write_float_value("diffToPrevPrice", self.diff_to_prev_price)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_float_value("numOfTrades", self.num_of_trades)
        writer.write_float_value("price", self.price)
        writer.write_str_value("priceReason", self.price_reason)
        writer.write_float_value("tradeHighPrice", self.trade_high_price)
        writer.write_float_value("tradeLowPrice", self.trade_low_price)
        writer.write_float_value("volume", self.volume)
        writer.write_additional_data_value(self.additional_data)
    

