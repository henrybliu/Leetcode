from collections import defaultdict
import heapq

class FoodRatings:
    '''
    We can use 3 hashmaps to keep track of each food's most updated rating, the
    cuisine that each food belongs to, and each cuisine's existing ratings with
    corresponding food item. We can skip over old food ratings that are not
    updated by comparing the hashmaps holding the food's most recent rating
    and what is being popped from the max heap.

    Time: O(n) intialization, O(1) changeRating(), O(nlogn) for highest rated
    Space: O(n)
    '''

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # keep track of each food's most updated rating
        self.foodRating = defaultdict()
        # keep track of the cuisine of each food
        self.foodCuisine = defaultdict()
        # keep sorted order of each cuisine's max rating and food
        self.system = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodRating[food] = -rating
            self.foodCuisine[food] = cuisine
            heapq.heappush(self.system[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        # update the foods rating and add max heap for that cuisine
        self.foodRating[food] = -newRating
        cuisine = self.foodCuisine[food]
        heapq.heappush(self.system[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # remove food with ratings that are no longer valid
        while self.system[cuisine][0][0] != self.foodRating[self.system[cuisine][0][1]]:
            heapq.heappop(self.system[cuisine])

        return self.system[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)