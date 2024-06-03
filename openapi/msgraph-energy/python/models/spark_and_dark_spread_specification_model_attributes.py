from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .spark_and_dark_spread_specification_model_attributes_market_delivery_profile_name import SparkAndDarkSpreadSpecificationModel_attributes_marketDeliveryProfileName

@dataclass
class SparkAndDarkSpreadSpecificationModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicates the Carbon Price Support (CPS) used.
    carbon_price_support: Optional[str] = None
    # Unique code representing the spark and dark spread specification.
    code: Optional[str] = None
    # Represents the name of the original data supplier.
    data_supplier_name: Optional[str] = None
    # Indicates the Emission Conversion Factor (ECF) used.
    emission_conversion_factor: Optional[str] = None
    # Indicates the heating value basis.
    heating_value_code: Optional[str] = None
    # Market Delivery Profile represents the demand for electricity over time, specific to the market.
    market_delivery_profile_name: Optional[SparkAndDarkSpreadSpecificationModel_attributes_marketDeliveryProfileName] = None
    # Name of the spark and dark spread specification.
    name: Optional[str] = None
    # Indicates the efficiency of the power plant.
    plant_efficiency: Optional[str] = None
    # Indicates the type of spark and dark spread.
    spread_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SparkAndDarkSpreadSpecificationModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SparkAndDarkSpreadSpecificationModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SparkAndDarkSpreadSpecificationModel_attributes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .spark_and_dark_spread_specification_model_attributes_market_delivery_profile_name import SparkAndDarkSpreadSpecificationModel_attributes_marketDeliveryProfileName

        from .spark_and_dark_spread_specification_model_attributes_market_delivery_profile_name import SparkAndDarkSpreadSpecificationModel_attributes_marketDeliveryProfileName

        fields: Dict[str, Callable[[Any], None]] = {
            "carbonPriceSupport": lambda n : setattr(self, 'carbon_price_support', n.get_str_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "dataSupplierName": lambda n : setattr(self, 'data_supplier_name', n.get_str_value()),
            "emissionConversionFactor": lambda n : setattr(self, 'emission_conversion_factor', n.get_str_value()),
            "heatingValueCode": lambda n : setattr(self, 'heating_value_code', n.get_str_value()),
            "marketDeliveryProfileName": lambda n : setattr(self, 'market_delivery_profile_name', n.get_enum_value(SparkAndDarkSpreadSpecificationModel_attributes_marketDeliveryProfileName)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "plantEfficiency": lambda n : setattr(self, 'plant_efficiency', n.get_str_value()),
            "spreadType": lambda n : setattr(self, 'spread_type', n.get_str_value()),
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
        writer.write_str_value("carbonPriceSupport", self.carbon_price_support)
        writer.write_str_value("code", self.code)
        writer.write_str_value("dataSupplierName", self.data_supplier_name)
        writer.write_str_value("emissionConversionFactor", self.emission_conversion_factor)
        writer.write_str_value("heatingValueCode", self.heating_value_code)
        writer.write_enum_value("marketDeliveryProfileName", self.market_delivery_profile_name)
        writer.write_str_value("name", self.name)
        writer.write_str_value("plantEfficiency", self.plant_efficiency)
        writer.write_str_value("spreadType", self.spread_type)
        writer.write_additional_data_value(self.additional_data)
    

