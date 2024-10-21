class Fibonacci:
    def __init__ (self):
        self.memo = {}

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in self.memo:
            return self.memo[n]
        else:
            result = self.fibonacci(n - 1) + self.fibonacci(n - 2)
            self.memo[n] = result
            return result

# Example usage:
fibonacci_sequence = Fibonacci()
n = 10
print("Fibonacci sequence up to", n, ":", [fibonacci_sequence.fibonacci(i) for i in range(n)])