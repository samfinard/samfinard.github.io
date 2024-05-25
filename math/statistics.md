# Statistics Roadmap

## Resources

"Statistical Inference" by George Casella and Roger Berger (textbook) - Probability theory starting from the fundamentals. Theorem based.

MIT 6.042 "Math for CS" by Prof. Leighton - 7 Great videos that very quickly cover conditional probability to random walks.

## Fundamentals Part I

1. **Basic Probability Concepts**
   - Sample space and events
   - Probability axioms
   - Additive and multiplicative rules

2. **Counting Techniques**
   - Permutations: Number of ways to arrange $n$ objects: $n!$
   - Combinations: Number of ways to choose $k$ objects from $n$: $\binom{n}{k}$
   - Binomial coefficient: Calculation and properties

3. **Random Variables**
   - Discrete random variables: Definition and PMF
   - Continuous random variables: Definition and PDF
   - Cumulative distribution function (CDF)

4. **Expected Value and Variance**
   - Expected value (mean): $E[X] = \sum x_i P(X = x_i)$ for discrete, $E[X] = \int x f_X(x) \, dx$ for continuous
   - Variance and standard deviation: $\text{Var}(X) = E[(X - E[X])^2]$
   - Linearity of expectation: $E[aX + b] = aE[X] + b$

5. **Conditional Probability and Independence**
   - Conditional probability: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
   - Independence: $P(A \cap B) = P(A) \cdot P(B)$

## Fundamentals Part II

6. **Common Distributions**
   - Binomial distribution: PMF, mean, variance, applications
   - Poisson distribution: PMF, mean, variance, applications
   - Normal (Gaussian) distribution: PDF, properties, Central Limit Theorem
   - Exponential distribution: PDF, mean, variance, memoryless property

7. **Joint Distributions**
   - Joint, marginal, and conditional distributions
   - Covariance: $\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])$
   - Correlation: $\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$

8. **Transformations of Random Variables**
   - Linear transformations: Effects on mean and variance
   - Functions of random variables: Methods for finding the distribution of a function of random variables

9. **Limit Theorems**
   - Law of Large Numbers: Convergence of sample averages to the expected value
   - Central Limit Theorem: Distribution of the sum of a large number of independent random variables

## Applications in Finance

10. **Random Walks**
    - Definition and properties: Simple random walk on a number line
    - Expected position and variance after $n$ steps
    - Applications: Modeling stock prices and financial markets

11. **Stock Price Modeling**
    - Geometric Brownian motion: Definition and properties, modeling stock prices
    - Black-Scholes model: Option pricing using the Black-Scholes formula

12. **Risk Management**
    - Value at Risk (VaR): Definition and calculation
    - Portfolio optimization: Mean-variance optimization, efficient frontier

## Monte Carlo Methods

13. **Introduction to Monte Carlo Methods**

- Definition and basic concepts
- Applications in numerical integration and simulation

14. **Random Number Generation**

- Uniform random number generation
- Transformations to other distributions (e.g., Box-Muller transform for normal distribution)

15. **Monte Carlo Integration**

- Estimating the value of definite integrals using random sampling
- Importance sampling to reduce variance

16. **Variance Reduction Techniques**

- Antithetic variates
- Control variates
- Stratified sampling

17. **Markov Chain Monte Carlo (MCMC)**

- Introduction to MCMC
- Metropolis-Hastings algorithm
- Gibbs sampling

18. **Applications of Monte Carlo Methods**

- Option pricing in finance
- Risk assessment and management
- Bayesian inference in statistics

## Markov Chains

19. **Introduction to Markov Chains**

- Definition and basic properties
- State space and transition probabilities

20. **Classification of States**

- Transient, recurrent, and absorbing states
  - Periodicity and ergodicity

21. **Long-term Behavior**

- Stationary distributions
- Convergence to equilibrium

22. **Markov Chain Models**

- Discrete-time Markov chains (DTMC)
- Continuous-time Markov chains (CTMC)

23. **Applications of Markov Chains**

- PageRank algorithm in web search
- Queueing theory and network modeling
- Hidden Markov Models (HMMs) in speech and language processing

24. **Markov Chain Simulation**

- Simulating Markov chains
- Monte Carlo simulations with Markov chains
- Coupling and mixing times
- Markov Chain Monte Carlo (MCMC) methods
