from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .location_spread_specification_model_relationships_currency import LocationSpreadSpecificationModel_relationships_currency
    from .location_spread_specification_model_relationships_market import LocationSpreadSpecificationModel_relationships_market
    from .location_spread_specification_model_relationships_secondary_market import LocationSpreadSpecificationModel_relationships_secondaryMarket
    from .location_spread_specification_model_relationships_unit import LocationSpreadSpecificationModel_relationships_unit

@dataclass
class LocationSpreadSpecificationModel_relationships(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The currency property
    currency: Optional[LocationSpreadSpecificationModel_relationships_currency] = None
    # The market property
    market: Optional[LocationSpreadSpecificationModel_relationships_market] = None
    # The secondaryMarket property
    secondary_market: Optional[LocationSpreadSpecificationModel_relationships_secondaryMarket] = None
    # The unit property
    unit: Optional[LocationSpreadSpecificationModel_relationships_unit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocationSpreadSpecificationModel_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocationSpreadSpecificationModel_relationships
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LocationSpreadSpecificationModel_relationships()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .location_spread_specification_model_relationships_currency import LocationSpreadSpecificationModel_relationships_currency
        from .location_spread_specification_model_relationships_market import LocationSpreadSpecificationModel_relationships_market
        from .location_spread_specification_model_relationships_secondary_market import LocationSpreadSpecificationModel_relationships_secondaryMarket
        from .location_spread_specification_model_relationships_unit import LocationSpreadSpecificationModel_relationships_unit

        from .location_spread_specification_model_relationships_currency import LocationSpreadSpecificationModel_relationships_currency
        from .location_spread_specification_model_relationships_market import LocationSpreadSpecificationModel_relationships_market
        from .location_spread_specification_model_relationships_secondary_market import LocationSpreadSpecificationModel_relationships_secondaryMarket
        from .location_spread_specification_model_relationships_unit import LocationSpreadSpecificationModel_relationships_unit

        fields: Dict[str, Callable[[Any], None]] = {
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(LocationSpreadSpecificationModel_relationships_currency)),
            "market": lambda n : setattr(self, 'market', n.get_object_value(LocationSpreadSpecificationModel_relationships_market)),
            "secondaryMarket": lambda n : setattr(self, 'secondary_market', n.get_object_value(LocationSpreadSpecificationModel_relationships_secondaryMarket)),
            "unit": lambda n : setattr(self, 'unit', n.get_object_value(LocationSpreadSpecificationModel_relationships_unit)),
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
        writer.write_object_value("currency", self.currency)
        writer.write_object_value("market", self.market)
        writer.write_object_value("secondaryMarket", self.secondary_market)
        writer.write_object_value("unit", self.unit)
        writer.write_additional_data_value(self.additional_data)
    

