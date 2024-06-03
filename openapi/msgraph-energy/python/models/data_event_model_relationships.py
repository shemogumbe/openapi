from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_event_model_relationships_event_resources import DataEventModel_relationships_eventResources

@dataclass
class DataEventModel_relationships(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The eventResources property
    event_resources: Optional[DataEventModel_relationships_eventResources] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataEventModel_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataEventModel_relationships
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DataEventModel_relationships()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .data_event_model_relationships_event_resources import DataEventModel_relationships_eventResources

        from .data_event_model_relationships_event_resources import DataEventModel_relationships_eventResources

        fields: Dict[str, Callable[[Any], None]] = {
            "eventResources": lambda n : setattr(self, 'event_resources', n.get_object_value(DataEventModel_relationships_eventResources)),
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
        writer.write_object_value("eventResources", self.event_resources)
        writer.write_additional_data_value(self.additional_data)
    

