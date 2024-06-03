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
    from ..models.data_events400_error import DataEvents400Error
    from ..models.data_events401_error import DataEvents401Error
    from ..models.data_events403_error import DataEvents403Error
    from ..models.data_events406_error import DataEvents406Error
    from ..models.data_events429_error import DataEvents429Error
    from ..models.data_events500_error import DataEvents500Error
    from .data_events_get_response import DataEventsGetResponse

class DataEventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /dataEvents
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DataEventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/dataEvents{?filter%5BcreatedAfter%5D*,filter%5BspecificationId%5D*,page%5Bafter%5D*,page%5Bsize%5D*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DataEventsRequestBuilderGetQueryParameters]] = None) -> Optional[DataEventsGetResponse]:
        """
        Returns a list of data events sorted by `eventCreationTime` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DataEventsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.data_events400_error import DataEvents400Error
        from ..models.data_events401_error import DataEvents401Error
        from ..models.data_events403_error import DataEvents403Error
        from ..models.data_events406_error import DataEvents406Error
        from ..models.data_events429_error import DataEvents429Error
        from ..models.data_events500_error import DataEvents500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": DataEvents400Error,
            "401": DataEvents401Error,
            "403": DataEvents403Error,
            "406": DataEvents406Error,
            "429": DataEvents429Error,
            "500": DataEvents500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .data_events_get_response import DataEventsGetResponse

        return await self.request_adapter.send_async(request_info, DataEventsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DataEventsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of data events sorted by `eventCreationTime` in ascending order. If there is no data, then an empty array will be returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> DataEventsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DataEventsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DataEventsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class DataEventsRequestBuilderGetQueryParameters():
        """
        Returns a list of data events sorted by `eventCreationTime` in ascending order. If there is no data, then an empty array will be returned.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "filtercreated_after":
                return "filter%5BcreatedAfter%5D"
            if original_name == "filterspecification_id":
                return "filter%5BspecificationId%5D"
            if original_name == "pageafter":
                return "page%5Bafter%5D"
            if original_name == "pagesize":
                return "page%5Bsize%5D"
            return original_name
        
        # The timestamp starting from which the data events need to be fetched. The format is yyyyMMddTHHmmssZ.
        filtercreated_after: Optional[str] = None

        # Comma separated list of specification Ids for which the user wants to retrieve data.
        filterspecification_id: Optional[str] = None

        # To view the next page of results, use the value of the `links.next` field in the response. This field contains a Base64 encoded string that represents the cursor for the next page.
        pageafter: Optional[str] = None

        # The number of entities returned in a single page. The default page size is `1000` while the maximum is `5000`.
        pagesize: Optional[int] = None

    
    @dataclass
    class DataEventsRequestBuilderGetRequestConfiguration(RequestConfiguration[DataEventsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

