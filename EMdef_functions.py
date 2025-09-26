
# Discrete boundary condition grid
def bc_known(N=10):
    """Define the boundary conditions of electric potential
    
    Boundary Conditions:
        i. V = 0 at y = 0
        ii. V = 0 at y = a
        iii. V = Vo(y) at x = 0
        iv. V = 0 as x -> infinity
        
    Parameters:
        N: The number of points along each axis
        h: The step size of the grid
        x: The x values of the grid
        y: The y values of the grid
        X: The x values of the grid in meshgrid format
        Y: The y values of the grid in meshgrid format
        
    Returns:
        Discrete plot of the boundary conditions in x and y directions
        The voltage is constant in the z direction
    """
    # Import the necessary modules
    import numpy as np, matplotlib.pyplot as plt
    # Define variables
    h = 1/N
    x = np.arange(0, 1+h, h)
    y = np.arange(0, 1+h, h)
    X, Y = np.meshgrid(x, y)
    # Plot the known points with given boundary conditions
    plt.figure(figsize=(8,5))
    # Mark all points as unknown
    plt.plot(x[1], y[1], 'ro', label='unknown points')
    plt.plot(X, Y, 'ro')
    # Mark the known points with given boundary conditions
    # i. V = 0 at y = 0
    plt.plot(x, np.zeros(N+1), 'go')
    # ii. V = 0 at y = a
    plt.plot(x, np.ones(N+1), 'go', label='V(x,y) = 0')
    # iii. V = Vo(y) at x = 0
    plt.plot(np.zeros(N+1), y, 'bo', label='V(x,y) = Vo(y)')
    # iv. V = 0 as x -> infinity
    plt.plot(np.ones(N+1), y, 'go')
    # Set the limits of the plot
    plt.xlim((-0.1, 1.1))
    plt.ylim((-0.1, 1.1))
    # Set the labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    # Set the aspect ratio of the plot
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # Set the title of the plot
    plt.title('Boundary Conditions')
    # Show the plot
    plt.show()
    
# Plot the boundary conditions in 3D
def bc_3D(N=10):
    """Define the boundary conditions of electric potential in 3D.
        
    Boundary Conditions:
        i. V = 0 at y = 0
        ii. V = 0 at y = a
        iii. V = Vo(y) at x = 0
        iv. V = 0 as x -> infinity
        
    Parameters:
        N: The number of points along each axis
        Vo: The voltage at x = 0
        h: The step size of the grid
        x: The x values of the grid
        y: The y values of the grid
        X: The x values of the grid in meshgrid format
        Y: The y values of the grid in meshgrid format
        V: The electric potential at each point in the grid
        
    Returns:
        Plot of the approximate boundary values in 3D.
    """
    # Import the necessary modules
    import numpy as np, matplotlib.pyplot as plt
    # Define variables
    Vo = 1
    h = 1/N
    x = np.arange(0, 1+h, h)
    y = np.arange(0, 1+h, h)
    X, Y = np.meshgrid(x, y)
    V = np.zeros((N+1, N+1))
        
    # Set the boundary conditions along the x-axis
    for i in range(0, N+1):
        V[i, 0] = Vo
        V[i, N] = 0
        
    # Set the boundary conditions along the y-axis
    for j in range(0, N+1):
        V[0, j] = 0
        V[N, j] = 0
        
    # Plot the boundary conditions in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Plot the basic wireframe
    ax.plot_wireframe(X, Y, V, color='b', rstride=10, cstride=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('V(x,y)')
    
    # Plot the boundary conditions
    plt.title('Boundary Conditions', fontsize=24)
    plt.show()

# Define the voltage as a fourier series
def V_fourier(n=100):
    """Creates a 2D electric potential function for a given number of terms in the fourier series.

    Args:
        n (int, optional): The number of terms in the fourier series. Defaults to 100.
        
    Parameters:
        Vo: The voltage at x = 0
        N: The number of points along each axis
        a: The length of the grid
        x: The x values of the grid
        y: The y values of the grid
        V: The electric potential at each point in the grid

    Returns:
        V: A 2D array of the electric potential at each point in the grid
    """
    import numpy as np
    # Define variables
    Vo = 1
    N = 100
    a = 5
    x = np.arange(0, 10, 10/N)
    y = np.arange(0, a, a/N)
    V = np.zeros((N, N))

    # Conditions for the boundaries
    # i. V(y = 0) = 0
    V[0, :] = 0
    # ii. V(y = a) = 0
    V[N-1, :] = 0
    # iii. V(x = 0) = Vo
    V[:, 0] = Vo
    # iv. V = 0 as x -> infinity
    V[:, N-1] = 0

    # Define the fourier series for the electric potential
    # Loop through each point in the grid
    for i in range(1, N-1):
        for j in range(1, N-1):
            # Sum the fourier series for the electric potential at given point (i, j) in the grid
            for k in range(1, n+1, 2):
                V[j,i] += (4*Vo/np.pi) * (1/k) * np.exp(-k*np.pi*x[i]/a) * np.sin(k*np.pi*y[j]/a)

    return V

# Define the electric potential function for the 2D case
def V_function():
    """
    Creates a 2D electric potential function for a given Vo and a

    Parameters:
        N: The number of points along each axis
        Vo: The voltage at x = 0
        a: The length of the grid
        x: The x values of the grid
        y: The y values of the grid
        V: The electric potential at each point in the x-y grid

    Returns:
        V: A 2D array of the electric potential at each point in the x-y grid
    """
    # Import the necessary modules
    import numpy as np
    # Define variables
    N = 100
    Vo = 1
    a = 5
    x = np.arange(0, 10, 10/N)
    y = np.arange(0, a, a/N)
    V = np.zeros((N, N))
    # Conditions for the boundaries
    # Defined explicitly to prevent computing issues
    # i. V(y = 0) = 0
    V[0, :] = 0
    # ii. V(y = a) = 0
    V[N-1, :] = 0
    # iii. V(x = 0) = Vo
    V[:, 0] = Vo
    # iv. V = 0 as x -> infinity
    V[:, N-1] = 0
    
    # Calculate the electric potential at each point in the grid
    for i in range(1, N-1):
        for j in range(1, N-1):
            V[j,i] = (2*Vo/np.pi) * np.arctan((np.sin(np.pi*y[j]/a)/np.sinh(np.pi*x[i]/a)))
    
    return V

# Compare the given approximation with the exact solution of the given PDE
# using the absolute error measure.
def abserr(V1, V2):
    """
    Calculate the absolute error between two matrices V1 and V2.

    Args:
        V1 (numpy.ndarray): The first matrix containing voltage values.
        V2 (numpy.ndarray): The second matrix containing voltage values.
    
    Parameters:
        N: The number of points along each axis
        a: The upper bounds of the potential in the y direction
        x: The x values of the grid
        y: The y values of the grid
        Diff: A matrix containing the absolute error between V1 and V2.

    Returns:
        Diff: A matrix containing the absolute error between V1 and V2.
    """
    import numpy as np
    # Define variables
    N = 100
    a = 5
    x = np.arange(0, 10, 10/N)
    y = np.arange(0, a, a/N)
    Diff = np.zeros((N, N))

    for i in range(0, N):
        for j in range(0, N):
            Diff[i][j] = abs(V1[i][j] - V2[i][j])
            
    return Diff

# Take in a 2D array of the electric potential with sizes x * y
# and return the 3D electric potential
def V_3D_Graph(V, version):
    """Creates a 3D graph of the electric potential
    
    Args:
        V (dep. variable): 2D array of the electric potential
        Version (string): The version of the electric potential plot
        
    Parameters:
        N: The number of points along each axis
        a: The upper bounds of the potential in the y direction
        x: The x values of the grid
        y: The y values of the grid
        X: The x values of the grid in meshgrid format
        Y: The y values of the grid in meshgrid format
        
    Returns:
        3D plot : A 3D plot of the electric potential
    """
    # Import the necessary modules
    import matplotlib.pyplot as plt, numpy as np
    # Define variables
    N = 100
    a = 5
    # Create the grid
    x = np.arange(0, 10, 10/N)
    y = np.arange(0, a, a/N)
    X, Y = np.meshgrid(x, y)
    # Create the 3D plot
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')
    # Plot the 3D electric potential
    ax.plot_wireframe(X, Y, V, color='b')
    # Set the labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('V(x,y)')
    # Set the title of the plot
    ax.set_title(f'Electric Potential in 3D: {version}')
    # Show the plot
    plt.show()

# Create a heat map to visualize the electric potential and error
def V_heatmap(V, Diff, version):
    """Creates a heatmap of the electric potential and error
    
    Args:
        V (dep. variable): 2D array of the electric potential
        Diff (dep. variable): 2D array of the absolute error
        Version (string): The version of the electric potential plot
        
    Parameters:
        N: The number of points along each axis
        a: The upper bounds of the potential in the y direction
        x: The x values of the grid
        y: The y values of the grid
        X: The x values of the grid in meshgrid format
        Y: The y values of the grid in meshgrid format
        
    Returns:
        2D plot : A heatmap of the electric potential and error
    """
    # Import the necessary modules
    import matplotlib.pyplot as plt, numpy as np
    # Define variables
    N = 100
    a = 5
    # Create the grid
    x = np.arange(0, 10, 10/N)
    y = np.arange(0, a, a/N)
    X, Y = np.meshgrid(x, y)
    # Create the heatmap
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    # Plot the electric potential
    im1 = ax[0].imshow(V, cmap='coolwarm', extent=[0, 10, 0, 5])
    ax[0].set_title(f'Electric Potential: {version}')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    # Plot the absolute error
    im2 = ax[1].imshow(Diff, cmap='hot', extent=[0, 10, 0, 5])
    ax[1].set_title(f'Absolute Error: {version}')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('y')
    # Add a colorbar
    fig.colorbar(im1, ax=ax[0], orientation='vertical')
    fig.colorbar(im2, ax=ax[1], orientation='vertical')
    # Show the plot
    plt.show()
