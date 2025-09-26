
# Extend 2D plot to 3D
def display_3D():
    """Test the 3D plot of the Fourier series and the error of the fourier series compared to the exact solution.
        Loops through n values to determine the best n value to approximate the solution.
        
    Contains the following functions:
    
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
    """
    # Import the necessary modules
    import numpy as np
    # Import the necessary functions
    import EMdef_functions as df
    # Defines minimal value error float values
    float_epsilon = np.finfo(float).eps
    
    
    # determine the lowest n with average error less than float_epsilon
    # given the number of steps n jumps each time
    def det_N(N, i):
        # Variables for determing best n value in loop
        avg_err = 1
        # loop to find acceptable n
        while avg_err > float_epsilon/2:
            i += N
            avg_err = np.mean(df.abserr(df.V_fourier(i), df.V_function()))
        print(f'The step size is {N}')
        print(f'n = {i}')
        i -= N
        return i
    
    # Calculate best n with steps of 50, 10, then 1
    best_n = det_N(200, 0)
    best_n = det_N(50, best_n)
    best_n = det_N(10, best_n)
    best_n = det_N(4, best_n)
    best_n = det_N(1, best_n)
    best_n += 1
    err = df.abserr(df.V_fourier(best_n), df.V_function())
    
    # print the n value that is most accurate
    print(f'The best n value is n = {best_n}')
        
    # plot the 3D graph of the potential function using the fourier series and the error of the fourier series compared to the exact solution
    nvalue = 'n = ' + str(best_n)
    df.V_3D_Graph(df.V_fourier(best_n), 'Fourier Series, ' + nvalue)
    df.V_3D_Graph(err, 'Relative Error, ' + nvalue)   
    df.V_heatmap(df.V_fourier(best_n), err, 'Fourier Series, ' + nvalue)
    
