\# Day 3 — Linear Algebra for ML



\## Summary

Explored the fundamentals of linear algebra and learned how these concepts are applied in Machine Learning. Practiced representing data as vectors and matrices, computing dot products, and performing matrix multiplication through practical exercises using NumPy.



\## Key Concepts

\- Linear algebra as the language of ML: datasets as matrices, parameters as vectors/matrices

\- Vectors: representing one data sample's features

\- Matrices: representing a full dataset (samples × features)

\- The dot product and its role in model prediction

\- Matrix multiplication and the shape-matching rule

\- Shape mismatches as a common source of errors in ML code



\## Tasks

\- Reviewed why every dataset in ML is represented as a matrix, with rows as samples and columns as features.

\- Represented three data samples (age, salary, id\_number) as a (3 × 3) NumPy matrix and confirmed its shape.

\- Computed the dot product of a feature vector with a weight vector by hand, then verified the result using `np.dot`.

\- Used matrix multiplication (@) to produce predictions for all three samples in a single operation.

\- Deliberately created a shape-mismatch error by using a weight vector of the wrong length, then explained in Markdown why the error occurred and how to fix it.

\- Documented the results and explained what each experiment demonstrates using Markdown cells.



\## Key Takeaway

Linear algebra is the mathematical foundation ML models operate on: every prediction a model makes comes down to vectors, matrices, dot products, and matrix multiplication. The dot product is the core operation behind how a linear model turns features into a prediction, while matrix multiplication extends this to an entire dataset at once. Understanding shapes — and why they must match — is essential, since shape mismatches are one of the most common errors encountered when writing ML code.



\## Files

day3.ipynb — linear algebra for ML, including vector/matrix representation, dot product computation, matrix multiplication, and a worked shape-mismatch error.



\## Tools Used

\- NumPy

\- Jupyter Notebook

