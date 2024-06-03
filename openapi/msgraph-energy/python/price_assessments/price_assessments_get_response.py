from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.period_model import PeriodModel
    from ..models.price_assessment_model import PriceAssessmentModel
    from ..models.price_assessment_specification_model import PriceAssessmentSpecificationModel
    from .price_assessments_get_response_included import PriceAssessmentsGetResponse_included
    from .price_assessments_get_response_links import PriceAssessmentsGetResponse_links

@dataclass
class PriceAssessmentsGetResponse(AdditionalDataHolder, Parsable):
    """
    A list of PriceAssessment entities.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The data property
    data: Optional[List[PriceAssessmentModel]] = None
    # The included property
    included: Optional[List[PriceAssessmentsGetResponse_included]] = None
    # The links property
    links: Optional[PriceAssessmentsGetResponse_links] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PriceAssessmentsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PriceAssessmentsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PriceAssessmentsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..models.period_model import PeriodModel
        from ..models.price_assessment_model import PriceAssessmentModel
        from ..models.price_assessment_specification_model import PriceAssessmentSpecificationModel
        from .price_assessments_get_response_included import PriceAssessmentsGetResponse_included
        from .price_assessments_get_response_links import PriceAssessmentsGetResponse_links

        from ..models.period_model import PeriodModel
        from ..models.price_assessment_model import PriceAssessmentModel
        from ..models.price_assessment_specification_model import PriceAssessmentSpecificationModel
        from .price_assessments_get_response_included import PriceAssessmentsGetResponse_included
        from .price_assessments_get_response_links import PriceAssessmentsGetResponse_links

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(PriceAssessmentModel)),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(PriceAssessmentsGetResponse_included)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(PriceAssessmentsGetResponse_links)),
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
    class PriceAssessmentsGetResponse_included(ComposedTypeWrapper, Parsable):
        from kiota_abstractions.serialization import ComposedTypeWrapper

        """
        Composed type wrapper for classes PeriodModel, PriceAssessmentSpecificationModel
        """
        @staticmethod
        def create_from_discriminator_value(parse_node: ParseNode) -> PriceAssessmentsGetResponse_included:
            """
            Creates a new instance of the appropriate class based on discriminator value
            param parse_node: The parse node to use to read the discriminator value and create the object
            Returns: PriceAssessmentsGetResponse_included
            """
            if not parse_node:
                raise TypeError("parse_node cannot be null.")
            result = PriceAssessmentsGetResponse_included()
            result.period_model = PeriodModel()
            result.price_assessment_specification_model = PriceAssessmentSpecificationModel()
            return result
        
        def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
            """
            The deserialization information for the current model
            Returns: Dict[str, Callable[[ParseNode], None]]
            """
            if self.period_model or self.price_assessment_specification_model:
                return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.period_model, self.price_assessment_specification_model)
            return {}
        
        def serialize(self,writer: SerializationWriter) -> None:
            """
            Serializes information the current object
            param writer: Serialization writer to use to serialize this model
            Returns: None
            """
            if not writer:
                raise TypeError("writer cannot be null.")
            writer.write_object_value(None, self.period_model, self.price_assessment_specification_model)
        
    

