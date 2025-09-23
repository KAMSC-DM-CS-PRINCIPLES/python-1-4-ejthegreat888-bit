# Power Algorithm Starter

This repository contains a starter template for implementing the power algorithm (x^n) as described in the algorithm specification.

## Algorithm Description

The algorithm calculates x^n where:
- `x` is a real number
- `n` is a positive integer
- The result is stored in variable `P`

### Algorithm Steps:
1. **Initialization**: Set `P = x` and `k = 1`
2. **Loop**: While `k < n`:
   - Multiply `P` by `x` (P = P * x)
   - Increment `k` by 1 (k = k + 1)
3. **Output**: Print `P`

## Assignment

Implement the `power(x, n)` function in `power.py` that follows the algorithm specification above.
