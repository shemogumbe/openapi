from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.period_model import PeriodModel
    from .periods_get_response_links import PeriodsGetResponse_links

@dataclass
class PeriodsGetResponse(AdditionalDataHolder, Parsable):
    """
    A list of period entities.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The data property
    data: Optional[List[PeriodModel]] = None
    # The links property
    links: Optional[PeriodsGetResponse_links] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PeriodsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PeriodsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PeriodsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..models.period_model import PeriodModel
        from .periods_get_response_links import PeriodsGetResponse_links

        from ..models.period_model import PeriodModel
        from .periods_get_response_links import PeriodsGetResponse_links

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(PeriodModel)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(PeriodsGetResponse_links)),
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
        writer.write_object_value("links", self.links)
        writer.write_additional_data_value(self.additional_data)
    

