from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.period_model import PeriodModel
    from ...models.spark_and_dark_spread_model import SparkAndDarkSpreadModel
    from ...models.spark_and_dark_spread_specification_model import SparkAndDarkSpreadSpecificationModel
    from .spark_and_dark_spreads_get_response_included import SparkAndDarkSpreadsGetResponse_included

@dataclass
class SparkAndDarkSpreadsGetResponse(AdditionalDataHolder, Parsable):
    """
    SparkAndDarkSpread entity.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Spark and dark spreads are the cost of power per MWh minus the fuel needed to generate that power. Spark is for gas, dark is for coal.
    data: Optional[SparkAndDarkSpreadModel] = None
    # The included property
    included: Optional[List[SparkAndDarkSpreadsGetResponse_included]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SparkAndDarkSpreadsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SparkAndDarkSpreadsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SparkAndDarkSpreadsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.period_model import PeriodModel
        from ...models.spark_and_dark_spread_model import SparkAndDarkSpreadModel
        from ...models.spark_and_dark_spread_specification_model import SparkAndDarkSpreadSpecificationModel
        from .spark_and_dark_spreads_get_response_included import SparkAndDarkSpreadsGetResponse_included

        from ...models.period_model import PeriodModel
        from ...models.spark_and_dark_spread_model import SparkAndDarkSpreadModel
        from ...models.spark_and_dark_spread_specification_model import SparkAndDarkSpreadSpecificationModel
        from .spark_and_dark_spreads_get_response_included import SparkAndDarkSpreadsGetResponse_included

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(SparkAndDarkSpreadModel)),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(SparkAndDarkSpreadsGetResponse_included)),
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
        writer.write_object_value("data", self.data)
        writer.write_collection_of_object_values("included", self.included)
        writer.write_additional_data_value(self.additional_data)
    
    from kiota_abstractions.serialization import ComposedTypeWrapper

    @dataclass
    class SparkAndDarkSpreadsGetResponse_included(ComposedTypeWrapper, Parsable):
        from kiota_abstractions.serialization import ComposedTypeWrapper

        """
        Composed type wrapper for classes PeriodModel, SparkAndDarkSpreadSpecificationModel
        """
        @staticmethod
        def create_from_discriminator_value(parse_node: ParseNode) -> SparkAndDarkSpreadsGetResponse_included:
            """
            Creates a new instance of the appropriate class based on discriminator value
            param parse_node: The parse node to use to read the discriminator value and create the object
            Returns: SparkAndDarkSpreadsGetResponse_included
            """
            if not parse_node:
                raise TypeError("parse_node cannot be null.")
            result = SparkAndDarkSpreadsGetResponse_included()
            result.period_model = PeriodModel()
            result.spark_and_dark_spread_specification_model = SparkAndDarkSpreadSpecificationModel()
            return result
        
        def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
            """
            The deserialization information for the current model
            Returns: Dict[str, Callable[[ParseNode], None]]
            """
            if self.period_model or self.spark_and_dark_spread_specification_model:
                return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.period_model, self.spark_and_dark_spread_specification_model)
            return {}
        
        def serialize(self,writer: SerializationWriter) -> None:
            """
            Serializes information the current object
            param writer: Serialization writer to use to serialize this model
            Returns: None
            """
            if not writer:
                raise TypeError("writer cannot be null.")
            writer.write_object_value(None, self.period_model, self.spark_and_dark_spread_specification_model)
        
    

