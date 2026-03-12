import time
import random

def count_distinct_dict(arr):
    """Count distinct integers using dictionary"""
    return len({x: True for x in arr})

def count_distinct_set(arr):
    """Count distinct integers using set"""
    return len(set(arr))

def count_distinct_sort(arr):
    """Count distinct integers using sorting"""
    if not arr:
        return 0
    
    sorted_arr = sorted(arr)
    distinct = 1
    
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[i-1]:
            distinct += 1
    
    return distinct

def generate_random_array(size, max_value=1000000):
    """Generate random array of given size"""
    return [random.randint(1, max_value) for _ in range(size)]

def test_performance():
    """Test and compare performance of different algorithms"""
    sizes = [1000, 100000, 1000000]
    
    print("=" * 70)
    print(f"{'Size':<12} {'Method':<20} {'Time (s)':<15} {'Result':<10}")
    print("=" * 70)
    
    for size in sizes:
        arr = generate_random_array(size)
        
        # Test dictionary method
        start = time.time()
        result_dict = count_distinct_dict(arr)
        time_dict = time.time() - start
        
        # Test set method (alternative approach)
        start = time.time()
        result_set = count_distinct_set(arr)
        time_set = time.time() - start
        
        # Test sorting method
        start = time.time()
        result_sort = count_distinct_sort(arr)
        time_sort = time.time() - start
        
        print(f"{size:<12} {'Dictionary':<20} {time_dict:<15.6f} {result_dict:<10}")
        print(f"{size:<12} {'Set':<20} {time_set:<15.6f} {result_set:<10}")
        print(f"{size:<12} {'Sorting':<20} {time_sort:<15.6f} {result_sort:<10}")
        print("-" * 70)

if __name__ == "__main__":
    test_performance()