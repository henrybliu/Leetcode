class Solution:
    '''
    Sort the cars by their position then speed and in reverse so we start with the cars that are furthest back. This is to simulate cars that are further back running into cars that are ahead. Use a stack to keep track of each "convoy" of cars.

    Time: O(n)
    Space: O(n)
    '''
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def timeLeft(pos, mph):
            return (target - pos)/mph

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)

        stack = []
        for i in range(len(cars)):
            time = timeLeft(cars[i][0], cars[i][1])
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)

        return len(stack)