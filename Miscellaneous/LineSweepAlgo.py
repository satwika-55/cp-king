def max_overlapping_intervals(intervals):
    events = []
    
    # Add start and end events to the event list
    for interval in intervals:
        start, end = interval
        events.append((start, 'start'))
        events.append((end, 'end'))
    
    # Sort events first by time, and then by type ('end' before 'start' to correctly handle ties)
    events.sort(key=lambda x: (x[0], x[1] == 'start'))
    
    max_overlap = 0
    current_overlap = 0
    
    # Sweep through the events
    for event in events:
        if event[1] == 'start':
            current_overlap += 1  # Increase overlap when an interval starts
            max_overlap = max(max_overlap, current_overlap)  # Update max overlap if needed
        else:
            current_overlap -= 1  # Decrease overlap when an interval ends
    
    return max_overlap

# Example usage
intervals = [(1, 4), (2, 5), (9, 12), (5, 9), (5, 12)]
print(max_overlapping_intervals(intervals))  # Output: 3

