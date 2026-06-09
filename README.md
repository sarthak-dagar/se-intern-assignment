# Data Structures & Systems Design Assignment

## Problem 1: LRU Cache
Implemented an LRU Cache using:

- Hash Map
- Doubly Linked List

### Features

- O(1) get operation
- O(1) put operation
- Automatic least recently used eviction

### Complexity

- get() → O(1)
- put() → O(1)


## Problem 2: Event Scheduler
Implemented:

- `can_attend_all(events)`
- `min_rooms_required(events)`

### Features

- Detect overlapping meetings
- Calculate minimum meeting rooms required using a min-heap

### Complexity

- can_attend_all() → O(n log n) (sorting dominates)
- min_rooms_required() → O(n log n) (sorting + heap operations)


## Technologies Used

- Python 3
- Heap Queue
- Doubly Linked List
- Dictionary / HashMap


## How to Run

Run the examples from the project folder:

```bash
python lru_cache.py
python event_scheduler.py
```


## Output Examples

LRU Cache example prints:

```
Get 1: 10
Get 2: -1
```

Event Scheduler example prints:

```
Can attend all meetings: True
Minimum rooms required: 2
```


## Notes

- This repository is ready to be uploaded to GitHub. After creating a new repo (for example `se-intern-assignment`), initialize git in this folder, add files, commit, add remote, and push.
- Deployment is optional for this backend assignment; GitHub repo and clean README are sufficient for submission.
