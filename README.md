Summary

The project centers on a simple script (Main.py) that orchestrates visualizations: it imports the helper modules, draws the boundary-condition plots, and then hands off to the testing harness to sweep Fourier terms until a desired accuracy is reached.

EMdef_functions.py supplies the core numerical utilities—plotting discrete boundary conditions, constructing Fourier-series and closed-form potentials on a rectangular grid, computing absolute errors, and rendering both 3D surfaces and 2D heat maps for inspection.

EMtest.py bundles an experiment that searches for the smallest odd Fourier term count producing sub–machine-precision average error, logs the intermediate step sizes, and visualizes both the approximation and its error using the helpers from EMdef_functions.
