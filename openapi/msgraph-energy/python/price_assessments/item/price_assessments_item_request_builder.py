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
    from ...models.price_assessments400_error import PriceAssessments400Error
    from ...models.price_assessments401_error import PriceAssessments401Error
    from ...models.price_assessments403_error import PriceAssessments403Error
    from ...models.price_assessments404_error import PriceAssessments404Error
    from ...models.price_assessments406_error import PriceAssessments406Error
    from ...models.price_assessments429_error import PriceAssessments429Error
    from ...models.price_assessments500_error import PriceAssessments500Error
    from .price_assessments_get_response import PriceAssessmentsGetResponse

class PriceAssessmentsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /priceAssessments/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PriceAssessmentsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/priceAssessments/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PriceAssessmentsGetResponse]:
        """
        Returns a price assessment entity for a valid identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PriceAssessmentsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.price_assessments400_error import PriceAssessments400Error
        from ...models.price_assessments401_error import PriceAssessments401Error
        from ...models.price_assessments403_error import PriceAssessments403Error
        from ...models.price_assessments404_error import PriceAssessments404Error
        from ...models.price_assessments406_error import PriceAssessments406Error
        from ...models.price_assessments429_error import PriceAssessments429Error
        from ...models.price_assessments500_error import PriceAssessments500Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": PriceAssessments400Error,
            "401": PriceAssessments401Error,
            "403": PriceAssessments403Error,
            "404": PriceAssessments404Error,
            "406": PriceAssessments406Error,
            "429": PriceAssessments429Error,
            "500": PriceAssessments500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .price_assessments_get_response import PriceAssessmentsGetResponse

        return await self.request_adapter.send_async(request_info, PriceAssessmentsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a price assessment entity for a valid identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> PriceAssessmentsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PriceAssessmentsItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PriceAssessmentsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PriceAssessmentsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

