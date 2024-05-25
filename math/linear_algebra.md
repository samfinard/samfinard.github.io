# Linear Algebra Roadmap

## Fundamentals part I

1. **Vector Spaces and Subspaces**
   - Definition and properties of vector spaces
   - Subspaces, span, and linear combinations
   - Basis and dimension
   - Direct sums and dimension theorem

2. **Linear Transformations and Matrices**
   - Definition of linear transformations
   - Matrix representation of linear transformations
   - Kernel and image of a linear transformation
   - Composition of linear transformations and matrix multiplication

3. **Matrix Properties and Column Independence**
   - Linear independence of columns
   - Rank of a matrix
   - Column space and null space
   - Basis and dimension of subspaces

4. **Triangular Matrices**
   - Upper triangular matrices
   - Lower triangular matrices
   - Properties and applications

5. **Determinants**
   - Definition and properties of determinants
   - Computing determinants (Laplace expansion, row reduction)
   - Applications of determinants (e.g., volume, Cramer's rule)

## Fundamentals part II

6. **Linear Equations and Subspaces**
   - Solving linear equations $Ax = b$
   - Inverse of a matrix
   - Four fundamental subspaces
     - Column space
     - Null space
     - Row space
     - Left null space

7. **Matrix Decompositions**
   - Matrix factorization: $A = CR$
     - C (column space matrix)
     - R (reduced row echelon form)
   - LU Decomposition
     - Lower triangular and upper triangular matrices
   - QR Decomposition
     - Orthogonal and upper triangular matrices

8. **Orthogonality and Least Squares**
    - Orthogonal vectors and subspaces
    - Projection matrices
    - Least squares problems and solutions

9. **Invertibility and Pseudo-inverse**
    - Conditions for invertibility
    - Moore-Penrose pseudo-inverse
    - Computation and applications of pseudo-inverses

10. **Eigenvalues and Eigenvectors**
   - Definition of eigenvalues and eigenvectors
   - Characteristic polynomial
   - Diagonalization of matrices
   - Applications of eigenvalues and eigenvectors

## Practical Applications

11. **Singular Value Decomposition (SVD)**
    - Definition and computation of singular values
    - Decomposition: $A = U \Sigma V^T$
    - Applications of SVD in data science and machine learning

12. **Principal Component Analysis (PCA)**
    - Introduction to PCA
    - Covariance matrix
    - Eigenvalues and eigenvectors of the covariance matrix
    - Dimensionality reduction
    - Applications of PCA in data science

13. **Numerical Computations in Linear Algebra**
    - Methods for solving linear systems (LU decomposition, QR decomposition)
    - Numerical stability and conditioning
    - Iterative methods (e.g., Jacobi, Gauss-Seidel)

14. **Applications in CS**
    - Computer  Graphics (transformations, projection, viewing)
    - Data Mining (Clustering algorithms like k-means, spectral clustering)
    - PageRank Algorithm (requires 15.)

## Advanced

15. **Jordan Canonical Form**
    - Definition of Jordan matrices
    - Jordan blocks and Jordan basis
    - Computation of Jordan canonical form
    - Applications and significance of Jordan form

16. **Other Matrix Forms and Decompositions**
    - Schur Decomposition
      - Unitary and upper triangular matrices
    - Polar Decomposition
      - Unitary and positive semidefinite matrices
    - Block matrices and partitioned matrices

15. **Markov Matrices and Perron-Frobenius** (requires stats)