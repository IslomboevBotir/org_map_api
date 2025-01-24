from typing import Sequence, Any
from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseSerializer[V: Any, T: BaseModel](ABC):
    @abstractmethod
    def serialize(self, value: V, **kwargs) -> Sequence[T]:
        raise NotImplementedError


class BaseListSerializer[V: Any, T: BaseModel](ABC):
    @abstractmethod
    def serializer_list(self, value: V, **kwargs) -> Sequence[T]:
        raise NotImplementedError
