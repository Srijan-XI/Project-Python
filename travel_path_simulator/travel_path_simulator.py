# Travel Path Simulator
# This program simulates a travel path based on user input for distance and direction.
# It calculates the total path length, net displacement, and visualizes the path using matplotlib.
# The program also provides a summary of the movements made.

import math
import matplotlib.pyplot as plt

# Function to determine the direction based on changes in x and y coordinates
def get_direction(dx, dy):
    if dx == 0 and dy > 0:
        return 'N'  # North
    elif dx == 0 and dy < 0:
        return 'S'  # South
    elif dy == 0 and dx > 0:
        return 'E'  # East
    elif dy == 0 and dx < 0:
        return 'W'  # West
    elif dx > 0 and dy > 0:
        return 'NE'  # Northeast
    elif dx < 0 and dy > 0:
        return 'NW'  # Northwest
    elif dx < 0 and dy < 0:
        return 'SW'  # Southwest
    elif dx > 0 and dy < 0:
        return 'SE'  # Southeast
    else:
        return ''  # No movement

# Main function to simulate the travel path
def main():
    # Initialize starting coordinates and total distance
    x, y = 0.0, 0.0  # Starting point (0, 0)
    total_distance = 0.0  # Total path length
    path_x = [x]  # List to store x-coordinates of the path
    path_y = [y]  # List to store y-coordinates of the path

    # Get the number of movements from the user
    try:
        n = int(input("Enter number of movements: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Loop through each movement
    for i in range(1, n + 1):
        try:
            # Get the distance and direction for the current movement
            distance = float(input(f"\nEnter distance for movement {i} (in km): "))
            direction = input("Enter direction (N/S/E/W): ").strip().upper()

            # Update coordinates based on the direction
            if direction == 'N':
                y += distance  # Move north
            elif direction == 'S':
                y -= distance  # Move south
            elif direction == 'E':
                x += distance  # Move east
            elif direction == 'W':
                x -= distance  # Move west
            else:
                print("Invalid direction! Please enter N, S, E, or W.")
                continue

            # Update total distance and path coordinates
            total_distance += distance
            path_x.append(x)
            path_y.append(y)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    # Calculate net displacement from the starting point
    displacement = math.sqrt(x**2 + y**2)

    # Display movement summary
    print("\n====== Movement Summary ======")
    print(f"Final Coordinates: ({x:.2f}, {y:.2f})")
    print(f"Total Path Length: {total_distance:.2f} km")
    print(f"Net Displacement: {displacement:.2f} km")

    # Plot the travel path
    plt.figure(figsize=(9, 7))
    plt.plot(path_x, path_y, marker='o', linestyle='-', color='blue')  # Plot the path

    # Annotate the path with distances and directions
    for i in range(1, len(path_x)):
        dx = path_x[i] - path_x[i-1]  # Change in x
        dy = path_y[i] - path_y[i-1]  # Change in y
        mid_x = (path_x[i] + path_x[i-1]) / 2  # Midpoint x-coordinate
        mid_y = (path_y[i] + path_y[i-1]) / 2  # Midpoint y-coordinate
        dist = math.sqrt(dx**2 + dy**2)  # Distance between points
        dirn = get_direction(dx, dy)  # Direction between points
        label = f"{dist:.1f} km {dirn}"  # Label with distance and direction
        plt.text(mid_x, mid_y, label, fontsize=9, ha='center', va='center',
                 bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='gray'))

    # Annotate each point with its index
    for i in range(len(path_x)):
        plt.text(path_x[i], path_y[i], f'{i}', fontsize=9, ha='right', color='black')

    # Add plot details
    plt.title('Travel Path with Distance & Direction')
    plt.xlabel('X Coordinate (km)')
    plt.ylabel('Y Coordinate (km)')
    plt.grid(True)
    plt.axis('equal')  # Ensure equal scaling for x and y axes
    plt.scatter(0, 0, color='green', label='Start (0,0)', zorder=5)  # Mark the starting point
    plt.scatter(path_x[-1], path_y[-1], color='red', label='End Point', zorder=5)  # Mark the endpoint
    plt.legend()
    plt.tight_layout()
    plt.show()  # Display the plot

# Entry point of the program
if __name__ == "__main__":
    main()
