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
    from ..models.units400_error import Units400Error
    from ..models.units401_error import Units401Error
    from ..models.units403_error import Units403Error
    from ..models.units406_error import Units406Error
    from ..models.units429_error import Units429Error
    from ..models.units500_error import Units500Error
    from .item.units_item_request_builder import UnitsItemRequestBuilder
    from .units_get_response import UnitsGetResponse

class UnitsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /units
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new UnitsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/units{?page%5Bafter%5D*,page%5Bsize%5D*}", path_parameters)
    
    def by_id(self,id: str) -> UnitsItemRequestBuilder:
        """
        Gets an item from the GraphPythonv1.units.item collection
        param id: The Id of the measure unit for which the user wants to retrieve data.
        Returns: UnitsItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.units_item_request_builder import UnitsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return UnitsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[UnitsRequestBuilderGetQueryParameters]] = None) -> Optional[UnitsGetResponse]:
        """
        Returns a list of measure units sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnitsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.units400_error import Units400Error
        from ..models.units401_error import Units401Error
        from ..models.units403_error import Units403Error
        from ..models.units406_error import Units406Error
        from ..models.units429_error import Units429Error
        from ..models.units500_error import Units500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Units400Error,
            "401": Units401Error,
            "403": Units403Error,
            "406": Units406Error,
            "429": Units429Error,
            "500": Units500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .units_get_response import UnitsGetResponse

        return await self.request_adapter.send_async(request_info, UnitsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[UnitsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of measure units sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> UnitsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UnitsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return UnitsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class UnitsRequestBuilderGetQueryParameters():
        """
        Returns a list of measure units sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
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
    class UnitsRequestBuilderGetRequestConfiguration(RequestConfiguration[UnitsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

