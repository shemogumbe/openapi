from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .trade_model_attributes_market_delivery_profile_name import TradeModel_attributes_marketDeliveryProfileName

@dataclass
class TradeModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The date the trade is created for.
    created_for_date: Optional[datetime.datetime] = None
    # Indicates if a trade is qualified for index calculation.
    is_index_qualified: Optional[bool] = None
    # Market Delivery Profile represents the demand for electricity over time, specific to the market.
    market_delivery_profile_name: Optional[TradeModel_attributes_marketDeliveryProfileName] = None
    # The date when the trade was last modified.
    modified_date_time: Optional[datetime.datetime] = None
    # Price traded.
    price: Optional[float] = None
    # Total volume for the delivery period.
    total_volume: Optional[float] = None
    # The date and time when the trade was transacted.
    trade_date_time: Optional[datetime.datetime] = None
    # Indicates the buy or sell side of the trade.
    trade_side: Optional[str] = None
    # Type of trade.
    trade_type: Optional[str] = None
    # Quantity traded.
    volume: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TradeModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TradeModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TradeModel_attributes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .trade_model_attributes_market_delivery_profile_name import TradeModel_attributes_marketDeliveryProfileName

        from .trade_model_attributes_market_delivery_profile_name import TradeModel_attributes_marketDeliveryProfileName

        fields: Dict[str, Callable[[Any], None]] = {
            "createdForDate": lambda n : setattr(self, 'created_for_date', n.get_datetime_value()),
            "isIndexQualified": lambda n : setattr(self, 'is_index_qualified', n.get_bool_value()),
            "marketDeliveryProfileName": lambda n : setattr(self, 'market_delivery_profile_name', n.get_enum_value(TradeModel_attributes_marketDeliveryProfileName)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "totalVolume": lambda n : setattr(self, 'total_volume', n.get_float_value()),
            "tradeDateTime": lambda n : setattr(self, 'trade_date_time', n.get_datetime_value()),
            "tradeSide": lambda n : setattr(self, 'trade_side', n.get_str_value()),
            "tradeType": lambda n : setattr(self, 'trade_type', n.get_str_value()),
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
        writer.write_datetime_value("createdForDate", self.created_for_date)
        writer.write_bool_value("isIndexQualified", self.is_index_qualified)
        writer.write_enum_value("marketDeliveryProfileName", self.market_delivery_profile_name)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_float_value("price", self.price)
        writer.write_float_value("totalVolume", self.total_volume)
        writer.write_datetime_value("tradeDateTime", self.trade_date_time)
        writer.write_str_value("tradeSide", self.trade_side)
        writer.write_str_value("tradeType", self.trade_type)
        writer.write_float_value("volume", self.volume)
        writer.write_additional_data_value(self.additional_data)
    

