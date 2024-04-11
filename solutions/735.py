class Solution:
    """
    Use a stack to maintain the surviving asteroids depending on its direction.

    Time: O(n)
    Space: O(n)
    """

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                difference = stack[-1] + asteroid

                if difference == 0:
                    stack.pop()
                    asteroid = 0
                    # don't add the asteroid bc both asteroids cancelled out

                elif difference < 0:
                    stack.pop()
                    # need to add this left moving asteroid still

                else:
                    # don't add asteroid to stack because the left asteroid moving right is lager
                    asteroid = 0

            if asteroid != 0:
                stack.append(asteroid)
        return stack
