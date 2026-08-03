#exercise 1.......................


def total(nums):
   
    if len(nums) == 0:
        return 0

  
    return nums[0] + total(nums[1:])


def count_down(n):
  
    if n <= 0:
        return

    print(n)
    count_down(n - 1)



numbers = [100, 250, 400]

print("Numbers:", numbers)
print("Total:", total(numbers))

print("\nCountdown:")
count_down(5)

#exercise ...............................2


def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



balances = [100, 250, 400, 550, 700]

print("\nBalances:", balances)
print("Index of 400:", binary_search(balances, 400))
print("Index of 800:", binary_search(balances, 800))

#exercise ............................3 



def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)



numbers = [8, 2, 9, 1, 5, 7]

print("\nOriginal:", numbers)
print("Merge Sort:", merge_sort(numbers))
print("Built-in Sorted:", sorted(numbers))

#exercise ....................... 4



accounts = [
    ("Abel", 700),
    ("Sara", 1200),
    ("John", 500),
    ("Liya", 900)
]

sorted_accounts = sorted(
    accounts,
    key=lambda account: account[1],
    reverse=True
)

print("\nSorted Accounts:")
for name, balance in sorted_accounts:
    print(name, balance)

#exercise 5 ...................................


def has_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False



numbers = [2, 4, 6, 8, 10]

print("\nNumbers:", numbers)
print("Target 12:", has_pair(numbers, 12))
print("Target 9:", has_pair(numbers, 9))    