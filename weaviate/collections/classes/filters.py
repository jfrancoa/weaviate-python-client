from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional, Union

from weaviate.types import UUID
from weaviate.proto.v1 import search_get_pb2
from weaviate.util import get_valid_uuid

DATE = Union[datetime, int]


class _Operator(str, Enum):
    EQUAL = "Equal"
    NOT_EQUAL = "NotEqual"
    LESS_THAN = "LessThan"
    LESS_THAN_EQUAL = "LessThanEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_EQUAL = "GreaterThanEqual"
    LIKE = "Like"
    IS_NULL = "IsNull"
    CONTAINS_ANY = "ContainsAny"
    CONTAINS_ALL = "ContainsAll"
    AND = "And"
    OR = "Or"

    def _to_grpc(self) -> search_get_pb2.Filters.Operator:
        if self == _Operator.EQUAL:
            return search_get_pb2.Filters.OPERATOR_EQUAL
        elif self == _Operator.NOT_EQUAL:
            return search_get_pb2.Filters.OPERATOR_NOT_EQUAL
        elif self == _Operator.LESS_THAN:
            return search_get_pb2.Filters.OPERATOR_LESS_THAN
        elif self == _Operator.LESS_THAN_EQUAL:
            return search_get_pb2.Filters.OPERATOR_LESS_THAN_EQUAL
        elif self == _Operator.GREATER_THAN:
            return search_get_pb2.Filters.OPERATOR_GREATER_THAN
        elif self == _Operator.GREATER_THAN_EQUAL:
            return search_get_pb2.Filters.OPERATOR_GREATER_THAN_EQUAL
        elif self == _Operator.LIKE:
            return search_get_pb2.Filters.OPERATOR_LIKE
        elif self == _Operator.IS_NULL:
            return search_get_pb2.Filters.OPERATOR_IS_NULL
        elif self == _Operator.CONTAINS_ANY:
            return search_get_pb2.Filters.OPERATOR_CONTAINS_ANY
        elif self == _Operator.CONTAINS_ALL:
            return search_get_pb2.Filters.OPERATOR_CONTAINS_ALL
        elif self == _Operator.AND:
            return search_get_pb2.Filters.OPERATOR_AND
        elif self == _Operator.OR:
            return search_get_pb2.Filters.OPERATOR_OR
        else:
            raise ValueError(f"Unknown operator {self}")


class _Filters:
    def __and__(self, other: "_Filters") -> "_FilterAnd":
        return _FilterAnd(self, other)

    def __or__(self, other: "_Filters") -> "_FilterOr":
        return _FilterOr(self, other)


class _FilterAnd(_Filters):
    def __init__(self, *args: _Filters):
        self.filters: List[_Filters] = list(args)

    # replace with the following once 3.11 is the minimum version
    #     Operator: weaviate_pb2.Filters.OperatorType = weaviate_pb2.Filters.OperatorAnd
    @property
    def operator(self) -> _Operator:
        return _Operator.AND


class _FilterOr(_Filters):
    def __init__(self, *args: _Filters):
        self.filters: List[_Filters] = list(args)

    # replace with the following once 3.11 is the minimum version
    #     Operator: weaviate_pb2.Filters.OperatorType = weaviate_pb2.Filters.OperatorOr
    @property
    def operator(self) -> _Operator:
        return _Operator.OR


FilterValuesList = Union[List[str], List[bool], List[int], List[float], List[datetime], List[UUID]]
FilterValues = Union[int, float, str, bool, datetime, UUID, None, FilterValuesList]


@dataclass
class _FilterValue(_Filters):
    path: Union[str, List[str]]
    value: FilterValues
    operator: _Operator


class Filter:
    """Define a filter based on a property to be used when querying a collection.

    Use the `__init__` method to define the path to the property to be filtered on and then
    use the methods of this class to define the condition to filter on.

    To combine multiple filters, you can use `&` or `|` operators for each `AND` or `OR` operations, e.g.,
        `Filter("name").equal("John") & Filter("age").greater_than(18)`

    See [the docs](https://weaviate.io/developers/weaviate/search/filters) for more details!
    """

    def __init__(self, path: Union[str, List[str]], length: bool = False):
        """Initialise the filter.

        Arguments:
            `path`
                The path to the property to be filtered on.
                    This can be a single string in the case of a top-level property or a list of strings in the case of a nested cross-ref property.
            `length`
                If `True`, the length of the property will be used in the filter. Defaults to `False`.
                    This is only valid for properties of type `string` or `text`. The inverted index must also be configured to index the property length.
        """
        if isinstance(path, str):
            path = [path]
        if length:
            path[-1] = "len(" + path[-1] + ")"
        self.__internal_path = path

    def is_none(self, val: bool) -> _FilterValue:
        """Filter on whether the property is `None`."""
        return _FilterValue(path=self.__internal_path, value=val, operator=_Operator.IS_NULL)

    def contains_any(self, val: FilterValuesList) -> _FilterValue:
        """Filter on whether the property contains any of the given values."""
        return _FilterValue(
            path=self.__internal_path,
            value=val,
            operator=_Operator.CONTAINS_ANY,
        )

    def contains_all(self, val: FilterValuesList) -> _FilterValue:
        """Filter on whether the property contains all of the given values."""
        return _FilterValue(
            path=self.__internal_path,
            value=val,
            operator=_Operator.CONTAINS_ALL,
        )

    def equal(self, val: FilterValues) -> _FilterValue:
        """Filter on whether the property is equal to the given value."""
        return _FilterValue(path=self.__internal_path, value=val, operator=_Operator.EQUAL)

    def not_equal(self, val: FilterValues) -> _FilterValue:
        """Filter on whether the property is not equal to the given value."""
        return _FilterValue(path=self.__internal_path, value=val, operator=_Operator.NOT_EQUAL)

    def less_than(self, val: FilterValues) -> _FilterValue:
        """Filter on whether the property is less than the given value."""
        return _FilterValue(path=self.__internal_path, value=val, operator=_Operator.LESS_THAN)

    def less_or_equal(self, val: FilterValues) -> _FilterValue:
        """Filter on whether the property is less than or equal to the given value."""
        return _FilterValue(
            path=self.__internal_path,
            value=val,
            operator=_Operator.LESS_THAN_EQUAL,
        )

    def greater_than(self, val: FilterValues) -> _FilterValue:
        """Filter on whether the property is greater than the given value."""
        return _FilterValue(
            path=self.__internal_path,
            value=val,
            operator=_Operator.GREATER_THAN,
        )

    def greater_or_equal(self, val: FilterValues) -> _FilterValue:
        """Filter on whether the property is greater than or equal to the given value."""
        return _FilterValue(
            path=self.__internal_path,
            value=val,
            operator=_Operator.GREATER_THAN_EQUAL,
        )

    def like(self, val: str) -> _FilterValue:
        """Filter on whether the property is like the given value.

        This filter can make use of `*` and `?` as wildcards. See [the docs](https://weaviate.io/developers/weaviate/search/filters#by-partial-matches-text) for more details.
        """
        return _FilterValue(path=self.__internal_path, value=val, operator=_Operator.LIKE)


class _FilterId:
    @staticmethod
    def contains_any(
        uuids: List[UUID], on_reference_path: Optional[List[str]] = None
    ) -> _FilterValue:
        """Filter for objects that has one of the given ID."""
        return _FilterValue(
            path=_FilterId._prepare_path(path=on_reference_path),
            value=[get_valid_uuid(val) for val in uuids],
            operator=_Operator.CONTAINS_ANY,
        )

    @staticmethod
    def equal(uuid: UUID, on_reference_path: Optional[List[str]] = None) -> _FilterValue:
        """Filter for object that has the given ID."""
        return _FilterValue(
            path=_FilterId._prepare_path(path=on_reference_path),
            value=get_valid_uuid(uuid),
            operator=_Operator.EQUAL,
        )

    @staticmethod
    def not_equal(uuid: UUID, on_reference_path: Optional[List[str]] = None) -> _FilterValue:
        """Filter our object that has the given ID."""
        return _FilterValue(
            path=_FilterId._prepare_path(path=on_reference_path),
            value=get_valid_uuid(uuid),
            operator=_Operator.NOT_EQUAL,
        )

    @staticmethod
    def _prepare_path(path: Optional[List[str]]) -> List[str]:
        return path or [] + ["_id"]


class _FilterTime:
    _internal_path: Optional[List[str]] = None

    @staticmethod
    def contains_any(
        dates: List[DATE], on_reference_path: Optional[List[str]] = None
    ) -> _FilterValue:
        """Filter for objects that have one of the given Times."""
        return _FilterValue(
            path=_FilterCreationTime._prepare_path(path=on_reference_path),
            value=[_FilterCreationTime._convert_date(date) for date in dates],
            operator=_Operator.CONTAINS_ANY,
        )

    @staticmethod
    def equal(date: DATE, on_reference_path: Optional[List[str]] = None) -> _FilterValue:
        """Filter for objects that have the given time."""
        return _FilterValue(
            path=_FilterCreationTime._prepare_path(path=on_reference_path),
            value=_FilterCreationTime._convert_date(date),
            operator=_Operator.EQUAL,
        )

    @staticmethod
    def not_equal(date: DATE, on_reference_path: Optional[List[str]] = None) -> _FilterValue:
        """Filter our objects that have the given time."""
        return _FilterValue(
            path=_FilterCreationTime._prepare_path(path=on_reference_path),
            value=_FilterCreationTime._convert_date(date),
            operator=_Operator.NOT_EQUAL,
        )

    @staticmethod
    def less_than(date: DATE, on_reference_path: Optional[List[str]] = None) -> _FilterValue:
        """Filter on whether the time is less than the given value."""
        return _FilterValue(
            path=_FilterCreationTime._prepare_path(path=on_reference_path),
            value=_FilterCreationTime._convert_date(date),
            operator=_Operator.LESS_THAN,
        )

    @staticmethod
    def less_or_equal(date: DATE, on_reference_path: Optional[List[str]] = None) -> _FilterValue:
        """Filter on whether the time is less than or equal to the given value."""
        return _FilterValue(
            path=_FilterCreationTime._prepare_path(path=on_reference_path),
            value=_FilterCreationTime._convert_date(date),
            operator=_Operator.LESS_THAN_EQUAL,
        )

    @staticmethod
    def greater_than(date: DATE, on_reference_path: Optional[List[str]] = None) -> _FilterValue:
        """Filter on whether the time is greater than the given value."""
        return _FilterValue(
            path=_FilterCreationTime._prepare_path(path=on_reference_path),
            value=_FilterCreationTime._convert_date(date),
            operator=_Operator.GREATER_THAN,
        )

    @staticmethod
    def greater_or_equal(date: DATE, on_reference_path: Optional[List[str]] = None) -> _FilterValue:
        """Filter on whether the time is greater than or equal to the given value."""
        return _FilterValue(
            path=_FilterCreationTime._prepare_path(path=on_reference_path),
            value=_FilterCreationTime._convert_date(date),
            operator=_Operator.GREATER_THAN_EQUAL,
        )

    @staticmethod
    def _prepare_path(path: Optional[List[str]]) -> List[str]:
        internal_path = _FilterTime._internal_path
        assert internal_path is not None
        return path or [] + internal_path

    @staticmethod
    def _convert_date(date: DATE) -> datetime:
        if isinstance(date, datetime):
            return date
        # weaviate returns a different timestamp format
        return datetime.fromtimestamp(date / 1000, tz=timezone.utc)


class _FilterCreationTime(_FilterTime):
    _FilterTime._internal_path = ["_creationTimeUnix"]


class _FilterUpdateTime(_FilterTime):
    _FilterTime._internal_path = ["_creationTimeUnix"]


class FilterMetadata:
    """Define a filter based on a property to be used when querying a collection.

    Use the `__init__` method to define the path to the property to be filtered on and then
    use the methods of this class to define the condition to filter on.

    To combine multiple filters, you can use `&` or `|` operators for each `AND` or `OR` operations, e.g.,
        `Filter("name").equal("John") & Filter("age").greater_than(18)`

    See [the docs](https://weaviate.io/developers/weaviate/search/filters) for more details!
    """

    FilterById = _FilterId
    FilterByCreationTime = _FilterCreationTime
    FilterByUpdateTime = _FilterUpdateTime
