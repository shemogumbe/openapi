from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PeriodModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Related absolute period code.
    absolute_period_code: Optional[str] = None
    # Related absolute period display label.
    absolute_period_label: Optional[str] = None
    # Represents how the period code is displayed as default.
    default_period_code: Optional[str] = None
    # Represents how the period label is displayed as default.
    default_period_label: Optional[str] = None
    # Represents the order in which periods are displayed.
    display_order: Optional[float] = None
    # End date of the period.
    end_date: Optional[datetime.datetime] = None
    # Period type name.
    period_type: Optional[str] = None
    # Date for which the period is relevant.
    reference_date: Optional[datetime.datetime] = None
    # Related relative period code.
    relative_period_code: Optional[str] = None
    # Related relative period display label.
    relative_period_label: Optional[str] = None
    # Start date of the period.
    start_date: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PeriodModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PeriodModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PeriodModel_attributes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "absolutePeriodCode": lambda n : setattr(self, 'absolute_period_code', n.get_str_value()),
            "absolutePeriodLabel": lambda n : setattr(self, 'absolute_period_label', n.get_str_value()),
            "defaultPeriodCode": lambda n : setattr(self, 'default_period_code', n.get_str_value()),
            "defaultPeriodLabel": lambda n : setattr(self, 'default_period_label', n.get_str_value()),
            "displayOrder": lambda n : setattr(self, 'display_order', n.get_float_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_datetime_value()),
            "periodType": lambda n : setattr(self, 'period_type', n.get_str_value()),
            "referenceDate": lambda n : setattr(self, 'reference_date', n.get_datetime_value()),
            "relativePeriodCode": lambda n : setattr(self, 'relative_period_code', n.get_str_value()),
            "relativePeriodLabel": lambda n : setattr(self, 'relative_period_label', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_datetime_value()),
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
        writer.write_str_value("absolutePeriodCode", self.absolute_period_code)
        writer.write_str_value("absolutePeriodLabel", self.absolute_period_label)
        writer.write_str_value("defaultPeriodCode", self.default_period_code)
        writer.write_str_value("defaultPeriodLabel", self.default_period_label)
        writer.write_float_value("displayOrder", self.display_order)
        writer.write_datetime_value("endDate", self.end_date)
        writer.write_str_value("periodType", self.period_type)
        writer.write_datetime_value("referenceDate", self.reference_date)
        writer.write_str_value("relativePeriodCode", self.relative_period_code)
        writer.write_str_value("relativePeriodLabel", self.relative_period_label)
        writer.write_datetime_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    

