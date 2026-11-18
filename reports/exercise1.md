# Bug reports for exercise1.py

Line:3  
Problem: The condition `n % 2 == 1` checks if a number is odd (remainder 1 when divided by 2), so it returns `True` for odd numbers and `False` for even numbers. This is the opposite of what the function `is_even(n)` is supposed to do. It should return `True` when `n` is even, i.e., when `n % 2 == 0`.  
Example: Input `4` → should return `True` (even), but currently returns `False`.  
Fix: `return n % 2 == 0`

---

Line:8  
Problem: The function `rectangle_area(width, height)` incorrectly returns the sum of width and height instead of the product (area). Area of a rectangle is calculated as `width * height`, not `width + height`.  
Example: Input `width=5`, `height=3` → should return `15`, but currently returns `8`.  
Fix: `return width * height`

---

Line:13  
Problem: The function `double(n)` adds 2 to `n`, but it should return twice the number, i.e., `n * 2`. Currently, it returns `n + 2`, which is incorrect.  
Example: Input `4` → should return `8`, but currently returns `6`.  
Fix: `return n * 2`
