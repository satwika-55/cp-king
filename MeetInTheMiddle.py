
# to find the closet value <= target

def meet_in_middle_subset_sum(arr, target):
    n = len(arr)
    half = n // 2
    left = arr[:half]
    right = arr[half:]

    def all_sums(subarr):
        sums = []
        for r in range(len(subarr) + 1):
            for comb in combinations(subarr, r):
                sums.append(sum(comb))
        return sums

    left_sums = all_sums(left)
    right_sums = all_sums(right)
    right_sums.sort()

    for s in left_sums:
        rem = target - s
        idx = bisect.bisect_left(right_sums, rem)
        if idx < len(right_sums) and right_sums[idx] == rem:
            return True

    return False

