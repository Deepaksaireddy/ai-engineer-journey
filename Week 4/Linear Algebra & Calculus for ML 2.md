# Essence of Linear Algebra — Summary (Part 2: Videos 4–7)
### Series by 3Blue1Brown

---

## 4. Matrix Multiplication as Composition *(Chapter 4)*

### Core Concept
Applying one linear transformation and then another (e.g., first a rotation, then a shear) is itself a new linear transformation, called the **composition** of the two. This single combined transformation can be represented by a single matrix, obtained by **multiplying** the two individual matrices — which is *why* matrix multiplication is defined the way it is.

### Key Ideas
- **Order matters:** Applying rotation then shear is generally *not* the same as shear then rotation. This is why matrix multiplication is **not commutative** (M₁M₂ ≠ M₂M₁ in general) — it mirrors function composition, which also isn't commutative.
- **Reading order:** In the product M₁M₂**v**, you apply M₂ first, then M₁ — read right to left, just like function composition f(g(x)).
- **Associativity holds:** (M₁M₂)M₃ = M₁(M₂M₃), because applying transformations one after another in the same sequence gives the same end result regardless of how you "group" the computation — this makes proving associativity intuitive without needing to grind through the numerical formula.
- **Mechanics of the calculation:** To compute the product matrix, track where the composed transformation sends **î** and **ĵ**: apply the second (rightmost) matrix's basis-vector destinations, then feed those results through the first (leftmost) matrix.

### Example
Let M₁ = rotation by 90°: `[[0,-1],[1,0]]`, and M₂ = a shear: `[[1,1],[0,1]]`.
To find M₁M₂ (shear first, then rotate):
- M₂ sends **î** → (1,0), **ĵ** → (1,1).
- Feed those through M₁ (rotation): (1,0) → (0,1), and (1,1) → (-1,1).
- So the composed matrix has columns (0,1) and (-1,1): `[[0,-1],[1,1]]`.

This matches directly multiplying the matrices using the standard row-by-column formula — but the geometric method (tracking basis vectors) is the intuitive foundation.

### Diagram (conceptual)
```
 Original grid --(apply M2: shear)--> sheared grid --(apply M1: rotate)--> final grid
        î,ĵ                 î',ĵ'                          î'',ĵ''

 Composite matrix M1*M2 takes original grid straight to final grid in ONE step.
```

---

## 5. Three-Dimensional Linear Transformations *(Chapter 5)*

### Core Concept
Everything learned in 2D generalizes directly to 3D (and beyond). A 3D linear transformation is fully described by where it sends the three basis vectors **î**, **ĵ**, **k̂** — each landing spot becomes one column of a 3×3 matrix.

### Key Ideas
- A 3×3 matrix's three columns tell you exactly where **î** = (1,0,0), **ĵ** = (0,1,0), and **k̂** = (0,0,1) land after the transformation.
- Any input vector (x, y, z) transforms via the linear combination: x·(column 1) + y·(column 2) + z·(column 3).
- **Matrix multiplication as composition still works in 3D**, and the same "apply right matrix first, then left matrix" logic and the same non-commutativity apply.
- Computing a 3D matrix product follows the same column-by-column tracking method as in 2D, just with three columns/rows instead of two.

### Example
A transformation that rotates 90° around the z-axis sends:
- **î** = (1,0,0) → (0,1,0)
- **ĵ** = (0,1,0) → (-1,0,0)
- **k̂** = (0,0,1) → (0,0,1) (unchanged, since it's the rotation axis)

Matrix form:
```
|  0  -1   0 |
|  1   0   0 |
|  0   0   1 |
```
Applying this to point (1, 1, 1) gives: 1·(0,1,0) + 1·(-1,0,0) + 1·(0,0,1) = (-1, 1, 1).

### Diagram (conceptual)
```
        k̂ (z-axis, up)
        |
        |
        +-------- ĵ (y-axis)
       /
      /
    î (x-axis)

Each basis vector's new landing position after transformation
becomes one column of the 3x3 matrix.
```

---

## 6. The Determinant *(Chapter 6)*

### Core Concept
The **determinant** of a transformation's matrix measures how much the transformation **scales area** (in 2D) or **volume** (in 3D). It captures a single number summarizing the overall "stretching or squishing factor" of the entire space.

### Key Ideas
- In 2D, the determinant tells you the factor by which the unit square (formed by **î** and **ĵ**) changes in area after the transformation. Because linear transformations keep grid lines evenly spaced and parallel, *every* region scales by this same factor, not just the unit square.
- **Negative determinant:** Indicates the transformation **flips orientation** (like flipping a piece of paper over) — î and ĵ's relative rotational order reverses (e.g., ĵ was counterclockwise from î, but ends up clockwise from î). The absolute value still gives the area-scaling factor.
- **Determinant of zero:** Means the transformation squashes space into a lower dimension (e.g., an entire plane collapsed onto a line, or all of space collapsed onto a single point) — area/volume collapses to zero. This is a critical signal used in later chapters (e.g., for identifying non-invertible matrices).
- **Formula (2D):** For matrix `[[a,b],[c,d]]`, determinant = ad − bc.
- **In 3D:** the determinant measures the scaling of volume, and its sign relates to whether the transformation preserves or inverts the "handedness" (orientation) of space (right-handed vs. left-handed coordinate systems).
- **Determinant of a product:** det(M₁M₂) = det(M₁) · det(M₂) — makes sense intuitively, since scaling factors of successive transformations multiply together.

### Example
For matrix `[[3, 2], [0, 2]]`, determinant = (3)(2) − (2)(0) = 6. This means any shape's area gets multiplied by 6 after this transformation. If instead the matrix were `[[1, 2], [2, 4]]`, determinant = (1)(4) − (2)(2) = 0 — signaling that this transformation squashes the entire 2D plane down onto a single line (zero area).

### Diagram (conceptual)
```
Unit square (area = 1)         After transform (area = |det|)
 ____                              ______
|    |         ---->              /     /
|____|                           /_____/
                           (parallelogram, scaled by det)
```

---

## 7. Inverse Matrices, Column Space and Null Space *(Chapter 7)*

### Core Concept
This video connects linear transformations to **solving systems of linear equations** (A**x** = **v**), and introduces the tools for understanding when and how such systems can be solved.

### Key Ideas
- **System of equations as a transformation problem:** The equation A**x** = **v** asks: "which vector **x**, after being transformed by matrix A, lands on **v**?"
- **Inverse matrix (A⁻¹):** The transformation that "undoes" A — applying A and then A⁻¹ (or vice versa) results in the **identity transformation** (do-nothing transformation, where every vector stays put). Formally, A⁻¹A = A⁻¹A = the identity matrix.
  - If det(A) ≠ 0, an inverse exists, and you can solve for **x** = A⁻¹**v** uniquely.
  - If det(A) = 0, the transformation squashes space into a lower dimension, and **there is no inverse** (you can't "unsquash" a collapsed space back into unique original points) — though solutions may still exist for special vectors **v**, just not a unique one.
- **Rank:** The number of dimensions in the output of a transformation (i.e., the dimensionality of the space the columns/output span). A 2D transformation with rank 2 means the output still fills the full 2D plane (full rank); rank 1 means it collapsed onto a line; rank 0 means it collapsed to a point.
- **Column space:** The set of *all possible outputs* of a transformation — literally, the span of the matrix's columns. Rank is formally defined as the dimension of the column space.
- **Full rank:** When the rank equals the number of columns (the highest possible value), meaning no dimensions are lost.
- **Null space (kernel):** The set of all vectors that land exactly on the **origin (zero vector)** after the transformation. When a transformation squashes space (rank < number of dimensions), there's necessarily a whole set of input vectors that get "collapsed" onto the origin — this set is the null space. It represents the set of solutions to A**x** = **0**.

### Example
Matrix A = `[[1, 2], [2, 4]]` has determinant = 0 (as computed in Chapter 6), so it's **not invertible**. Its rank is 1, since its columns (1,2) and (2,4) both point along the same line (they're parallel — one is a scalar multiple of the other) — so the column space is just that one line, not the full plane. Its null space is the line of all vectors (x, y) satisfying x + 2y = 0 (e.g., (2, -1) and any scalar multiple), since all of those get squashed to the origin (0,0).

By contrast, matrix `[[3, 2], [0, 2]]` (determinant = 6 ≠ 0) is full rank (rank 2), invertible, has a column space equal to the entire 2D plane, and its null space contains only the zero vector itself.

### Diagram (conceptual)
```
Full-rank transformation (invertible):     Rank-deficient transformation (det = 0):
  Output still fills 2D plane                Output collapses onto a single line
                                             (this is the "column space")
        ^                                          
        |  fills all directions                     ^
        |                                            |   all outputs
        +------->                                    | fall on this line
                                                       +------->
                                              Null space = the line of inputs
                                              that get squashed to the origin
```
