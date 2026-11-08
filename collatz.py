#!/usr/bin/env python3
"""Print the Collatz sequence starting at 27 and the number of steps to reach 1."""


def collatz(n):
    """Return the Collatz sequence from n down to 1, inclusive."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for value in sequence:
        print(value)
    # One step per transformation; the starting value is not a step.
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
