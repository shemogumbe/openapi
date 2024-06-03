from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class LocationSpreadModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Percent change to the last location spread price displayed in decimal format. Values can be in positive, zero or negative numbers.
    change_pct: Optional[float] = None
    # The date the location spread is created for.
    created_for_date: Optional[datetime.datetime] = None
    # Difference to the last location spread price. Values can be positive, zero or negative numbers.
    diff_to_prev_price: Optional[float] = None
    # The date when the location spread was last modified.
    modified_date_time: Optional[datetime.datetime] = None
    # Location spread price. Values can be positive, zero or negative numbers.
    price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocationSpreadModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocationSpreadModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LocationSpreadModel_attributes()
    
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
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
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
        writer.write_float_value("price", self.price)
        writer.write_additional_data_value(self.additional_data)
    

