from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.index_model import IndexModel
    from ...models.index_specification_model import IndexSpecificationModel
    from ...models.period_model import PeriodModel
    from .indices_get_response_included import IndicesGetResponse_included

@dataclass
class IndicesGetResponse(AdditionalDataHolder, Parsable):
    """
    Index entity.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indices are volume-weighted averages of trades gathered and verified by ICIS during the course of its market reporting activities or weighted averages of price assessments or other indices to represent an overall market performance.
    data: Optional[IndexModel] = None
    # The included property
    included: Optional[List[IndicesGetResponse_included]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IndicesGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IndicesGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IndicesGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.index_model import IndexModel
        from ...models.index_specification_model import IndexSpecificationModel
        from ...models.period_model import PeriodModel
        from .indices_get_response_included import IndicesGetResponse_included

        from ...models.index_model import IndexModel
        from ...models.index_specification_model import IndexSpecificationModel
        from ...models.period_model import PeriodModel
        from .indices_get_response_included import IndicesGetResponse_included

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(IndexModel)),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(IndicesGetResponse_included)),
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
    class IndicesGetResponse_included(ComposedTypeWrapper, Parsable):
        from kiota_abstractions.serialization import ComposedTypeWrapper

        """
        Composed type wrapper for classes IndexSpecificationModel, PeriodModel
        """
        @staticmethod
        def create_from_discriminator_value(parse_node: ParseNode) -> IndicesGetResponse_included:
            """
            Creates a new instance of the appropriate class based on discriminator value
            param parse_node: The parse node to use to read the discriminator value and create the object
            Returns: IndicesGetResponse_included
            """
            if not parse_node:
                raise TypeError("parse_node cannot be null.")
            result = IndicesGetResponse_included()
            result.index_specification_model = IndexSpecificationModel()
            result.period_model = PeriodModel()
            return result
        
        def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
            """
            The deserialization information for the current model
            Returns: Dict[str, Callable[[ParseNode], None]]
            """
            if self.index_specification_model or self.period_model:
                return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.index_specification_model, self.period_model)
            return {}
        
        def serialize(self,writer: SerializationWriter) -> None:
            """
            Serializes information the current object
            param writer: Serialization writer to use to serialize this model
            Returns: None
            """
            if not writer:
                raise TypeError("writer cannot be null.")
            writer.write_object_value(None, self.index_specification_model, self.period_model)
        
    

