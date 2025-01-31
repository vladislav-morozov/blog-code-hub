% ===========================================================
% File: exampleParforWithProgress.m
% Description: This script shows how to use createParallelProgressBar
% ===========================================================
% Blog Post: How to Add a Progress Bar for Matlab parfor Loops
% Post link: https://vladislav-morozov.github.io/blog/simulations/tools/...
%            2024-11-11-simple-parfor-progress-bar/
% Author: Vladislav Morozov
% Date: 2024-11-11
% License: MIT
% ===========================================================

numSamples = 100;

% Initialize the progress bar
queue = createParallelProgressBar(numSamples);  %  <---

parfor iterID = 1:numSamples
    % Simulate computation, replace with your own
    pause(rand(1));   
    % Update progress bar after simulation is done
    send(queue, iterID);  % <---
end