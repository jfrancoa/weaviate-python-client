from typing import Generic, List, Optional

from weaviate.collections.classes.filters import (
    _Filters,
)
from weaviate.collections.classes.grpc import METADATA, HybridFusion, Rerank
from weaviate.collections.classes.internal import (
    QueryReturn,
    ReturnProperties,
    ReturnReferences,
    _QueryOptions,
    References,
    TReferences,
)
from weaviate.collections.classes.types import Properties, TProperties
from weaviate.collections.queries.base import _BaseQuery


class _HybridQuery(Generic[Properties, References], _BaseQuery[Properties, References]):
    def hybrid(
        self,
        query: str,
        *,
        alpha: float = 0.5,
        vector: Optional[List[float]] = None,
        query_properties: Optional[List[str]] = None,
        fusion_type: Optional[HybridFusion] = None,
        limit: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        rerank: Optional[Rerank] = None,
        include_vector: bool = False,
        return_metadata: Optional[METADATA] = None,
        return_properties: Optional[ReturnProperties[TProperties]] = None,
        return_references: Optional[ReturnReferences[TReferences]] = None,
    ) -> QueryReturn[Properties, References, TProperties, TReferences]:
        """Search for objects in this collection using the hybrid algorithm blending keyword-based BM25 and vector-based similarity.

        See the [docs](https://weaviate.io/developers/weaviate/search/hybrid) for a more detailed explanation.

        Arguments:
            `query`
                The keyword-based query to search for, REQUIRED.
            `alpha`
                The weight of the BM25 score. If not specified, the default weight specified by the server is used.
            `vector`
                The specific vector to search for. If not specified, the query is vectorised and used in the similarity search.
            `query_properties`
                The properties to search in. If not specified, all properties are searched.
            `fusion_type`
                The type of fusion to apply. If not specified, the default fusion type specified by the server is used.
            `limit`
                The maximum number of results to return. If not specified, the default limit specified by the server is returned.
            `auto_limit`
                The maximum number of [autocut](https://weaviate.io/developers/weaviate/api/graphql/additional-operators#autocut) results to return. If not specified, no limit is applied.
            `filters`
                The filters to apply to the search.
            `rerank`
                How the results should be reranked. NOTE: A `rerank-*` module must be enabled for this functionality to work.
            `include_vector`
                Whether to include the vector in the results. If not specified, this is set to False.
            `return_metadata`
                The metadata to return for each object, defaults to `None`.
            `return_properties`
                The properties to return for each object.
            `return_references`
                The references to return for each object.

        NOTE:
            - If `return_properties` is not provided then all properties are returned except for blob properties.
            - If `return_metadata` is not provided then no metadata is provided.
            - If `return_references` is not provided then no references are provided.

        Returns:
            A `_QueryReturn` object that includes the searched objects.

        Raises:
            `weaviate.exceptions.WeaviateQueryException`:
                If the network connection to Weaviate fails.
        """
        res = self._query().hybrid(
            query=query,
            alpha=alpha,
            vector=vector,
            properties=query_properties,
            fusion_type=fusion_type,
            limit=limit,
            autocut=auto_limit,
            filters=filters,
            rerank=rerank,
            return_metadata=self._parse_return_metadata(return_metadata, include_vector),
            return_properties=self._parse_return_properties(return_properties),
            return_references=self._parse_return_references(return_references),
        )
        return self._result_to_query_return(
            res,
            _QueryOptions.from_input(
                return_metadata,
                return_properties,
                include_vector,
                self._references,
                return_references,
                rerank,
            ),
            return_properties,
            return_references,
        )
