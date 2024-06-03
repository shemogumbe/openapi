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
    from ..models.periods400_error import Periods400Error
    from ..models.periods401_error import Periods401Error
    from ..models.periods403_error import Periods403Error
    from ..models.periods406_error import Periods406Error
    from ..models.periods429_error import Periods429Error
    from ..models.periods500_error import Periods500Error
    from .item.periods_item_request_builder import PeriodsItemRequestBuilder
    from .periods_get_response import PeriodsGetResponse

class PeriodsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /periods
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PeriodsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/periods{?page%5Bafter%5D*,page%5Bsize%5D*}", path_parameters)
    
    def by_id(self,id: str) -> PeriodsItemRequestBuilder:
        """
        Gets an item from the GraphPythonv1.periods.item collection
        param id: The Id of the period for which the user wants to retrieve data.
        Returns: PeriodsItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.periods_item_request_builder import PeriodsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PeriodsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PeriodsRequestBuilderGetQueryParameters]] = None) -> Optional[PeriodsGetResponse]:
        """
        Returns a list of periods sorted by `referenceDate` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PeriodsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.periods400_error import Periods400Error
        from ..models.periods401_error import Periods401Error
        from ..models.periods403_error import Periods403Error
        from ..models.periods406_error import Periods406Error
        from ..models.periods429_error import Periods429Error
        from ..models.periods500_error import Periods500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Periods400Error,
            "401": Periods401Error,
            "403": Periods403Error,
            "406": Periods406Error,
            "429": Periods429Error,
            "500": Periods500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .periods_get_response import PeriodsGetResponse

        return await self.request_adapter.send_async(request_info, PeriodsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PeriodsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of periods sorted by `referenceDate` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> PeriodsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PeriodsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PeriodsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PeriodsRequestBuilderGetQueryParameters():
        """
        Returns a list of periods sorted by `referenceDate` in ascending order. If there is no data, then an empty array will be returned.
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
    class PeriodsRequestBuilderGetRequestConfiguration(RequestConfiguration[PeriodsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

