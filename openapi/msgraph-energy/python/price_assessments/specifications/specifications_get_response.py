from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.currency_model import CurrencyModel
    from ...models.market_model import MarketModel
    from ...models.price_assessment_specification_model import PriceAssessmentSpecificationModel
    from ...models.unit_model import UnitModel
    from .specifications_get_response_included import SpecificationsGetResponse_included
    from .specifications_get_response_links import SpecificationsGetResponse_links

@dataclass
class SpecificationsGetResponse(AdditionalDataHolder, Parsable):
    """
    A list of PriceAssessmentSpecification entities.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The data property
    data: Optional[List[PriceAssessmentSpecificationModel]] = None
    # The included property
    included: Optional[List[SpecificationsGetResponse_included]] = None
    # The links property
    links: Optional[SpecificationsGetResponse_links] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecificationsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecificationsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SpecificationsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.currency_model import CurrencyModel
        from ...models.market_model import MarketModel
        from ...models.price_assessment_specification_model import PriceAssessmentSpecificationModel
        from ...models.unit_model import UnitModel
        from .specifications_get_response_included import SpecificationsGetResponse_included
        from .specifications_get_response_links import SpecificationsGetResponse_links

        from ...models.currency_model import CurrencyModel
        from ...models.market_model import MarketModel
        from ...models.price_assessment_specification_model import PriceAssessmentSpecificationModel
        from ...models.unit_model import UnitModel
        from .specifications_get_response_included import SpecificationsGetResponse_included
        from .specifications_get_response_links import SpecificationsGetResponse_links

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(PriceAssessmentSpecificationModel)),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(SpecificationsGetResponse_included)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(SpecificationsGetResponse_links)),
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
        writer.write_collection_of_object_values("data", self.data)
        writer.write_collection_of_object_values("included", self.included)
        writer.write_object_value("links", self.links)
        writer.write_additional_data_value(self.additional_data)
    
    from kiota_abstractions.serialization import ComposedTypeWrapper

    @dataclass
    class SpecificationsGetResponse_included(ComposedTypeWrapper, Parsable):
        from kiota_abstractions.serialization import ComposedTypeWrapper

        """
        Composed type wrapper for classes CurrencyModel, MarketModel, UnitModel
        """
        @staticmethod
        def create_from_discriminator_value(parse_node: ParseNode) -> SpecificationsGetResponse_included:
            """
            Creates a new instance of the appropriate class based on discriminator value
            param parse_node: The parse node to use to read the discriminator value and create the object
            Returns: SpecificationsGetResponse_included
            """
            if not parse_node:
                raise TypeError("parse_node cannot be null.")
            result = SpecificationsGetResponse_included()
            result.currency_model = CurrencyModel()
            result.market_model = MarketModel()
            result.unit_model = UnitModel()
            return result
        
        def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
            """
            The deserialization information for the current model
            Returns: Dict[str, Callable[[ParseNode], None]]
            """
            if self.self.currency_model or self.market_model or self.unit_model:
                return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.self.currency_model, self.market_model, self.unit_model)
            return {}
        
        def serialize(self,writer: SerializationWriter) -> None:
            """
            Serializes information the current object
            param writer: Serialization writer to use to serialize this model
            Returns: None
            """
            if not writer:
                raise TypeError("writer cannot be null.")
            writer.write_object_value(None, self.self.currency_model, self.market_model, self.unit_model)
        
    

