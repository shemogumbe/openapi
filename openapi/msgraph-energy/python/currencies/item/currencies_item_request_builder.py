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
    from ...models.currencies400_error import Currencies400Error
    from ...models.currencies401_error import Currencies401Error
    from ...models.currencies403_error import Currencies403Error
    from ...models.currencies404_error import Currencies404Error
    from ...models.currencies406_error import Currencies406Error
    from ...models.currencies429_error import Currencies429Error
    from ...models.currencies500_error import Currencies500Error
    from .currencies_get_response import CurrenciesGetResponse

class CurrenciesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /currencies/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CurrenciesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/currencies/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CurrenciesGetResponse]:
        """
        Returns a currency entity for a valid identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CurrenciesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.currencies400_error import Currencies400Error
        from ...models.currencies401_error import Currencies401Error
        from ...models.currencies403_error import Currencies403Error
        from ...models.currencies404_error import Currencies404Error
        from ...models.currencies406_error import Currencies406Error
        from ...models.currencies429_error import Currencies429Error
        from ...models.currencies500_error import Currencies500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Currencies400Error,
            "401": Currencies401Error,
            "403": Currencies403Error,
            "404": Currencies404Error,
            "406": Currencies406Error,
            "429": Currencies429Error,
            "500": Currencies500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .currencies_get_response import CurrenciesGetResponse

        return await self.request_adapter.send_async(request_info, CurrenciesGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a currency entity for a valid identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> CurrenciesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CurrenciesItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CurrenciesItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CurrenciesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

