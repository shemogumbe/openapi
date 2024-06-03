from __future__ import annotations
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_serialization_form.form_parse_node_factory import FormParseNodeFactory
from kiota_serialization_form.form_serialization_writer_factory import FormSerializationWriterFactory
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_multipart.multipart_serialization_writer_factory import MultipartSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .basis_price_assessments.basis_price_assessments_request_builder import BasisPriceAssessmentsRequestBuilder
    from .currencies.currencies_request_builder import CurrenciesRequestBuilder
    from .data_events.data_events_request_builder import DataEventsRequestBuilder
    from .indices.indices_request_builder import IndicesRequestBuilder
    from .location_spreads.location_spreads_request_builder import LocationSpreadsRequestBuilder
    from .markets.markets_request_builder import MarketsRequestBuilder
    from .periods.periods_request_builder import PeriodsRequestBuilder
    from .price_assessments.price_assessments_request_builder import PriceAssessmentsRequestBuilder
    from .spark_and_dark_spreads.spark_and_dark_spreads_request_builder import SparkAndDarkSpreadsRequestBuilder
    from .trades.trades_request_builder import TradesRequestBuilder
    from .units.units_request_builder import UnitsRequestBuilder

class ApiClient(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new ApiClient and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_serializer(FormSerializationWriterFactory)
        register_default_serializer(MultipartSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
        register_default_deserializer(FormParseNodeFactory)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://api.icis.com/energy/v1"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def basis_price_assessments(self) -> BasisPriceAssessmentsRequestBuilder:
        """
        The basisPriceAssessments property
        """
        from .basis_price_assessments.basis_price_assessments_request_builder import BasisPriceAssessmentsRequestBuilder

        return BasisPriceAssessmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def currencies(self) -> CurrenciesRequestBuilder:
        """
        The currencies property
        """
        from .currencies.currencies_request_builder import CurrenciesRequestBuilder

        return CurrenciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_events(self) -> DataEventsRequestBuilder:
        """
        The dataEvents property
        """
        from .data_events.data_events_request_builder import DataEventsRequestBuilder

        return DataEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def indices(self) -> IndicesRequestBuilder:
        """
        The indices property
        """
        from .indices.indices_request_builder import IndicesRequestBuilder

        return IndicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def location_spreads(self) -> LocationSpreadsRequestBuilder:
        """
        The locationSpreads property
        """
        from .location_spreads.location_spreads_request_builder import LocationSpreadsRequestBuilder

        return LocationSpreadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def markets(self) -> MarketsRequestBuilder:
        """
        The markets property
        """
        from .markets.markets_request_builder import MarketsRequestBuilder

        return MarketsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def periods(self) -> PeriodsRequestBuilder:
        """
        The periods property
        """
        from .periods.periods_request_builder import PeriodsRequestBuilder

        return PeriodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price_assessments(self) -> PriceAssessmentsRequestBuilder:
        """
        The priceAssessments property
        """
        from .price_assessments.price_assessments_request_builder import PriceAssessmentsRequestBuilder

        return PriceAssessmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def spark_and_dark_spreads(self) -> SparkAndDarkSpreadsRequestBuilder:
        """
        The sparkAndDarkSpreads property
        """
        from .spark_and_dark_spreads.spark_and_dark_spreads_request_builder import SparkAndDarkSpreadsRequestBuilder

        return SparkAndDarkSpreadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trades(self) -> TradesRequestBuilder:
        """
        The trades property
        """
        from .trades.trades_request_builder import TradesRequestBuilder

        return TradesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def units(self) -> UnitsRequestBuilder:
        """
        The units property
        """
        from .units.units_request_builder import UnitsRequestBuilder

        return UnitsRequestBuilder(self.request_adapter, self.path_parameters)
    

