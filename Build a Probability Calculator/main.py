import copy
import random

class Hat:
    def __init__(self, **balls):
        # Initialize contents list based on keyword args
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If drawing more balls than exist, return all and empty contents
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        
        # Randomly sample without replacement
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    
    for _ in range(num_experiments):
        # Deep copy hat to not modify original
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        
        # Check if drawn contains at least the expected balls
        success = True
        for color, required_count in expected_balls.items():
            if drawn.count(color) < required_count:
                success = False
                break
        if success:
            successes += 1
    
    return successes / num_experiments

# Demonstration and tests

# Test 1: Creation of hat object should add correct contents.
hat1 = Hat(yellow=3, blue=2, green=6)
print("Test 1 contents:", sorted(hat1.contents))
# Expected: ['blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'yellow', 'yellow', 'yellow']

# Test 2: draw method reduces number of items in contents.
hat2 = Hat(red=2, blue=1)
initial_count = len(hat2.contents)
drawn2 = hat2.draw(2)
print("Test 2 drawn:", drawn2)
print("Test 2 remaining count:", len(hat2.contents), "Expected:", initial_count - 2)

# Test 3: draw method when drawing more balls than available
hat3 = Hat(red=1)
drawn3 = hat3.draw(5)
print("Test 3 drawn all:", drawn3)
print("Test 3 remaining contents:", hat3.contents, "Expected: []")

# Test 4: experiment returns a probability between 0 and 1 and varies
hat4 = Hat(black=6, red=4, green=3)
prob1 = experiment(hat=hat4, expected_balls={'red':2, 'green':1}, num_balls_drawn=5, num_experiments=2000)
prob2 = experiment(hat=hat4, expected_balls={'red':2, 'green':1}, num_balls_drawn=5, num_experiments=2000)
print("Test 4 probabilities:", prob1, prob2)