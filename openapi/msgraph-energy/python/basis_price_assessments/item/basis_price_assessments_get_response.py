from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.basis_price_assessment_model import BasisPriceAssessmentModel
    from ...models.basis_price_assessment_specification_model import BasisPriceAssessmentSpecificationModel
    from ...models.period_model import PeriodModel
    from .basis_price_assessments_get_response_included import BasisPriceAssessmentsGetResponse_included

@dataclass
class BasisPriceAssessmentsGetResponse(AdditionalDataHolder, Parsable):
    """
    BasisPriceAssessment entity.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Basis price assessments represent the basis bid-offer price ranges and the outright bid-offer price ranges for a commodity delivered at a number of markets.
    data: Optional[BasisPriceAssessmentModel] = None
    # The included property
    included: Optional[List[BasisPriceAssessmentsGetResponse_included]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BasisPriceAssessmentsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BasisPriceAssessmentsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BasisPriceAssessmentsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.basis_price_assessment_model import BasisPriceAssessmentModel
        from ...models.basis_price_assessment_specification_model import BasisPriceAssessmentSpecificationModel
        from ...models.period_model import PeriodModel
        from .basis_price_assessments_get_response_included import BasisPriceAssessmentsGetResponse_included

        from ...models.basis_price_assessment_model import BasisPriceAssessmentModel
        from ...models.basis_price_assessment_specification_model import BasisPriceAssessmentSpecificationModel
        from ...models.period_model import PeriodModel
        from .basis_price_assessments_get_response_included import BasisPriceAssessmentsGetResponse_included

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(BasisPriceAssessmentModel)),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(BasisPriceAssessmentsGetResponse_included)),
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
    class BasisPriceAssessmentsGetResponse_included(ComposedTypeWrapper, Parsable):
        from kiota_abstractions.serialization import ComposedTypeWrapper

        """
        Composed type wrapper for classes BasisPriceAssessmentSpecificationModel, PeriodModel
        """
        @staticmethod
        def create_from_discriminator_value(parse_node: ParseNode) -> BasisPriceAssessmentsGetResponse_included:
            """
            Creates a new instance of the appropriate class based on discriminator value
            param parse_node: The parse node to use to read the discriminator value and create the object
            Returns: BasisPriceAssessmentsGetResponse_included
            """
            if not parse_node:
                raise TypeError("parse_node cannot be null.")
            result = BasisPriceAssessmentsGetResponse_included()
            result.basis_price_assessment_specification_model = BasisPriceAssessmentSpecificationModel()
            result.period_model = PeriodModel()
            return result
        
        def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
            """
            The deserialization information for the current model
            Returns: Dict[str, Callable[[ParseNode], None]]
            """
            if self.basis_price_assessment_specification_model or self.period_model:
                return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.basis_price_assessment_specification_model, self.period_model)
            return {}
        
        def serialize(self,writer: SerializationWriter) -> None:
            """
            Serializes information the current object
            param writer: Serialization writer to use to serialize this model
            Returns: None
            """
            if not writer:
                raise TypeError("writer cannot be null.")
            writer.write_object_value(None, self.basis_price_assessment_specification_model, self.period_model)
        
    

