class MyCalendarTwo:
    """
    Use two arrays to keep track of the overlapping and non-overlapping
    intervals. We first check the already overlapping intervals for if a third
    booking is formed. If there are none, we check if any new double bookings
    can be formed. Finally, we save the booking.

    Notice that we can check for overlap using the contrapositive -- by
    checking if two intervals do not start/end before the other
    """

    def __init__(self):
        self.singleBooked = []
        self.doubleBooked = []

    def book(self, start: int, end: int) -> bool:
        for doubleStart, doubleEnd in self.doubleBooked:
            if not (end <= doubleStart or doubleEnd <= start):
                return False

        # check if there is any overlap
        for singleStart, singleEnd in self.singleBooked:
            if not (end <= singleStart or singleEnd <= start):
                self.doubleBooked.append((max(start, singleStart), min(end, singleEnd)))

        # save the booking
        self.singleBooked.append((start, end))

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
