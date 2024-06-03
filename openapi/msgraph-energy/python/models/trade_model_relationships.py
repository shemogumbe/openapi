from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .trade_model_relationships_period import TradeModel_relationships_period
    from .trade_model_relationships_trade_specification import TradeModel_relationships_tradeSpecification

@dataclass
class TradeModel_relationships(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The period property
    period: Optional[TradeModel_relationships_period] = None
    # The tradeSpecification property
    trade_specification: Optional[TradeModel_relationships_tradeSpecification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TradeModel_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TradeModel_relationships
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TradeModel_relationships()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .trade_model_relationships_period import TradeModel_relationships_period
        from .trade_model_relationships_trade_specification import TradeModel_relationships_tradeSpecification

        from .trade_model_relationships_period import TradeModel_relationships_period
        from .trade_model_relationships_trade_specification import TradeModel_relationships_tradeSpecification

        fields: Dict[str, Callable[[Any], None]] = {
            "period": lambda n : setattr(self, 'period', n.get_object_value(TradeModel_relationships_period)),
            "tradeSpecification": lambda n : setattr(self, 'trade_specification', n.get_object_value(TradeModel_relationships_tradeSpecification)),
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
        writer.write_object_value("period", self.period)
        writer.write_object_value("tradeSpecification", self.trade_specification)
        writer.write_additional_data_value(self.additional_data)
    

