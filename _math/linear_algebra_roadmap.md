# Linear Algebra Roadmap

## Resources

MIT 18.06 by Gilbert Strang [(course)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/) - great videos, lots of homework problems/exams

Linear Algebra by 3blue1brown [(video)](https://www.3blue1brown.com/topics/linear-algebra) - extremely high quality visualizations

"Introduction to Linear Algebra" by Gilbert Strang (textbook) - clear understanding of basics and applications

"Linear Algebra Done Right" by Sheldon Axler (textbook) - Theoretical understanding of linear algebra without heavy reliance on determinants

## Extra Resources
Instead of computing the most exact answer possible as fast as possible (NLA), in Rand-NLA we compute a close enough answer as fast as possible with high probability.

Randomized Numerical Linear Algebra: Foundations & Algorithms [[paper]](https://arxiv.org/abs/2002.01387)

Is the Future of Linear Algebra..Random? [[video]](https://www.youtube.com/watch?v=6htbyY3rH1w&ab_channel=MutualInformation)

## Fundamentals part I

1. **Vector Spaces and Subspaces**
   - Definition and properties of vector spaces
     - "Done Right" section 1
     - Abstract Vector Spaces 3blue1brown [(video)](https://www.youtube.com/watch?v=TgKwz5Ikpc8&ab_channel=3Blue1Brown)
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
   - $A=CR$
     - C (column space matrix)
     - R (reduced row echelon form)
   - $A=LU$
     - Lower triangular and upper triangular matrices
   - $A=QR$
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
    - $S=Q \Lambda Q^T$
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
    - PageRank Algorithm (Google's page algorithm - uses Markov Matrices.)

## Advanced

15. **Jordan Canonical Form**
    - Definition of Jordan matrices
    - Jordan blocks and Jordan basis
    - Computation of Jordan canonical form
    - Applications and significance of Jordan form

16. **Dual spaces and tensors**

17. **Markov Matrices and Perron-Frobenius**

18. **Random Matrices**

19. **Other Matrix Forms and Decompositions**
    - Schur Decomposition
      - Unitary and upper triangular matrices
    - Polar Decomposition
      - Unitary and positive semidefinite matrices
    - Block matrices and partitioned matrices
