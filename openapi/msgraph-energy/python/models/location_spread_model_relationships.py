from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .location_spread_model_relationships_location_spread_specification import LocationSpreadModel_relationships_locationSpreadSpecification
    from .location_spread_model_relationships_period import LocationSpreadModel_relationships_period

@dataclass
class LocationSpreadModel_relationships(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The locationSpreadSpecification property
    location_spread_specification: Optional[LocationSpreadModel_relationships_locationSpreadSpecification] = None
    # The period property
    period: Optional[LocationSpreadModel_relationships_period] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocationSpreadModel_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocationSpreadModel_relationships
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LocationSpreadModel_relationships()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .location_spread_model_relationships_location_spread_specification import LocationSpreadModel_relationships_locationSpreadSpecification
        from .location_spread_model_relationships_period import LocationSpreadModel_relationships_period

        from .location_spread_model_relationships_location_spread_specification import LocationSpreadModel_relationships_locationSpreadSpecification
        from .location_spread_model_relationships_period import LocationSpreadModel_relationships_period

        fields: Dict[str, Callable[[Any], None]] = {
            "locationSpreadSpecification": lambda n : setattr(self, 'location_spread_specification', n.get_object_value(LocationSpreadModel_relationships_locationSpreadSpecification)),
            "period": lambda n : setattr(self, 'period', n.get_object_value(LocationSpreadModel_relationships_period)),
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
        writer.write_object_value("locationSpreadSpecification", self.location_spread_specification)
        writer.write_object_value("period", self.period)
        writer.write_additional_data_value(self.additional_data)
    

