"""
Travel Path Simulator
=====================
An advanced travel path simulator that visualizes and analyzes movement patterns.

Features:
- Support for cardinal (N/S/E/W) and diagonal directions (NE/NW/SE/SW)
- Visual path plotting with distance and direction annotations
- Statistics including total distance, displacement, and efficiency
- Movement history with detailed step-by-step summary
- Error handling and input validation
- Option to save the plot as an image

Author: Enhanced Version
Date: November 2025
"""

import math
import matplotlib.pyplot as plt
from typing import List, Tuple

# Direction mappings for easier input
DIRECTION_MAP = {
    'N': (0, 1), 'NORTH': (0, 1),
    'S': (0, -1), 'SOUTH': (0, -1),
    'E': (1, 0), 'EAST': (1, 0),
    'W': (-1, 0), 'WEST': (-1, 0),
    'NE': (1, 1), 'NORTHEAST': (1, 1),
    'NW': (-1, 1), 'NORTHWEST': (-1, 1),
    'SE': (1, -1), 'SOUTHEAST': (1, -1),
    'SW': (-1, -1), 'SOUTHWEST': (-1, -1)
}

def get_direction(dx: float, dy: float) -> str:
    """
    Determine the direction based on changes in x and y coordinates.
    
    Args:
        dx: Change in x coordinate
        dy: Change in y coordinate
    
    Returns:
        String representing the direction (N, S, E, W, NE, NW, SE, SW)
    """
    if abs(dx) < 0.001 and abs(dy) < 0.001:
        return ''
    
    # Normalize for diagonal detection
    angle = math.atan2(dy, dx)
    angle_deg = math.degrees(angle)
    
    # Map angle to direction
    if -22.5 <= angle_deg < 22.5:
        return 'E'
    elif 22.5 <= angle_deg < 67.5:
        return 'NE'
    elif 67.5 <= angle_deg < 112.5:
        return 'N'
    elif 112.5 <= angle_deg < 157.5:
        return 'NW'
    elif 157.5 <= angle_deg <= 180 or -180 <= angle_deg < -157.5:
        return 'W'
    elif -157.5 <= angle_deg < -112.5:
        return 'SW'
    elif -112.5 <= angle_deg < -67.5:
        return 'S'
    elif -67.5 <= angle_deg < -22.5:
        return 'SE'
    return ''

def get_valid_distance() -> float:
    """Get a valid distance input from the user."""
    while True:
        try:
            distance = float(input("Enter distance (in km): "))
            if distance <= 0:
                print("⚠️  Distance must be positive!")
                continue
            return distance
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def get_valid_direction() -> Tuple[float, float]:
    """Get a valid direction input from the user."""
    while True:
        direction = input("Enter direction (N/S/E/W/NE/NW/SE/SW): ").strip().upper()
        if direction in DIRECTION_MAP:
            dx, dy = DIRECTION_MAP[direction]
            return dx, dy
        print(f"❌ Invalid direction! Valid options: {', '.join(sorted(set(DIRECTION_MAP.keys())))}")

def calculate_statistics(path_x: List[float], path_y: List[float], 
                         total_distance: float) -> dict:
    """
    Calculate various statistics about the journey.
    
    Returns:
        Dictionary containing statistics
    """
    displacement = math.sqrt(path_x[-1]**2 + path_y[-1]**2)
    efficiency = (displacement / total_distance * 100) if total_distance > 0 else 0
    
    # Calculate bearing to final position
    if displacement > 0:
        bearing = math.degrees(math.atan2(path_y[-1], path_x[-1]))
        if bearing < 0:
            bearing += 360
    else:
        bearing = 0
    
    return {
        'displacement': displacement,
        'efficiency': efficiency,
        'bearing': bearing,
        'final_x': path_x[-1],
        'final_y': path_y[-1]
    }

def print_movement_summary(path_x: List[float], path_y: List[float], 
                          total_distance: float):
    """Print detailed movement summary."""
    stats = calculate_statistics(path_x, path_y, total_distance)
    
    print("\n" + "="*50)
    print("📊 MOVEMENT SUMMARY")
    print("="*50)
    
    # Step-by-step movements
    print("\n🚶 Step-by-Step Movements:")
    print("-" * 50)
    for i in range(1, len(path_x)):
        dx = path_x[i] - path_x[i-1]
        dy = path_y[i] - path_y[i-1]
        dist = math.sqrt(dx**2 + dy**2)
        dirn = get_direction(dx, dy)
        print(f"  Step {i}: {dist:.2f} km {dirn} → Position ({path_x[i]:.2f}, {path_y[i]:.2f})")
    
    # Statistics
    print("\n📈 Journey Statistics:")
    print("-" * 50)
    print(f"  🏁 Starting Point    : (0.00, 0.00)")
    print(f"  🎯 Final Position    : ({stats['final_x']:.2f}, {stats['final_y']:.2f})")
    print(f"  📏 Total Path Length : {total_distance:.2f} km")
    print(f"  ↗️  Net Displacement  : {stats['displacement']:.2f} km")
    print(f"  🧭 Bearing to End    : {stats['bearing']:.1f}°")
    print(f"  ⚡ Path Efficiency   : {stats['efficiency']:.1f}%")
    print(f"  📍 Total Moves       : {len(path_x) - 1}")
    print("="*50)

def main():
    """Main function to simulate the travel path."""
    print("\n🗺️  TRAVEL PATH SIMULATOR")
    print("="*50)
    
    # Initialize starting coordinates and total distance
    x, y = 0.0, 0.0
    total_distance = 0.0
    path_x = [x]
    path_y = [y]
    movements = []

    # Get the number of movements from the user
    while True:
        try:
            n = int(input("\nEnter number of movements: "))
            if n <= 0:
                print("⚠️  Number of movements must be positive!")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a positive integer.")

    # Loop through each movement
    print("\n📝 Enter movement details:")
    print("-" * 50)
    
    for i in range(1, n + 1):
        print(f"\nMovement {i}:")
        
        distance = get_valid_distance()
        dx, dy = get_valid_direction()
        
        # Calculate actual movement considering diagonal distances
        if dx != 0 and dy != 0:
            # Diagonal movement - normalize to unit vector and scale
            magnitude = math.sqrt(dx**2 + dy**2)
            dx = dx / magnitude
            dy = dy / magnitude
        
        # Update coordinates
        x += dx * distance
        y += dy * distance
        total_distance += distance
        
        # Store movement
        path_x.append(x)
        path_y.append(y)
        movements.append((distance, get_direction(dx, dy)))
        
        print(f"✓ Current position: ({x:.2f}, {y:.2f})")

    # Display movement summary
    print_movement_summary(path_x, path_y, total_distance)

    # Ask if user wants to visualize
    visualize = input("\n🎨 Would you like to visualize the path? (y/n): ").strip().lower()
    if visualize != 'y':
        print("\n👋 Thank you for using Travel Path Simulator!")
        return

    # Plot the travel path
    fig, ax = plt.subplots(figsize=(12, 9))
    
    # Plot the path with gradient color
    for i in range(len(path_x) - 1):
        color = plt.cm.viridis(i / (len(path_x) - 1))
        ax.plot(path_x[i:i+2], path_y[i:i+2], marker='o', linestyle='-', 
                color=color, linewidth=2, markersize=8)

    # Annotate the path with distances and directions
    for i in range(1, len(path_x)):
        dx = path_x[i] - path_x[i-1]
        dy = path_y[i] - path_y[i-1]
        mid_x = (path_x[i] + path_x[i-1]) / 2
        mid_y = (path_y[i] + path_y[i-1]) / 2
        dist = math.sqrt(dx**2 + dy**2)
        dirn = get_direction(dx, dy)
        label = f"{dist:.1f} km\n{dirn}"
        ax.text(mid_x, mid_y, label, fontsize=8, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.4', fc='lightyellow', ec='gray', alpha=0.9))

    # Annotate each point with its index
    for i in range(len(path_x)):
        label = 'START' if i == 0 else f'P{i}'
        offset = 0.3 if i == 0 else 0.2
        ax.text(path_x[i], path_y[i] + offset, label, fontsize=9, 
                ha='center', va='bottom', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='black', alpha=0.8))

    # Draw displacement line
    stats = calculate_statistics(path_x, path_y, total_distance)
    ax.plot([0, path_x[-1]], [0, path_y[-1]], 'r--', linewidth=2, 
            alpha=0.6, label=f'Displacement: {stats["displacement"]:.2f} km')

    # Add plot details
    ax.set_title('🗺️  Travel Path Visualization\nwith Distance & Direction', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('X Coordinate (km)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y Coordinate (km)', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.axis('equal')
    
    # Mark special points
    ax.scatter(0, 0, color='green', s=200, marker='o', 
               label='Start (0,0)', zorder=5, edgecolors='black', linewidths=2)
    ax.scatter(path_x[-1], path_y[-1], color='red', s=200, marker='*', 
               label='End Point', zorder=5, edgecolors='black', linewidths=2)
    
    # Add legend with statistics
    legend_text = (f'Total Distance: {total_distance:.2f} km\n'
                  f'Efficiency: {stats["efficiency"]:.1f}%\n'
                  f'Bearing: {stats["bearing"]:.1f}°')
    ax.text(0.02, 0.98, legend_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    ax.legend(loc='upper right', fontsize=10)
    plt.tight_layout()
    
    # Ask to save
    save_plot = input("\n💾 Save plot as image? (y/n): ").strip().lower()
    if save_plot == 'y':
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            filename = "travel_path"
        plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
        print(f"✅ Plot saved as {filename}.png")
    
    plt.show()
    print("\n👋 Thank you for using Travel Path Simulator!")

# Entry point of the program
if __name__ == "__main__":
    main()
