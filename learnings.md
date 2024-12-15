# Day 3
Iterating in pairs:
```python
it = iter(my_list)
for a, b in zip(it, it):
    print(f"{a}-{b}")

# my_list = [1,2,3,4,5,6]
# prints:
# 1-2
# 3-4
# 5-6
```

# Day 6 - part 2
Checking one location is quite slow, but managable. This gets immediately compounded when both having to check every position, but also getting caught in potentially infinite loops. Breaking out of the inifinite loops was solved by counting the number of times that the guard passed the location. The search space can be narrowed by recognising that many of the locations will never be reached by an initial path. The stoppers only needed to be tested ALONG THE ORIGINAL PATH

# Day 10 - part 1
All of my issues with this were due to not paying close enough attention to the directionality of my "check neighbours" functions. At first I was checking all 8 directions (including diagonals) and then when editing, changed it to only the diagonals. Algorithmic solution seemed nice and easy, given history of tree-walking.

# Day 10 - part 2
All test cases pass, but not the true case. The issue was surprisingly difficult to track down as only the true input data set was failing. The difference turned out to be only 4 paths out of nearly 2000. The issue was that at some point during part one I had added a check for the [0,0] position to always return false. I cannot remember why I did this, but it was this self-sabotage that was causing the issues. The algorithm was correct.

# Day 11 - part 2
Initial implementation was much too slow. My second was just a minor speed improvement on the first, and still ultimately infeasible. Third attempt is significantly better, but I need a way to avoid redoing the same lookups for different counts.
My ultimately correct solution was lightning fast. I realised that in the earlier attempts I was attempting to preserve the order of the stones, even though the final answer did not actually require it.