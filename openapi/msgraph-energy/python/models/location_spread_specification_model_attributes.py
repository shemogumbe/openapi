from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .location_spread_specification_model_attributes_market_delivery_profile_name import LocationSpreadSpecificationModel_attributes_marketDeliveryProfileName

@dataclass
class LocationSpreadSpecificationModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Unique code representing the location spread specification.
    code: Optional[str] = None
    # Represents the name of the original data supplier.
    data_supplier_name: Optional[str] = None
    # Market Delivery Profile represents the demand for electricity over time, specific to the market.
    market_delivery_profile_name: Optional[LocationSpreadSpecificationModel_attributes_marketDeliveryProfileName] = None
    # Name of the location spread specification.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocationSpreadSpecificationModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocationSpreadSpecificationModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LocationSpreadSpecificationModel_attributes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .location_spread_specification_model_attributes_market_delivery_profile_name import LocationSpreadSpecificationModel_attributes_marketDeliveryProfileName

        from .location_spread_specification_model_attributes_market_delivery_profile_name import LocationSpreadSpecificationModel_attributes_marketDeliveryProfileName

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "dataSupplierName": lambda n : setattr(self, 'data_supplier_name', n.get_str_value()),
            "marketDeliveryProfileName": lambda n : setattr(self, 'market_delivery_profile_name', n.get_enum_value(LocationSpreadSpecificationModel_attributes_marketDeliveryProfileName)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_enum_value("marketDeliveryProfileName", self.market_delivery_profile_name)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

