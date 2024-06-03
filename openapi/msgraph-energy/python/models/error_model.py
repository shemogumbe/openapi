from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ErrorModel(AdditionalDataHolder, Parsable):
    """
    The error object provides additional information about problems encountered while performing an operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # An application-specific error code, expressed as a string value.
    code: Optional[str] = None
    # A human-readable explanation specific to this occurrence of the problem.
    detail: Optional[str] = None
    # A unique identifier for the particular occurence of the problem.
    id: Optional[str] = None
    # The HTTP status code applicable to this problem, expressed as a string value.
    status: Optional[str] = None
    # A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence of the problem.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ErrorModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ErrorModel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ErrorModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("code", self.code)
        writer.write_str_value("detail", self.detail)
        writer.write_str_value("id", self.id)
        writer.write_str_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

