class HatsAndBalls:
    def __init__(self):
        """
        Initialize the HatsAndBalls class.
        We have 10^9 hats numbered from 1 to 10^9, initially all empty.
        """
        self.hats = {}  # Dictionary to store hat number -> count of balls
        
    def AddBall(self, x):
        """
        Adds a ball to hat x.
        
        Args:
            x (int): Hat number (between 1 and 10^9)
        """
        # Check if x is within valid range (1 to 10^9)
        if x < 1 or x > 10**9:
            raise ValueError(f"Hat number must be between 1 and 10^9. Got: {x}")
            
        # Increment the count for this hat
        if x in self.hats:
            self.hats[x] += 1
        else:
            self.hats[x] = 1
    
    def howManyHatsAtleastOne(self):
        """
        Returns how many hats have at least one ball.
        
        Returns:
            int: Number of hats containing at least one ball
        """
        return len(self.hats)
    
    def greatestAmount(self):
        """
        Returns the count of balls for the hat that has the most balls.
        
        Returns:
            int: Maximum number of balls in any single hat
        """
        if not self.hats:
            return 0
        return max(self.hats.values())
    
    def getHatCount(self, x):
        """
        Helper method to get the number of balls in a specific hat.
        
        Args:
            x (int): Hat number
            
        Returns:
            int: Number of balls in hat x
        """
        return self.hats.get(x, 0)
    
    def __str__(self):
        """String representation of the current state"""
        if not self.hats:
            return "All hats are empty"
        
        result = "Hat status:\n"
        for hat, count in sorted(self.hats.items()):
            result += f"  Hat {hat}: {count} ball(s)\n"
        result += f"\nTotal hats with balls: {self.howManyHatsAtleastOne()}"
        result += f"\nMaximum balls in any hat: {self.greatestAmount()}"
        return result

# Comprehensive test function
def test_hats_and_balls():
    """Test the HatsAndBalls class with various scenarios"""
    
    print("=" * 50)
    print("TESTING HATS AND BALLS CLASS")
    print("=" * 50)
    
    # Test 1: Basic functionality
    print("\n1. Testing basic functionality:")
    hb = HatsAndBalls()
    
    # Add balls to different hats
    test_cases = [
        (5, "Add ball to hat 5"),
        (10, "Add ball to hat 10"),
        (5, "Add another ball to hat 5"),
        (1000000, "Add ball to hat 1,000,000"),
        (10, "Add another ball to hat 10"),
        (10, "Add third ball to hat 10"),
        (5, "Add third ball to hat 5")
    ]
    
    for hat, description in test_cases:
        hb.AddBall(hat)
        print(f"  {description}: Hat {hat} now has {hb.getHatCount(hat)} balls")
    
    # Test the main methods
    print(f"\n  Number of hats with at least one ball: {hb.howManyHatsAtleastOne()}")
    print(f"  Greatest amount in any hat: {hb.greatestAmount()}")
    
    # Test 2: Empty state
    print("\n2. Testing empty state:")
    hb_empty = HatsAndBalls()
    print(f"  Hats with balls (should be 0): {hb_empty.howManyHatsAtleastOne()}")
    print(f"  Greatest amount (should be 0): {hb_empty.greatestAmount()}")
    
    # Test 3: Large numbers (within range)
    print("\n3. Testing with large hat numbers:")
    hb_large = HatsAndBalls()
    large_hat = 10**9  # Maximum hat number
    hb_large.AddBall(large_hat)
    print(f"  Added ball to hat {large_hat}")
    print(f"  Hat count: {hb_large.getHatCount(large_hat)}")
    print(f"  Total hats with balls: {hb_large.howManyHatsAtleastOne()}")
    
    # Test 4: Boundary testing
    print("\n4. Testing boundary conditions:")
    hb_boundary = HatsAndBalls()
    
    # Test hat number 1 (minimum)
    hb_boundary.AddBall(1)
    print(f"  Hat 1 count: {hb_boundary.getHatCount(1)}")
    
    # This would raise an error if uncommented:
    # hb_boundary.AddBall(0)  # Invalid - below minimum
    
    # Test 5: Multiple balls in same hat
    print("\n5. Testing multiple balls in same hat:")
    hb_multi = HatsAndBalls()
    for i in range(1, 6):
        hb_multi.AddBall(42)  # Add 5 balls to hat 42
    print(f"  Hat 42 ball count: {hb_multi.getHatCount(42)}")
    print(f"  Greatest amount (should be 5): {hb_multi.greatestAmount()}")
    
    # Test 6: Random operations
    print("\n6. Testing random operations:")
    hb_random = HatsAndBalls()
    import random
    
    # Simulate 20 random ball additions
    for _ in range(20):
        hat_num = random.randint(1, 100)  # Random hat between 1 and 100
        hb_random.AddBall(hat_num)
    
    print(f"  After 20 random additions:")
    print(f"  Hats with balls: {hb_random.howManyHatsAtleastOne()}")
    print(f"  Maximum balls in any hat: {hb_random.greatestAmount()}")
    
    # Show distribution
    print("\n  Distribution of balls:")
    hat_counts = {}
    for i in range(1, 101):
        count = hb_random.getHatCount(i)
        if count > 0:
            hat_counts[i] = count
    
    for hat, count in sorted(hat_counts.items())[:10]:  # Show first 10 hats
        print(f"    Hat {hat}: {count} ball(s)")
    
    if len(hat_counts) > 10:
        print(f"    ... and {len(hat_counts) - 10} more hats")
    
    # Test 7: Performance with many operations
    print("\n7. Testing performance with many operations:")
    hb_perf = HatsAndBalls()
    num_operations = 10000
    
    import time
    start_time = time.time()
    
    for i in range(num_operations):
        hat_num = random.randint(1, 1000000)
        hb_perf.AddBall(hat_num)
    
    elapsed_time = time.time() - start_time
    
    print(f"  Added {num_operations} balls in {elapsed_time:.4f} seconds")
    print(f"  Unique hats used: {hb_perf.howManyHatsAtleastOne()}")
    print(f"  Maximum balls in any hat: {hb_perf.greatestAmount()}")
    
    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED SUCCESSFULLY")
    print("=" * 50)

# Example usage
if __name__ == "__main__":
    # Simple usage example
    print("SIMPLE USAGE EXAMPLE:")
    print("-" * 30)
    
    hb = HatsAndBalls()
    
    # Add some balls
    hb.AddBall(5)
    hb.AddBall(10)
    hb.AddBall(5)
    hb.AddBall(1000000)
    hb.AddBall(10)
    hb.AddBall(10)
    
    print(f"Hats with at least one ball: {hb.howManyHatsAtleastOne()}")
    print(f"Greatest amount in any hat: {hb.greatestAmount()}")
    print(f"Balls in hat 5: {hb.getHatCount(5)}")
    print(f"Balls in hat 10: {hb.getHatCount(10)}")
    print(f"Balls in hat 1000000: {hb.getHatCount(1000000)}")
    
    print("\n" + "=" * 50)
    print("RUNNING COMPREHENSIVE TESTS:")
    print("=" * 50)
    
    # Run comprehensive tests
    test_hats_and_balls()