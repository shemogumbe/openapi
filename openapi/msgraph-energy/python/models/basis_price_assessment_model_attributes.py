from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BasisPriceAssessmentModel_attributes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Basis bid price. Values can be positive, zero or negative numbers.
    basis_bid: Optional[float] = None
    # Percent change to the last assessed basis midpoint price displayed in decimal format. Values can be positive, zero or negative numbers.
    basis_change_pct: Optional[float] = None
    # Basis mid-point price. Values can be positive, zero or negative numbers.
    basis_midpoint: Optional[float] = None
    # Basis offer price. Values can be positive, zero or negative numbers.
    basis_offer: Optional[float] = None
    # Bid price. Values can be positive, zero or negative numbers.
    bid: Optional[float] = None
    # Percent change to the last assessed midpoint price displayed in decimal format. Values can be positive, zero or negative numbers.
    change_pct: Optional[float] = None
    # The date the assessment is created for.
    created_for_date: Optional[datetime.datetime] = None
    # Data used identifies the pricing approach and represented as a letter key. B - Bid/Offer, T - Transaction, S - Spread, I - Interpolation/Extrapolation, F - Fundamentals.
    data_used: Optional[str] = None
    # Difference to the last assessed basis midpoint price. Values can be positive, zero or negative numbers.
    diff_to_prev_basis_mid: Optional[float] = None
    # Difference to the last assessed midpoint price. Values can be positive, zero or negative numbers.
    diff_to_prev_mid: Optional[float] = None
    # Indicative bid offers.
    is_estimate: Optional[bool] = None
    # Mid-point price. Values can be positive, zero or negative numbers.
    midpoint: Optional[float] = None
    # The date when the assessment was last modified.
    modified_date_time: Optional[datetime.datetime] = None
    # Offer price. Values can be positive, zero or negative numbers.
    offer: Optional[float] = None
    # Volatility index displayed in decimal format.
    volatility_index: Optional[float] = None
    # The reason when volatility index is not calculated.
    volatility_index_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BasisPriceAssessmentModel_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BasisPriceAssessmentModel_attributes
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BasisPriceAssessmentModel_attributes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "basisBid": lambda n : setattr(self, 'basis_bid', n.get_float_value()),
            "basisChangePct": lambda n : setattr(self, 'basis_change_pct', n.get_float_value()),
            "basisMidpoint": lambda n : setattr(self, 'basis_midpoint', n.get_float_value()),
            "basisOffer": lambda n : setattr(self, 'basis_offer', n.get_float_value()),
            "bid": lambda n : setattr(self, 'bid', n.get_float_value()),
            "changePct": lambda n : setattr(self, 'change_pct', n.get_float_value()),
            "createdForDate": lambda n : setattr(self, 'created_for_date', n.get_datetime_value()),
            "dataUsed": lambda n : setattr(self, 'data_used', n.get_str_value()),
            "diffToPrevBasisMid": lambda n : setattr(self, 'diff_to_prev_basis_mid', n.get_float_value()),
            "diffToPrevMid": lambda n : setattr(self, 'diff_to_prev_mid', n.get_float_value()),
            "isEstimate": lambda n : setattr(self, 'is_estimate', n.get_bool_value()),
            "midpoint": lambda n : setattr(self, 'midpoint', n.get_float_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "offer": lambda n : setattr(self, 'offer', n.get_float_value()),
            "volatilityIndex": lambda n : setattr(self, 'volatility_index', n.get_float_value()),
            "volatilityIndexReason": lambda n : setattr(self, 'volatility_index_reason', n.get_str_value()),
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
        writer.write_float_value("basisBid", self.basis_bid)
        writer.write_float_value("basisChangePct", self.basis_change_pct)
        writer.write_float_value("basisMidpoint", self.basis_midpoint)
        writer.write_float_value("basisOffer", self.basis_offer)
        writer.write_float_value("bid", self.bid)
        writer.write_float_value("changePct", self.change_pct)
        writer.write_datetime_value("createdForDate", self.created_for_date)
        writer.write_str_value("dataUsed", self.data_used)
        writer.write_float_value("diffToPrevBasisMid", self.diff_to_prev_basis_mid)
        writer.write_float_value("diffToPrevMid", self.diff_to_prev_mid)
        writer.write_bool_value("isEstimate", self.is_estimate)
        writer.write_float_value("midpoint", self.midpoint)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_float_value("offer", self.offer)
        writer.write_float_value("volatilityIndex", self.volatility_index)
        writer.write_str_value("volatilityIndexReason", self.volatility_index_reason)
        writer.write_additional_data_value(self.additional_data)
    

