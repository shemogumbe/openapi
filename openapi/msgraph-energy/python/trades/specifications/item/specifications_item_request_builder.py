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
    from ....models.specifications400_error import Specifications400Error
    from ....models.specifications401_error import Specifications401Error
    from ....models.specifications403_error import Specifications403Error
    from ....models.specifications404_error import Specifications404Error
    from ....models.specifications406_error import Specifications406Error
    from ....models.specifications429_error import Specifications429Error
    from ....models.specifications500_error import Specifications500Error
    from .specifications_get_response import SpecificationsGetResponse

class SpecificationsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /trades/specifications/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SpecificationsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/trades/specifications/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SpecificationsGetResponse]:
        """
        Returns a trade specification entity for a valid identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SpecificationsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.specifications400_error import Specifications400Error
        from ....models.specifications401_error import Specifications401Error
        from ....models.specifications403_error import Specifications403Error
        from ....models.specifications404_error import Specifications404Error
        from ....models.specifications406_error import Specifications406Error
        from ....models.specifications429_error import Specifications429Error
        from ....models.specifications500_error import Specifications500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Specifications400Error,
            "401": Specifications401Error,
            "403": Specifications403Error,
            "404": Specifications404Error,
            "406": Specifications406Error,
            "429": Specifications429Error,
            "500": Specifications500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .specifications_get_response import SpecificationsGetResponse

        return await self.request_adapter.send_async(request_info, SpecificationsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a trade specification entity for a valid identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> SpecificationsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SpecificationsItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SpecificationsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SpecificationsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

