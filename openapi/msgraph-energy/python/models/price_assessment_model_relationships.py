from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .price_assessment_model_relationships_period import PriceAssessmentModel_relationships_period
    from .price_assessment_model_relationships_price_assessment_specification import PriceAssessmentModel_relationships_priceAssessmentSpecification

@dataclass
class PriceAssessmentModel_relationships(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The period property
    period: Optional[PriceAssessmentModel_relationships_period] = None
    # The priceAssessmentSpecification property
    price_assessment_specification: Optional[PriceAssessmentModel_relationships_priceAssessmentSpecification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PriceAssessmentModel_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PriceAssessmentModel_relationships
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PriceAssessmentModel_relationships()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .price_assessment_model_relationships_period import PriceAssessmentModel_relationships_period
        from .price_assessment_model_relationships_price_assessment_specification import PriceAssessmentModel_relationships_priceAssessmentSpecification

        from .price_assessment_model_relationships_period import PriceAssessmentModel_relationships_period
        from .price_assessment_model_relationships_price_assessment_specification import PriceAssessmentModel_relationships_priceAssessmentSpecification

        fields: Dict[str, Callable[[Any], None]] = {
            "period": lambda n : setattr(self, 'period', n.get_object_value(PriceAssessmentModel_relationships_period)),
            "priceAssessmentSpecification": lambda n : setattr(self, 'price_assessment_specification', n.get_object_value(PriceAssessmentModel_relationships_priceAssessmentSpecification)),
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
        writer.write_object_value("priceAssessmentSpecification", self.price_assessment_specification)
        writer.write_additional_data_value(self.additional_data)
    

