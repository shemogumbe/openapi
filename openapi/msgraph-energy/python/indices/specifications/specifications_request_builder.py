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
    from ...models.specifications400_error import Specifications400Error
    from ...models.specifications401_error import Specifications401Error
    from ...models.specifications403_error import Specifications403Error
    from ...models.specifications406_error import Specifications406Error
    from ...models.specifications429_error import Specifications429Error
    from ...models.specifications500_error import Specifications500Error
    from .item.specifications_item_request_builder import SpecificationsItemRequestBuilder
    from .specifications_get_response import SpecificationsGetResponse

class SpecificationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /indices/specifications
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SpecificationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/indices/specifications{?filter%5BcurrencyId%5D*,filter%5BmarketDeliveryProfileName%5D*,filter%5BmarketId%5D*,filter%5BunitId%5D*,page%5Bafter%5D*,page%5Bsize%5D*}", path_parameters)
    
    def by_id(self,id: str) -> SpecificationsItemRequestBuilder:
        """
        Gets an item from the GraphPythonv1.indices.specifications.item collection
        param id: The Id of the index specification for which the user wants to retrieve data.
        Returns: SpecificationsItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.specifications_item_request_builder import SpecificationsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return SpecificationsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SpecificationsRequestBuilderGetQueryParameters]] = None) -> Optional[SpecificationsGetResponse]:
        """
        Returns a list of index specifications sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SpecificationsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.specifications400_error import Specifications400Error
        from ...models.specifications401_error import Specifications401Error
        from ...models.specifications403_error import Specifications403Error
        from ...models.specifications406_error import Specifications406Error
        from ...models.specifications429_error import Specifications429Error
        from ...models.specifications500_error import Specifications500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Specifications400Error,
            "401": Specifications401Error,
            "403": Specifications403Error,
            "406": Specifications406Error,
            "429": Specifications429Error,
            "500": Specifications500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .specifications_get_response import SpecificationsGetResponse

        return await self.request_adapter.send_async(request_info, SpecificationsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SpecificationsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of index specifications sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> SpecificationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SpecificationsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SpecificationsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SpecificationsRequestBuilderGetQueryParameters():
        """
        Returns a list of index specifications sorted by `name` in ascending order. If there is no data, then an empty array will be returned.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "filtercurrency_id":
                return "filter%5BcurrencyId%5D"
            if original_name == "filtermarket_delivery_profile_name":
                return "filter%5BmarketDeliveryProfileName%5D"
            if original_name == "filtermarket_id":
                return "filter%5BmarketId%5D"
            if original_name == "filterunit_id":
                return "filter%5BunitId%5D"
            if original_name == "pageafter":
                return "page%5Bafter%5D"
            if original_name == "pagesize":
                return "page%5Bsize%5D"
            return original_name
        
        # Comma separated list of currency Ids for which the user wants to retrieve specifications.
        filtercurrency_id: Optional[str] = None

        # Comma separated list of market delivery profile names for which the user wants to retrieve data. Allowed values can be found in the corresponding API response model for this resource.
        filtermarket_delivery_profile_name: Optional[str] = None

        # Comma separated list of market Ids for which the user wants to retrieve specifications.
        filtermarket_id: Optional[str] = None

        # Comma separated list of measure unit Ids for which the user wants to retrieve specifications.
        filterunit_id: Optional[str] = None

        # To view the next page of results, use the value of the `links.next` field in the response. This field contains a Base64 encoded string that represents the cursor for the next page.
        pageafter: Optional[str] = None

        # The number of entities returned in a single page. The default page size is `1000` while the maximum is `5000`.
        pagesize: Optional[int] = None

    
    @dataclass
    class SpecificationsRequestBuilderGetRequestConfiguration(RequestConfiguration[SpecificationsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

