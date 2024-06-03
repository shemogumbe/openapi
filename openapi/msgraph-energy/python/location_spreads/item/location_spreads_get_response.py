from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.location_spread_model import LocationSpreadModel
    from ...models.location_spread_specification_model import LocationSpreadSpecificationModel
    from ...models.period_model import PeriodModel
    from .location_spreads_get_response_included import LocationSpreadsGetResponse_included

@dataclass
class LocationSpreadsGetResponse(AdditionalDataHolder, Parsable):
    """
    LocationSpread entity.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Location spreads are price differentials and reflect the premium of the first-named market to the second named market.
    data: Optional[LocationSpreadModel] = None
    # The included property
    included: Optional[List[LocationSpreadsGetResponse_included]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocationSpreadsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocationSpreadsGetResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LocationSpreadsGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.location_spread_model import LocationSpreadModel
        from ...models.location_spread_specification_model import LocationSpreadSpecificationModel
        from ...models.period_model import PeriodModel
        from .location_spreads_get_response_included import LocationSpreadsGetResponse_included

        from ...models.location_spread_model import LocationSpreadModel
        from ...models.location_spread_specification_model import LocationSpreadSpecificationModel
        from ...models.period_model import PeriodModel
        from .location_spreads_get_response_included import LocationSpreadsGetResponse_included

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(LocationSpreadModel)),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(LocationSpreadsGetResponse_included)),
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
    class LocationSpreadsGetResponse_included(ComposedTypeWrapper, Parsable):
        from kiota_abstractions.serialization import ComposedTypeWrapper

        """
        Composed type wrapper for classes LocationSpreadSpecificationModel, PeriodModel
        """
        @staticmethod
        def create_from_discriminator_value(parse_node: ParseNode) -> LocationSpreadsGetResponse_included:
            """
            Creates a new instance of the appropriate class based on discriminator value
            param parse_node: The parse node to use to read the discriminator value and create the object
            Returns: LocationSpreadsGetResponse_included
            """
            if not parse_node:
                raise TypeError("parse_node cannot be null.")
            result = LocationSpreadsGetResponse_included()
            result.location_spread_specification_model = LocationSpreadSpecificationModel()
            result.period_model = PeriodModel()
            return result
        
        def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
            """
            The deserialization information for the current model
            Returns: Dict[str, Callable[[ParseNode], None]]
            """
            if self.location_spread_specification_model or self.period_model:
                return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.location_spread_specification_model, self.period_model)
            return {}
        
        def serialize(self,writer: SerializationWriter) -> None:
            """
            Serializes information the current object
            param writer: Serialization writer to use to serialize this model
            Returns: None
            """
            if not writer:
                raise TypeError("writer cannot be null.")
            writer.write_object_value(None, self.location_spread_specification_model, self.period_model)
        
    

