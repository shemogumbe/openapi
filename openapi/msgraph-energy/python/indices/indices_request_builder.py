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
    from ..models.indices400_error import Indices400Error
    from ..models.indices401_error import Indices401Error
    from ..models.indices403_error import Indices403Error
    from ..models.indices406_error import Indices406Error
    from ..models.indices429_error import Indices429Error
    from ..models.indices500_error import Indices500Error
    from .indices_get_response import IndicesGetResponse
    from .item.indices_item_request_builder import IndicesItemRequestBuilder
    from .specifications.specifications_request_builder import SpecificationsRequestBuilder

class IndicesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /indices
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new IndicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/indices{?filter%5BabsolutePeriodCode%5D*,filter%5BcreatedForDateEnd%5D*,filter%5BcreatedForDateStart%5D*,filter%5BrelativePeriodCode%5D*,filter%5BspecificationId%5D*,page%5Bafter%5D*,page%5Bsize%5D*}", path_parameters)
    
    def by_id(self,id: str) -> IndicesItemRequestBuilder:
        """
        Gets an item from the GraphPythonv1.indices.item collection
        param id: The Id of the index for which the user wants to retrieve data.
        Returns: IndicesItemRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .item.indices_item_request_builder import IndicesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return IndicesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IndicesRequestBuilderGetQueryParameters]] = None) -> Optional[IndicesGetResponse]:
        """
        Returns a list of indices sorted by `createdForDate` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IndicesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.indices400_error import Indices400Error
        from ..models.indices401_error import Indices401Error
        from ..models.indices403_error import Indices403Error
        from ..models.indices406_error import Indices406Error
        from ..models.indices429_error import Indices429Error
        from ..models.indices500_error import Indices500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Indices400Error,
            "401": Indices401Error,
            "403": Indices403Error,
            "406": Indices406Error,
            "429": Indices429Error,
            "500": Indices500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .indices_get_response import IndicesGetResponse

        return await self.request_adapter.send_async(request_info, IndicesGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IndicesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of indices sorted by `createdForDate` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> IndicesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IndicesRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return IndicesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def specifications(self) -> SpecificationsRequestBuilder:
        """
        The specifications property
        """
        from .specifications.specifications_request_builder import SpecificationsRequestBuilder

        return SpecificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IndicesRequestBuilderGetQueryParameters():
        """
        Returns a list of indices sorted by `createdForDate` in ascending order. If there is no data, then an empty array will be returned.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "filterabsolute_period_code":
                return "filter%5BabsolutePeriodCode%5D"
            if original_name == "filtercreated_for_date_end":
                return "filter%5BcreatedForDateEnd%5D"
            if original_name == "filtercreated_for_date_start":
                return "filter%5BcreatedForDateStart%5D"
            if original_name == "filterrelative_period_code":
                return "filter%5BrelativePeriodCode%5D"
            if original_name == "filterspecification_id":
                return "filter%5BspecificationId%5D"
            if original_name == "pageafter":
                return "page%5Bafter%5D"
            if original_name == "pagesize":
                return "page%5Bsize%5D"
            return original_name
        
        # Comma separated list of absolute period codes for which the user wants to retrieve data.
        filterabsolute_period_code: Optional[str] = None

        # The end range of the created for date filter. The format is yyyyMMdd.
        filtercreated_for_date_end: Optional[str] = None

        # The start range of the created for date filter. The format is yyyyMMdd.
        filtercreated_for_date_start: Optional[str] = None

        # Comma separated list of relative period codes for which the user wants to retrieve data.
        filterrelative_period_code: Optional[str] = None

        # Comma separated list of specification Ids for which the user wants to retrieve data.
        filterspecification_id: Optional[str] = None

        # To view the next page of results, use the value of the `links.next` field in the response. This field contains a Base64 encoded string that represents the cursor for the next page.
        pageafter: Optional[str] = None

        # The number of entities returned in a single page. The default page size is `1000` while the maximum is `5000`.
        pagesize: Optional[int] = None

    
    @dataclass
    class IndicesRequestBuilderGetRequestConfiguration(RequestConfiguration[IndicesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

