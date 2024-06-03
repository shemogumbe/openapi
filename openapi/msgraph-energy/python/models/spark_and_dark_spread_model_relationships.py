from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .spark_and_dark_spread_model_relationships_period import SparkAndDarkSpreadModel_relationships_period
    from .spark_and_dark_spread_model_relationships_spark_and_dark_spread_specification import SparkAndDarkSpreadModel_relationships_sparkAndDarkSpreadSpecification

@dataclass
class SparkAndDarkSpreadModel_relationships(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The period property
    period: Optional[SparkAndDarkSpreadModel_relationships_period] = None
    # The sparkAndDarkSpreadSpecification property
    spark_and_dark_spread_specification: Optional[SparkAndDarkSpreadModel_relationships_sparkAndDarkSpreadSpecification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SparkAndDarkSpreadModel_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SparkAndDarkSpreadModel_relationships
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SparkAndDarkSpreadModel_relationships()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .spark_and_dark_spread_model_relationships_period import SparkAndDarkSpreadModel_relationships_period
        from .spark_and_dark_spread_model_relationships_spark_and_dark_spread_specification import SparkAndDarkSpreadModel_relationships_sparkAndDarkSpreadSpecification

        from .spark_and_dark_spread_model_relationships_period import SparkAndDarkSpreadModel_relationships_period
        from .spark_and_dark_spread_model_relationships_spark_and_dark_spread_specification import SparkAndDarkSpreadModel_relationships_sparkAndDarkSpreadSpecification

        fields: Dict[str, Callable[[Any], None]] = {
            "period": lambda n : setattr(self, 'period', n.get_object_value(SparkAndDarkSpreadModel_relationships_period)),
            "sparkAndDarkSpreadSpecification": lambda n : setattr(self, 'spark_and_dark_spread_specification', n.get_object_value(SparkAndDarkSpreadModel_relationships_sparkAndDarkSpreadSpecification)),
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
        writer.write_object_value("period", self.period)
        writer.write_object_value("sparkAndDarkSpreadSpecification", self.spark_and_dark_spread_specification)
        writer.write_additional_data_value(self.additional_data)
    

