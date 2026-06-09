import heapq


def can_attend_all(events):
    """Return True if a single person can attend all events (no overlaps)."""
    if not events:
        return True

    events.sort(key=lambda x: x[0])

    for i in range(1, len(events)):
        previous_end = events[i - 1][1]
        current_start = events[i][0]

        if current_start < previous_end:
            return False

    return True


def min_rooms_required(events):
    """Return minimum number of rooms required to hold all events."""
    if not events:
        return 0

    events.sort(key=lambda x: x[0])
    min_heap = []  # stores end times

    for start, end in events:
        if min_heap and start >= min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)

    return len(min_heap)


if __name__ == "__main__":
    # Example Usage
    events1 = [(9, 10), (10, 11), (11, 12)]
    print("Can attend all meetings:", can_attend_all(events1))

    events2 = [(1, 4), (2, 5), (7, 9)]
    print("Minimum rooms required:", min_rooms_required(events2))
