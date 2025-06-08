def radix_sort(arr):
    # Step 1: Find the number with the most digits
    max_num = max(arr)
    max_digits = len(str(max_num))

    # Start from the least significant digit
    place = 1  # 1 -> units, 10 -> tens, 100 -> hundreds, etc.

    for _ in range(max_digits):
        # Create 10 empty buckets (lists) for digits 0-9
        buckets = [[] for _ in range(10)]

        # Step 2: Place each number in the corresponding bucket
        for num in arr:
            digit = (num // place) % 10
            buckets[digit].append(num)

        # Step 3: Flatten the list from buckets back to arr
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        # Move to next digit place (units → tens → hundreds)
        place *= 10

    return arr


