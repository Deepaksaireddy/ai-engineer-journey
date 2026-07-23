# Essence of Linear Algebra — Summary (Part 1)
### Series by 3Blue1Brown

---

## 1. Vectors, What Even Are They? *(Chapter 1)*

### Core Concept
A vector is presented from three complementary viewpoints:
- **Physics student's view:** an arrow in space, defined by length and direction, which can be freely moved as long as length/direction are preserved.
- **Computer science student's view:** an ordered list of numbers (e.g., a house's size and price used together).
- **Mathematician's view:** any object that can be added to another vector or scaled (multiplied by a number), which generalizes the idea beyond arrows.

The video settles on the visual, "physics-meets-CS" convention used throughout the series: every vector is rooted at the **origin** of a coordinate system, and its tip's coordinates are the list of numbers describing it. For example, the vector (3, -2) points 3 units right and 2 units down from the origin.

### Key Operations
- **Vector addition:** Place the tail of the second vector at the tip of the first; the sum is the vector from the origin to the final tip. Numerically, you add corresponding components: (1, 2) + (3, -1) = (4, 1).
- **Scalar multiplication:** Stretching, squishing, or reversing a vector by a number ("scalar"). Multiplying (1, 2) by 2 gives (2, 4) — the arrow stretches to twice its length in the same direction. A negative scalar flips the direction.

### Example
If vector **v** = (1, 2) represents "walk 1 east, 2 north," and vector **w** = (3, -1) represents "walk 3 east, 1 south," then **v + w** = (4, 1): the combined walk ends up 4 east, 1 north of the start — visualized as placing the arrows tip-to-tail.

### Diagram (conceptual)
```
        ^
        |  w tip
        |   \
        |    \ (v+w) resultant
        |     \
   v --> +------> 
        |
 origin (0,0) ----------------> x-axis
```

---

## 2. Linear Combinations, Span, and Basis Vectors *(Chapter 2)*

### Core Concept
This video reframes vector coordinates using **basis vectors**: in standard 2D coordinates, **î** (i-hat) = (1, 0) and **ĵ** (j-hat) = (0, 1). Any vector, such as (3, -2), can be seen as the sum of scaled basis vectors: 3**î** + (-2)**ĵ**. This sum — scaling vectors and adding them — is called a **linear combination**.

### Key Ideas
- **Linear combination:** For scalars *a* and *b*, the expression *a***v** + *b***w** is a linear combination of **v** and **w**.
- **Span:** The set of *all possible* linear combinations of a set of vectors is called their **span**.
  - If **v** and **w** point in different directions, their span is the entire 2D plane.
  - If **v** and **w** are parallel (one is a scalar multiple of the other), their span collapses to a single line.
  - In 3D, the span of two non-parallel vectors is a flat plane through the origin; adding a third vector not in that plane extends the span to fill all of 3D space.
- **Linear dependence:** A vector is **linearly dependent** on others if it can be written as a combination of them (i.e., it adds no new direction to the span, such as a third vector lying in the plane already spanned by two others).
- **Linear independence:** Vectors are **linearly independent** if each one adds a new dimension to the span (none can be built from the others).
- **Basis (technical definition):** A basis of a vector space is a set of linearly independent vectors that span the full space. The standard basis in 2D is {**î**, **ĵ**}, but any two non-parallel vectors could serve as a basis.

### Example
Vectors **v** = (2, 1) and **w** = (-1, 1) are not parallel, so their span is all of 2D space — meaning *any* 2D vector, like (5, 5), can be written as some combination *a***v** + *b***w**. But if a third vector **u** = (4, 2) were introduced (which is just 2**v**), it would be linearly dependent, since it lies along the line already spanned by **v** alone.

### Diagram (conceptual)
```
Span of two non-parallel vectors (2D plane):

      ^ j-hat direction
      |
      |     * w
      |   /
      | /
      +------------> i-hat direction
        \
          * v

All combinations a·v + b·w sweep out the entire plane.
```

---

## 3. Linear Transformations and Matrices *(Chapter 3)*

### Core Concept
A **linear transformation** is a special kind of function that takes in a vector and outputs a vector, while satisfying two visual/geometric properties:
1. **Lines remain lines** (no curving).
2. **The origin stays fixed** in place.

More technically, grid lines must remain parallel and evenly spaced after the transformation.

### The Big Insight
Because any vector can be written as a linear combination of basis vectors (e.g., **v** = x**î** + y**ĵ**), and because linear transformations preserve the *operations* of scaling and adding, a transformation is **entirely determined by where it sends î and ĵ**. You don't need to track every vector in space — just the two (or *n*, in higher dimensions) basis vectors.

- If **î** lands at (a, c) and **ĵ** lands at (b, d), then any vector (x, y) transforms to: x(a, c) + y(b, d) = (ax + by, cx + dy).
- This is exactly **matrix-vector multiplication**. The matrix
  ```
  | a  b |
  | c  d |
  ```
  is simply the recorded landing spots of **î** (first column) and **ĵ** (second column).
- **Matrix-vector multiplication**, therefore, is nothing more than a compact notation for "compute the linear combination of the matrix's columns, using the vector's entries as the scalar weights."

### Example
Suppose a transformation sends **î** = (1,0) to (2,0) and **ĵ** = (0,1) to (0,3) — a simple stretch. Its matrix is:
```
| 2  0 |
| 0  3 |
```
Applying it to vector (1, 1): x·(2,0) + y·(0,3) = (2, 3). So point (1,1) moves to (2,3) — stretched twice as far in x and three times as far in y.

A 90° counter-clockwise rotation sends **î** → (0,1) and **ĵ** → (-1,0), giving the matrix:
```
| 0  -1 |
| 1   0 |
```

### Diagram (conceptual)
```
BEFORE transform:            AFTER transform (stretch x2, x3):
  ĵ                             ĵ'
  ^                              ^
  |                              |
  |                              |
  +----> î                       +--------> î'
 (grid squares, uniform)     (grid rectangles, stretched)
```
