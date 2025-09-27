# Extend 2D plot to 3D
import numpy as np


DEFAULT_ERROR_TOLERANCE = 1e-6
# Default average error tolerance used when determining n values.

DEFAULT_MAX_ITERATIONS = 250
# Default maximum iterations allowed while searching for an acceptable n value.


def display_3D(*, tolerance: float = DEFAULT_ERROR_TOLERANCE, max_iterations: int = DEFAULT_MAX_ITERATIONS) -> bool:
    """Test the 3D plot of the Fourier series and the error of the fourier series compared to the exact solution.
        Loops through n values to determine the best n value to approximate the solution.
        
    Uses the following functions:
    
        - EMfunction.V_function
        Given the values of Vo and a, calculate the exact solution of the potential function in the x-y plane.
        
        - EMfourier.V_fourier
        Calculate the Fourier series of the potential at each point for given n value.
        
        - EMV_3D.V_3D_Graph
        Display the 3D plot of the potential function using data from eith EMfourier or EMfunction.
        
        - EMcompare.abserr
        Display the absolute error between the fourier series and the exact solution.
        
    Returns:
        Plots of the 3D electric potential using the fourier series for each n and
        the error of the fourier series compared to the exact solution for each n.
        The data is displayed using the voltage as the z-axis and the x and y axes as the position.
        In reality, the electric potential is independent of the z-axis. For any set of fixed points in the x-y plane,
        the electric potential is the same, regardless of the value of z.
        This is done for visualization purposes.
    Args:
        tolerance (float, optional): Average error tolerance used while determining the
            candidate ``n`` values. Defaults to :data:`DEFAULT_ERROR_TOLERANCE` (``1e-6``).
        max_iterations (int, optional): Maximum iterations permitted while searching for an
            ``n`` value that satisfies the tolerance. Defaults to
            :data:`DEFAULT_MAX_ITERATIONS` (``250``).

    Returns:
        bool: ``True`` when an appropriate ``n`` value is found, otherwise ``False`` when the
        search exceeded ``max_iterations``. Callers should check the return value so that scripts
        can terminate gracefully instead of hanging.
    """
    # Import the necessary functions
    import EMdef_functions as df
    # Cache the exact solution once for reuse
    exact = df.V_function()

    # Cache previously computed approximations and error surfaces by n value
    evaluation_cache: dict[int, tuple[np.ndarray, np.ndarray]] = {}
    
    # determine the lowest n with average error less than tolerance
    # given the number of steps n jumps each time
    def det_N(
        N,
        start,
        exact_solution,
        *,
        cache_result=False,
        tolerance=tolerance,
        max_iterations=max_iterations,
    ):
        # Variables for determing best n value in loop
        avg_err = np.inf
        candidate = start
        approx_cache = None
        error_cache = None
        previous_candidate = start
        iterations = 0
        success = False
        # loop to find acceptable n
        while iterations < max_iterations and avg_err > tolerance:
            iterations += 1
            candidate += N

            if candidate in evaluation_cache:
                approx_cache, error_cache = evaluation_cache[candidate]
            else:
                approx_cache = df.V_fourier(candidate)
                error_cache = df.abserr(approx_cache, exact_solution)
                evaluation_cache[candidate] = (approx_cache, error_cache)
            avg_err = np.mean(error_cache)
            if avg_err <= tolerance:
                success = True
                break
            previous_candidate = candidate

        if success:
            print(f'The step size is {N}')
            print(f'n = {candidate}')
        else:
            print(
                f"Stopping search for step {N}: reached maximum iterations ({max_iterations}) "
                f"after {iterations} attempts without meeting the tolerance {tolerance:.3e}. "
                f"Last candidate n = {candidate} with average error {avg_err:.3e}."
            )

        fallback = previous_candidate
        if cache_result:
            return success, fallback, candidate, approx_cache, error_cache
        return success, fallback, candidate

    # Calculate best n with steps of 200, 50, 10, 4, then 1
    success, current_n, _ = det_N(200, 0, exact)
    if not success:
        return False

    success, current_n, _ = det_N(50, current_n, exact)
    if not success:
        return False

    success, current_n, _ = det_N(10, current_n, exact)
    if not success:
        return False

    success, current_n, _ = det_N(4, current_n, exact)
    if not success:
        return False

    success, current_n, best_n, approx, error_surface = det_N(1, current_n, exact, cache_result=True)
    if not success:
        return False

    # print the n value that is most accurate
    print(f'The best n value is n = {best_n}')

    # plot the 3D graph of the potential function using the fourier series and the error of the fourier series compared to the exact solution
    nvalue = 'n = ' + str(best_n)
    df.V_3D_Graph(approx, 'Fourier Series, ' + nvalue)
    df.V_3D_Graph(error_surface, 'Relative Error, ' + nvalue)
    df.V_heatmap(approx, error_surface, 'Fourier Series, ' + nvalue)

    return True
