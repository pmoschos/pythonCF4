from typing import Sequence, TypeVar, List, Any, Optional

# Declare Generic Type Variable
T = TypeVar('T')

AnyStr = TypeVar('AnyStr', int, float)

# generic function
def first(seq: Sequence[T]) -> T:
    return seq[0]

# generic function
def last(seq: Sequence[T]) -> T:
    return seq[-1]

def count_truthy(elements: List[Any]) -> int:
    return sum(1 for element in elements if element)

def len_str(s: Optional[str] = None) -> int:
    if s is None: return 0
    return len(s)
