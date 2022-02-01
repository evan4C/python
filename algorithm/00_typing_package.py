# Using mypy filename.py to check if there is any typing error.

# Variable.
x: int = 1

# The following code didn't throw an error BC typing annotation is just a hint not mandatory.
y: str = 10

# Function with a return value.
def add_numbers(a: int, b: int, c: int) -> int:
    return a + b + c

# Function without a return value.
def add_numbers2(a: int, b: int, c: int) -> None:
    print(a + b + c)

# List, Dict, Set, Tuple
from typing import List, Dict, Set, Tuple  # import the related structure first
list_test: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dict_test: Dict[str, str] = {'a': 'b'}
set_test: Set[str, str] = {'c', 'd'}
tuple_test: Tuple[int, int, int] = (1, 2, 3)  # need to indicate all the elements.

# Customize type
Vector = List[float]
def foo(v: Vector) -> Vector:
    return v

# Optional type
from typing import Optional
def foo2(output: Optional[bool] = False):
    return output

# Any type
from typing import Any
def foo3(output: Any):
    return output

# Sequence (string, list, or tuple)
from typing import Sequence
def foo4(seq: Sequence[str]):
    return seq

foo4(('a', 'b', 'c'))  # OK
foo4(['a', 'b', 'c'])  # OK
foo4(1)  # NG

# Callable type
from typing import Callable
def my_add(x: int, y: float) -> float:
    return x + y

def foo5(func: Callable[[int, float], float]) -> None:
    func(1, 2)

# Generic type: a placeholder
from typing import TypeVar
T = TypeVar('T')

# I don't care which type T is, but I want to make sure the element of the list and the return value have the same type.
def get_item(lst: List[T], index: int) -> T:
    return lst[index]


