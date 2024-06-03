from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .location_spread_specification_model_attributes import LocationSpreadSpecificationModel_attributes
    from .location_spread_specification_model_relationships import LocationSpreadSpecificationModel_relationships

@dataclass
class LocationSpreadSpecificationModel(AdditionalDataHolder, Parsable):
    """
    Location spread specification describes information about the market, secondary market, currency and unit associated with the location spread.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The attributes property
    attributes: Optional[LocationSpreadSpecificationModel_attributes] = None
    # Unique identifier of the location spread specification.
    id: Optional[str] = None
    # The relationships property
    relationships: Optional[LocationSpreadSpecificationModel_relationships] = None
    # Type of data.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocationSpreadSpecificationModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocationSpreadSpecificationModel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LocationSpreadSpecificationModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .location_spread_specification_model_attributes import LocationSpreadSpecificationModel_attributes
        from .location_spread_specification_model_relationships import LocationSpreadSpecificationModel_relationships

        from .location_spread_specification_model_attributes import LocationSpreadSpecificationModel_attributes
        from .location_spread_specification_model_relationships import LocationSpreadSpecificationModel_relationships

        fields: Dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(LocationSpreadSpecificationModel_attributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(LocationSpreadSpecificationModel_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_object_value("attributes", self.attributes)
        writer.write_str_value("id", self.id)
        writer.write_object_value("relationships", self.relationships)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

