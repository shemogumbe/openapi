from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .price_assessment_specification_model_attributes_market_delivery_profile_name import PriceAssessmentSpecificationModel_attributes_marketDeliveryProfileName

@dataclass
class PriceAssessmentSpecificationModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Unique code representing the price assessment specification.
    code: Optional[str] = None
    # Represents the name of the original data supplier.
    data_supplier_name: Optional[str] = None
    # Indicates if the respective dataset is unit/currency converted.
    is_converted: Optional[bool] = None
    # Market Delivery Profile represents the demand for electricity over time, specific to the market.
    market_delivery_profile_name: Optional[PriceAssessmentSpecificationModel_attributes_marketDeliveryProfileName] = None
    # Name of the price assessment specification.
    name: Optional[str] = None
    # Indicates when during the day, prices are published. The possible values are EoD (End of Day), Intra-day and Closing Day.
    timeliness_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PriceAssessmentSpecificationModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PriceAssessmentSpecificationModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PriceAssessmentSpecificationModel_attributes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .price_assessment_specification_model_attributes_market_delivery_profile_name import PriceAssessmentSpecificationModel_attributes_marketDeliveryProfileName

        from .price_assessment_specification_model_attributes_market_delivery_profile_name import PriceAssessmentSpecificationModel_attributes_marketDeliveryProfileName

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "dataSupplierName": lambda n : setattr(self, 'data_supplier_name', n.get_str_value()),
            "isConverted": lambda n : setattr(self, 'is_converted', n.get_bool_value()),
            "marketDeliveryProfileName": lambda n : setattr(self, 'market_delivery_profile_name', n.get_enum_value(PriceAssessmentSpecificationModel_attributes_marketDeliveryProfileName)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "timelinessName": lambda n : setattr(self, 'timeliness_name', n.get_str_value()),
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
        writer.write_str_value("dataSupplierName", self.data_supplier_name)
        writer.write_bool_value("isConverted", self.is_converted)
        writer.write_enum_value("marketDeliveryProfileName", self.market_delivery_profile_name)
        writer.write_str_value("name", self.name)
        writer.write_str_value("timelinessName", self.timeliness_name)
        writer.write_additional_data_value(self.additional_data)
    

