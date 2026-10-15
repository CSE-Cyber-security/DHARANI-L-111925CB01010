# Fibonacci Series

A Python program that prints the Fibonacci series for `n` terms.

## Folder Structure

```
fibonacci-series/
├── py/
│   └── fibonacci.py
└── output/
    └── output.png
```

## Code

```python
n = int(input("Enter the number of terms: "))

a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

## How to Run

```bash
python py/fibonacci.py
```

## Sample Input / Output

```
Enter the number of terms: 7
Fibonacci Series:
0 1 1 2 3 5 8
```

Screenshot: see `output/output.png`

## How It Works

Each loop prints the current term `a`, then moves the pair forward: `a` becomes `b`, and `b` becomes `a + b`.
