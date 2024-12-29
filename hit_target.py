import math

def height(t, v0, theta, g=9.81):
    """Calculate the height of the ball at time t """
    
    return (-1/2) * g * t**2 + v0 * t * math.sin(theta)


def score(b, theta, h0, h1):
    points = 0

    # velocity range 
    initial_v_list = [15, 16, 19, 22] 
    
    for v in initial_v_list :
        T = b / (v * math.cos(theta))  # Time to reach the horizontal distance b
        H = height(T, v, theta, 9.81)  # Height at time T

        
        if (1/2) * (h0 + h1) <= H <= h1:
            points += 2  
        elif h0 <= H < (1/2) * (h0 + h1):
            points += 1  
        else:
            points += 0  

    return points 


try:
    time = float(input("Enter the time (in seconds): "))
    initial_v = float(input("Enter the initial velocity (in m/s): "))
    angle_indegree = float(input("Enter the angle of projection (in degrees): "))
    angle_radians = math.radians(angle_indegree)  # Convert to radians
    
    h = height(time, initial_v, angle_radians)
    if h >= 0:  # Check if the height is not negative
        print(f"The height of the ball at time {time:.2f} seconds is: {h:.2f} meters")
    else:
        print(f"The ball has already hit the ground at time {time:.2f} seconds.")
except ValueError:
    print("Invalid input. Please enter float or integer values ")



try:
    b = 3.5  
    theta = math.pi / 4  
    h0 = 3  # Minimum target height
    h1 = 3.5  # Maximum target height

    sc = score(b, theta, h0, h1)
    print(f"The person got a score of {sc} points.")
except Exception as e:
    print(f"An error occurred while calculating the score: {e}")
