# E-commerce System: Search Customer Account IDs

def linear_search(ids, target):
    for i in ids:
        if i == target:
            return True
    return False

def binary_search(ids, target):
    low, high = 0, len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == target:
            return True
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

ids = [101, 105, 108, 110, 115, 120]
target = 110

print("Linear Search:", "Found" if linear_search(ids, target) else "Not Found")
print("Binary Search:", "Found" if binary_search(ids, target) else "Not Found")

"""
⏱️ Time Complexity:
Linear Search → O(n)
Binary Search → O(log n)

💾 Space Complexity: O(1)
"""
