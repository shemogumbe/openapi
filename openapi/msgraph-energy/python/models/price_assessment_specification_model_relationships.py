from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .price_assessment_specification_model_relationships_currency import PriceAssessmentSpecificationModel_relationships_currency
    from .price_assessment_specification_model_relationships_market import PriceAssessmentSpecificationModel_relationships_market
    from .price_assessment_specification_model_relationships_unit import PriceAssessmentSpecificationModel_relationships_unit

@dataclass
class PriceAssessmentSpecificationModel_relationships(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The currency property
    currency: Optional[PriceAssessmentSpecificationModel_relationships_currency] = None
    # The market property
    market: Optional[PriceAssessmentSpecificationModel_relationships_market] = None
    # The unit property
    unit: Optional[PriceAssessmentSpecificationModel_relationships_unit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PriceAssessmentSpecificationModel_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PriceAssessmentSpecificationModel_relationships
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PriceAssessmentSpecificationModel_relationships()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .price_assessment_specification_model_relationships_currency import PriceAssessmentSpecificationModel_relationships_currency
        from .price_assessment_specification_model_relationships_market import PriceAssessmentSpecificationModel_relationships_market
        from .price_assessment_specification_model_relationships_unit import PriceAssessmentSpecificationModel_relationships_unit

        from .price_assessment_specification_model_relationships_currency import PriceAssessmentSpecificationModel_relationships_currency
        from .price_assessment_specification_model_relationships_market import PriceAssessmentSpecificationModel_relationships_market
        from .price_assessment_specification_model_relationships_unit import PriceAssessmentSpecificationModel_relationships_unit

        fields: Dict[str, Callable[[Any], None]] = {
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(PriceAssessmentSpecificationModel_relationships_currency)),
            "market": lambda n : setattr(self, 'market', n.get_object_value(PriceAssessmentSpecificationModel_relationships_market)),
            "unit": lambda n : setattr(self, 'unit', n.get_object_value(PriceAssessmentSpecificationModel_relationships_unit)),
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
        writer.write_object_value("currency", self.currency)
        writer.write_object_value("market", self.market)
        writer.write_object_value("unit", self.unit)
        writer.write_additional_data_value(self.additional_data)
    

