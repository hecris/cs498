# Adversary Implementation
## Importing the Adversary class
```
from adversary import Adversary
```

## Interface
### Constructor
```
n = 10
A = Adversary(n)
```

### swap
```
Takes two indices and performs a swap.

Params:
  i: int
  j: int

Returns:
  A list of at most 2 integers containing the indices
  that are frozen following the swap.

froze = A.swap(0, 1) # possible outputs: [], [0], [1], [0, 1]
```

### original\_array
```
Returns:
  An input that is consistent with the swaps so far.

print(A.original_array()) # example output: [5, 6, 7, 8, 9, 4, 3, 2, 1, 0]
```

## Example Usage
See [deter\_player.py](./deter_player.py), which implements a deterministic algorithm
that "plays against" the adversary.
