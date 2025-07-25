# Code Repository for My Blog

Welcome to the code repository for my [📖 personal blog](https://vladislav-morozov.github.io/blog/)!

This repository contains the code for all the blog posts with code. Each post own folder with a README that provides an overview and any replication/usage instructions.

 

## 📂 Repository Structure

The structure of the repository reflects the categories on the blog. Current folder structure:
```
├── Simulations
│   ├── Tools                      # Tools for simulations
|       ├── ...
├── Statistics
│   ├── Heterogeneity              # Dealing with unseen heterogeneity in data
|       ├── ...
│   ├── Inference                  # Testing and confidence regions
|       ├── ...
```

## Getting Started

To get started with any of the code in this repository, navigate to the relevant post folder and follow the instructions in the README file. Each README contains an overview of the post, the purpose of the code, and step-by-step instructions to replicate the results.

## Recent Posts With Code

### 1. [The Hidden Delta Method in `statsmodels` (A Worked Example)](https://vladislav-morozov.github.io/blog/statistics/inference/2025-07-23-delta-method-statsmodels/)
**Summary**: Using the delta method in Python with `statsmodels` for nonlinear inference: a practical example of confidence intervals and tests. Repository contains Python codes for the empirical example.
<figure>
  <img src="Statistics/Inference/delta-method-statsmodels/img/delta-method-statsmodels.jpg" alt="Essential syntax">
  <figcaption>The essential syntax for using the delta method</figcaption>
</figure>

### 2. [Why Simultaneous (Joint) Tests Instead of Adjusted Multiple Tests?](https://vladislav-morozov.github.io/blog/statistics/inference/2025-04-01-why-joint-test/)
**Summary**: Why simultaneous hypothesis tests are better — but not always — than adjusted multiple tests. Repository contains Python simulation code.
<figure>
  <img src="Statistics/Inference/why-simultaneous-tests/img/power_animated_small.gif" alt="How adding fixed effects may lead to bias">
  <figcaption>Graphical summary of results: simultaneous tests may be more powerful by a large margin, but not always.</figcaption>
</figure>

### 3. [Why Fixed Effects Are Not a Silver Bullet](http://vladislav-morozov.github.io/blog/statistics/heterogeneity/2025-02-01-fixed_effects_danger/)
**Summary**: Why adding (more) fixed effects is not a silver bullet for the problem of unobserved heterogeneity and 3 things you can do about it. Repository contains Python simulation code.
<figure>
  <img src="Statistics/Heterogeneity/fixed-effects-dangers/img/blog_fe_bias_kde_simplified.gif" alt="How adding fixed effects may lead to bias">
  <figcaption>Graphical summary of results: adding fixed effects may lead to more biased estimates</figcaption>
</figure>
  
### 4. [How to Add a Progress Bar for Matlab parfor Loops](https://vladislav-morozov.github.io/blog/simulations/tools/2024-11-11-simple-parfor-progress-bar/)
**Summary**: An easy way to track progress in `parfor` loops in Matlab. Repository contains `createParallelProgressBar.m` function that creates a visually appealing progress bar, along with a usage example 
<figure>
  <img src="https://vladislav-morozov.github.io/assets/img/blog/parfor_bar.gif" alt="A visual parfor progress bar for Matlab">
  <figcaption>What it looks like: a waitbar with explicit progress and an accessible diverging color scheme</figcaption>
</figure>

## Contributions

Contributions to this repository are welcome! If you have suggestions or improvements, please feel free to open an issue or get in touch using any other means.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or inquiries, feel free to contact me via  email at  [vladislav.morozov [at] barcelonagse.eu](mailto:vladislav.morozov@barcelonagse.eu).

---

Thank you for visiting!

