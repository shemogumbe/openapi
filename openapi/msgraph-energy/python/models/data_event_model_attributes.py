from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DataEventModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The timestamp when the dataset is created.
    created_for_date: Optional[datetime.datetime] = None
    # The timestamp when the data event is created.
    event_creation_time: Optional[datetime.datetime] = None
    # The type of the event that triggered the creation of the data event.
    event_type: Optional[str] = None
    # The resource type associated with the event.
    resource_type: Optional[str] = None
    # The specification Id for which the dataset is published.
    specification_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataEventModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataEventModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DataEventModel_attributes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "createdForDate": lambda n : setattr(self, 'created_for_date', n.get_datetime_value()),
            "eventCreationTime": lambda n : setattr(self, 'event_creation_time', n.get_datetime_value()),
            "eventType": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "specificationId": lambda n : setattr(self, 'specification_id', n.get_str_value()),
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
        writer.write_datetime_value("eventCreationTime", self.event_creation_time)
        writer.write_str_value("eventType", self.event_type)
        writer.write_str_value("resourceType", self.resource_type)
        writer.write_str_value("specificationId", self.specification_id)
        writer.write_additional_data_value(self.additional_data)
    

