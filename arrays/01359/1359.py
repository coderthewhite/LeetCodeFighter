class Solution:
    def countOrders(self, n: int) -> int: 
        """
        n! * (1 * 2 * 3 * (2n - 1))
        n == 3
            ==> (1 * 2 * 3) * (1 * 3 * 5)
                ==> 1 * 1 * 2 * 3 * 3 * 5
        result = 1
        for i: 1 to n
            result *= i * (2*n - 1)
        """
        result = 1
        modulo = 10 ** 9 + 7
        for index in range(1, n + 1):
            result *= index * (2 * index - 1)
        return result % modulo