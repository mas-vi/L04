# Bug reports for exercise2.py

Line:8
Problem:The condition "at least one digit" is correctly checked with any(c.isdigit() for c in password), but the logical "and" between length and digit check is correct in form. However, there's no explicit handling of edge cases like empty passwords or non-string inputs. Also, the requirement "at least 8 characters" is correctly implemented, but the function does not validate that the input is a string, which could lead to errors if passed a number or None. This is a bad input validation case.
Example:is_valid_password(1234567) → returns False (correct), but is_valid_password("") → returns False (correct), is_valid_password(12345) → returns False (correct), but is_valid_password(12345678) → returns True (correct). However, is_valid_password(None) would raise an error due to len(None) being undefined.
Fix: return (isinstance(password, str) and len(password) >= 8) and any(c.isdigit() for c in password)

Line:12
Problem:The clamp function uses min and max correctly, but it assumes that low <= high. If low > high, it will return high, which is incorrect. For example, if low=10 and high=5, then clamp(7,10,5) should return 5, but it returns max(10, min(7,5)) = max(10,5) = 10, which is wrong. This is a bad interval boundary condition.
Example:clamp(7, 10, 5) → returns 10, but should return 5.
Fix: return max(low, min(x, high)) if low <= high else max(low, high) if x >= high else x

Line:3
Problem:The condition "grade >= 5" is correct for "5 or more", but it fails to handle negative grades or non-numeric inputs. For example, if grade is -1, it returns False, which is correct, but if grade is "A", it will raise a TypeError. The function does not validate input type, leading to runtime errors.
Example:is_passing("A") → raises TypeError.
Fix: return isinstance(grade, (int, float)) and grade >= 5
