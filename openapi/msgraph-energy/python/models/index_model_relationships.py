from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .index_model_relationships_index_specification import IndexModel_relationships_indexSpecification
    from .index_model_relationships_period import IndexModel_relationships_period

@dataclass
class IndexModel_relationships(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The indexSpecification property
    index_specification: Optional[IndexModel_relationships_indexSpecification] = None
    # The period property
    period: Optional[IndexModel_relationships_period] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IndexModel_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IndexModel_relationships
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IndexModel_relationships()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .index_model_relationships_index_specification import IndexModel_relationships_indexSpecification
        from .index_model_relationships_period import IndexModel_relationships_period

        from .index_model_relationships_index_specification import IndexModel_relationships_indexSpecification
        from .index_model_relationships_period import IndexModel_relationships_period

        fields: Dict[str, Callable[[Any], None]] = {
            "indexSpecification": lambda n : setattr(self, 'index_specification', n.get_object_value(IndexModel_relationships_indexSpecification)),
            "period": lambda n : setattr(self, 'period', n.get_object_value(IndexModel_relationships_period)),
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
        writer.write_object_value("indexSpecification", self.index_specification)
        writer.write_object_value("period", self.period)
        writer.write_additional_data_value(self.additional_data)
    

