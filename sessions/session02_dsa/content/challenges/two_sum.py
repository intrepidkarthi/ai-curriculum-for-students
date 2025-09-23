"""Two Sum variants."""
from typing import List, Tuple

def two_sum_indices(nums: List[int], target: int) -> Tuple[int, int] | None:
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    return None
