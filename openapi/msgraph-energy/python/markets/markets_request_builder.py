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
    from ..models.markets400_error import Markets400Error
    from ..models.markets401_error import Markets401Error
    from ..models.markets403_error import Markets403Error
    from ..models.markets406_error import Markets406Error
    from ..models.markets429_error import Markets429Error
    from ..models.markets500_error import Markets500Error
    from .item.markets_item_request_builder import MarketsItemRequestBuilder
    from .markets_get_response import MarketsGetResponse

class MarketsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /markets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MarketsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/markets{?page%5Bafter%5D*,page%5Bsize%5D*}", path_parameters)
    
    def by_id(self,id: str) -> MarketsItemRequestBuilder:
        """
        Gets an item from the GraphPythonv1.markets.item collection
        param id: The Id of the market for which the user wants to retrieve data.
        Returns: MarketsItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.markets_item_request_builder import MarketsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return MarketsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MarketsRequestBuilderGetQueryParameters]] = None) -> Optional[MarketsGetResponse]:
        """
        Returns a list of markets sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MarketsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.markets400_error import Markets400Error
        from ..models.markets401_error import Markets401Error
        from ..models.markets403_error import Markets403Error
        from ..models.markets406_error import Markets406Error
        from ..models.markets429_error import Markets429Error
        from ..models.markets500_error import Markets500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Markets400Error,
            "401": Markets401Error,
            "403": Markets403Error,
            "406": Markets406Error,
            "429": Markets429Error,
            "500": Markets500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .markets_get_response import MarketsGetResponse

        return await self.request_adapter.send_async(request_info, MarketsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MarketsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of markets sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> MarketsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MarketsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return MarketsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MarketsRequestBuilderGetQueryParameters():
        """
        Returns a list of markets sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "pageafter":
                return "page%5Bafter%5D"
            if original_name == "pagesize":
                return "page%5Bsize%5D"
            return original_name
        
        # To view the next page of results, use the value of the `links.next` field in the response. This field contains a Base64 encoded string that represents the cursor for the next page.
        pageafter: Optional[str] = None

        # The number of entities returned in a single page. The default page size is `1000` while the maximum is `5000`.
        pagesize: Optional[int] = None

    
    @dataclass
    class MarketsRequestBuilderGetRequestConfiguration(RequestConfiguration[MarketsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

