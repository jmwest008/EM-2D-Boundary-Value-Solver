
if __name__ == '__main__':
    # Import the necessary modules
    import EMdef_functions as bnd
    import EMtest as test
    
    # Define the known values from boundary conditions
    bnd.bc_known()
    # Plot the known values for the boundaries
    bnd.bc_3D()
    
    # Plot the 3D graph of the potential function for the Fourier series
    # and the absolute error of the fourier series compared to the exact solution
    # Iterate through n starting with steps of 200, 50, 5, then 1 to get the lowest n value that is still accurate
    # with average error of the potential less than float-epsilon / 2 (approximately 1.11E-16)
    test.display_3D()
    