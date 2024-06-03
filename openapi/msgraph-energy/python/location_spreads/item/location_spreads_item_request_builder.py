from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.location_spreads400_error import LocationSpreads400Error
    from ...models.location_spreads401_error import LocationSpreads401Error
    from ...models.location_spreads403_error import LocationSpreads403Error
    from ...models.location_spreads404_error import LocationSpreads404Error
    from ...models.location_spreads406_error import LocationSpreads406Error
    from ...models.location_spreads429_error import LocationSpreads429Error
    from ...models.location_spreads500_error import LocationSpreads500Error
    from .location_spreads_get_response import LocationSpreadsGetResponse

class LocationSpreadsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /locationSpreads/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new LocationSpreadsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/locationSpreads/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LocationSpreadsGetResponse]:
        """
        Returns a location spread entity for a valid identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LocationSpreadsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.location_spreads400_error import LocationSpreads400Error
        from ...models.location_spreads401_error import LocationSpreads401Error
        from ...models.location_spreads403_error import LocationSpreads403Error
        from ...models.location_spreads404_error import LocationSpreads404Error
        from ...models.location_spreads406_error import LocationSpreads406Error
        from ...models.location_spreads429_error import LocationSpreads429Error
        from ...models.location_spreads500_error import LocationSpreads500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": LocationSpreads400Error,
            "401": LocationSpreads401Error,
            "403": LocationSpreads403Error,
            "404": LocationSpreads404Error,
            "406": LocationSpreads406Error,
            "429": LocationSpreads429Error,
            "500": LocationSpreads500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .location_spreads_get_response import LocationSpreadsGetResponse

        return await self.request_adapter.send_async(request_info, LocationSpreadsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a location spread entity for a valid identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> LocationSpreadsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LocationSpreadsItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return LocationSpreadsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LocationSpreadsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

