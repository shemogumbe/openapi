from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.data_event_model import DataEventModel
    from .data_events_get_response_links import DataEventsGetResponse_links

@dataclass
class DataEventsGetResponse(AdditionalDataHolder, Parsable):
    """
    A list of DataEvent entities.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The data property
    data: Optional[List[DataEventModel]] = None
    # The links property
    links: Optional[DataEventsGetResponse_links] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataEventsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataEventsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DataEventsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..models.data_event_model import DataEventModel
        from .data_events_get_response_links import DataEventsGetResponse_links

        from ..models.data_event_model import DataEventModel
        from .data_events_get_response_links import DataEventsGetResponse_links

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(DataEventModel)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(DataEventsGetResponse_links)),
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
        writer.write_collection_of_object_values("data", self.data)
        writer.write_object_value("links", self.links)
        writer.write_additional_data_value(self.additional_data)
    

