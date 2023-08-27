## Interval Analysis: Dealing with Uncertainties

Interval analysis is a fascinating field within mathematics that revolves around the study of intervals. Instead of focusing on precise real numbers, interval analysis centers on closed intervals \([a, b]\).

The driving force behind this approach originates from the recognition that measurements in the real world are rarely exact. Rather, they are accompanied by inherent error margins. For instance, the mass of an object might be expressed as \(m = 3 \pm 10^{-3} \, \text{kg}\), accounting for the sensitivity of the scale at \(1 \, \text{g}\). This can be naturally represented as \(m \in [3 - 10^{-3}, 3 + 10^{-3}] \, \text{kg}\). Similarly, if we measure the object's acceleration as \(a \in [2 - 10^{-2}, 2 + 10^{-2}] \, \text{m/s}^2\), Newton's second law (\(F = ma\)) yields a force interval
\[
F \in \left[(3 - 10^{-3})(2 - 10^{-2}), (3 + 10^{-3})(2 + 10^{-2})\right].
\]
It's important to note that the lower limit of the measurement error is not the same as the upper limit. Expressing \(F = 6 \pm \text{err}\) would oversimplify and lead to loss of crucial information.

To delve into these concepts, we will create a class dedicated to interval representation and operations on intervals. We'll begin by exploring fundamental arithmetic operations. Given a binary operator \(\odot\) (e.g., +), the operation on intervals \([a, b]\) and \([c, d]\) yields a new interval defined as
\[
[a, b] \odot [c, d] = \{z \in \mathbb{R} \mid z = x \odot y, \text{ where } x \in [a, b] \text{ and } y \in [c, d]\}.
\]
This mathematical expression can be explicitly written as
\[
[a, b] \odot [c, d] = [\min(a \odot c, a \odot d, b \odot c, b \odot d), \max(a \odot c, a \odot d, b \odot c, b \odot d)].
\]
For the four fundamental arithmetic operators, we arrive at the following rules:
- \([a, b] + [c, d] = [a + c, b + d]\)
- \([a, b] - [c, d] = [a - d, b - c]\)
- \([a, b] \cdot [c, d] = [\min(ac, ad, bc, bd), \max(ac, ad, bc, bd)]\)
- \([a, b] / [c, d] = [\min(a/c, a/d, b/c, b/d), \max(a/c, a/d, b/c, b/d)]\), given that \(0 \notin [c, d]\).

## Functions of Intervals: Addressing Peculiarities

Expanding the concept further, it's possible to define functions of intervals. However, a cautious approach is required due to certain intricacies. Let's explore a specific example: the power functions, represented as \(x \mapsto x^n\) where \(n \geq 1\). Depending on the parity of \(n\), distinct behaviors emerge.

### Odd Powers

When \(n\) is odd, the power function is monotonically increasing. As a result, we can express the interval \( [a, b]^n \) as \( \left[a^n, b^n\right] \).

### Even Powers

For even \(n > 0\), the situation is more intricate and depends on the signs of \(a\) and \(b\). We encounter three distinct cases:

1. \(a \geq 0\): In this scenario, \( [a, b]^n \) translates to \( \left[a^n, b^n\right] \).
2. \(b < 0\): When \(b\) is negative, \( [a, b]^n \) transforms into \( \left[b^n, a^n\right] \).
3. Otherwise: If neither of the above conditions apply, the interval becomes \( \left[0, \max \left(a^n, b^n\right)\right] \).

It's crucial to acknowledge that raising intervals to powers is distinct from repeated products. In other words, \( [a, b]^2 \neq [a, b] \ast [a, b] \).

## Interval Class: Mathematical Operations and Functionality

In this program, we'll create a class called `Interval` to facilitate interval arithmetic operations and related functionalities.

### Interval Initialization

We start by constructing the `Interval` class, initialized with two real numbers that define the left and right endpoints of the interval.

### Arithmetic Operations

The program includes methods for performing the four basic arithmetic operations on intervals: addition, subtraction, multiplication, and division.

### Printing Intervals

A `print` method is provided, allowing the interval to be displayed in a readable format. For instance, given the interval `Interval(1, 2)`, the printed output will be `[1, 2]`.

### Contains Method

The program extends the class with a `contains` method that checks whether a given real value lies within the interval.

### Exception Handling

In the division function, proper exceptions are raised to handle scenarios where the divisor interval contains zero or where the result would lead to an infinitely large interval.

### Degenerate Intervals

The class is enhanced to accommodate the identification of a real number \(r\) with a degenerate interval \([r, r]\). As a result, intervals can now be initialized with a single real value, such as `Interval(1)` resulting in the interval \([1, 1]\).

### Flexible Arithmetic

Flexibility in arithmetic operations is achieved by modifying the code. It allows expressions like `Interval(2, 3) + 1`, `1 + Interval(2, 3)`, `1.0 + Interval(2, 3)`, and `Interval(2, 3) + 1.0` to yield the expected results for addition. The same is true for subtraction and multiplication.

### Power Function

The program implements the power function \(x \mapsto x^n\) through the `pow` function. This function allows expressions like:
- \(\text{Interval}(-2, 2) * \star 2\) resulting in \([0, 4]\)
- \(\text{Interval}(-2, 2) * \star 3\) resulting in \([-8, 8]\)

Through these components, the program illustrates how the `Interval` class can facilitate interval arithmetic operations and function calculations.

## Evaluating a Polynomial on Intervals and Visualization

This program focuses on evaluating a polynomial on a list of intervals and creating visualizations based on the results.

### Generating Intervals

To start, a list of 1000 intervals is created. This is achieved by generating a list of lower boundary values using \(\mathrm{xl} = 1\) in steps of \(0.001\), and upper boundaries \(\mathrm{xu} = 1\) in steps of \(0.001\) as well. These intervals are constructed as \([xl, xu]\) where each \(xl\) and \(xu\) define the endpoints of an interval.

### Polynomial Evaluation

The polynomial \(p(I) = 3I^3 - 2I^2 - 5I - 1\) is then evaluated for each interval \(I\) in the list. The results of these evaluations are used to create another list of intervals.

### Visualization

From this new list of intervals, lower boundary values \(\mathrm{yl}\) and upper boundary values \(\mathrm{yu}\) are extracted. A plot is generated to visually represent these lower and upper boundaries against the \(xl\) values of the intervals. This plot provides insights into the behavior of the polynomial across the intervals.