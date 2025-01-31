# Simple Progress Bar for Matlab `parfor` Loops

This folder contains code to track progress in `parfor` loops in Matlab using a visual progress bar.

## Overview, Blog Post and What It Looks Like

When running parallel computations with `parfor`, tracking progress is challenging because iterations are assigned dynamically to workers. The provided function, `createParallelProgressBar.m`, enables progress tracking by using a `DataQueue` to collect updates from parallel workers and updating a `waitbar` accordingly.

For a detailed explanation of how this progress bar works, check out the original blog post:
[How to Add a Progress Bar for Matlab parfor Loops](https://vladislav-morozov.github.io/blog/simulations/tools/2024-11-11-simple-parfor-progress-bar/)

<figure>
  <img src="https://vladislav-morozov.github.io/assets/img/blog/parfor_bar.gif" alt="A visual parfor progress bar for Matlab">
  <figcaption>What it looks like: a waitbar with explicit progress and an accessible diverging color scheme</figcaption>
</figure>
 

## Files
- **`createParallelProgressBar.m`** – Implements the parallel progress bar.
- **`exampleParforWithProgress.m`** – Example script demonstrating how to use it.

## Usage
1. Place `createParallelProgressBar.m` in a directory included in your Matlab `path`.
2. Use the function in your `parfor` loop as follows:

```matlab
numSamples = 100;

% Initialize the progress bar
queue = createParallelProgressBar(numSamples);  %  <---

parfor iterID = 1:numSamples
    % Simulate computation, replace with your own
    pause(rand(1));   
    % Update progress bar after simulation is done
    send(queue, iterID);  % <---
end
```

## How It Works
- `createParallelProgressBar.m` initializes a `DataQueue` and a `waitbar`.
- Each worker sends messages to the `DataQueue` upon completing an iteration.
- The main process listens for updates and refreshes the progress bar.
- The progress bar automatically closes when all iterations are complete.


## Compatibility
Tested on Matlab 2024b+ on Windows. Should work on most modern versions of Matlab with `parfor` and `DataQueue` support. 
 
## License

The standard MIT license applies. 