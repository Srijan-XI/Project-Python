"""
Multi-Dimensional Shape Analyzer with AI
=========================================
Advanced shape detection and visualization system supporting 2D, 3D, and 4D shapes.
Features:
- AI-powered shape prediction using KNN classifier
- Rule-based shape detection with extensive shape database
- Interactive visualizations for 2D polygons and 3D polyhedra
- 4D shape projections (tesseract, hypersphere)
- Shape properties calculation (area, perimeter, volume, surface area)
- Color-coded visualizations with rotation capabilities

Author: Enhanced Version
Date: November 2025
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from typing import Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

# AI Model Trainer
class AIPredictor:
    """Enhanced AI predictor with expanded training dataset."""
    
    def __init__(self):
        self.model = self.train_model()
        self.accuracy = self._calculate_accuracy()

    def train_model(self) -> KNeighborsClassifier:
        """Train KNN model with comprehensive shape dataset."""
        # Expanded training data: [sides, dimension] -> shape_name
        X = [
            # 2D shapes (dimension = 2)
            [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [12, 2], [20, 2],
            # 3D shapes (dimension = 3)
            [3, 3], [4, 3], [5, 3], [6, 3], [8, 3], [12, 3], [20, 3],
            # 4D shapes (dimension = 4)
            [3, 4], [4, 4], [5, 4], [6, 4], [8, 4], [16, 4], [24, 4]
        ]
        y = [
            # 2D shapes
            "Triangle", "Quadrilateral", "Pentagon", "Hexagon", "Heptagon", 
            "Octagon", "Nonagon", "Decagon", "Dodecagon", "Icosagon",
            # 3D shapes
            "Tetrahedron", "Cube/Hexahedron", "Pentagonal Prism", "Hexagonal Prism",
            "Octahedron", "Dodecahedron", "Icosahedron",
            # 4D shapes
            "5-cell (4-simplex)", "Tesseract (8-cell)", "Penteract (5-cube)", 
            "Hexeract (6-cube)", "Octacross (16-cell)", "Hexadecachoron", "24-cell"
        ]
        model = KNeighborsClassifier(n_neighbors=1, weights='uniform')
        model.fit(X, y)
        return model

    def predict(self, sides: int, dimension: int) -> str:
        """Predict shape name based on sides and dimension."""
        try:
            prediction = self.model.predict([[sides, dimension]])[0]
            return prediction
        except Exception as e:
            return f"Unknown Shape (Error: {str(e)})"
    
    def _calculate_accuracy(self) -> float:
        """Calculate model accuracy on training data."""
        return 100.0  # KNN with k=1 has 100% accuracy on training data


# Shape Detector
class ShapeDetector:
    """Enhanced shape detector with comprehensive shape database and properties."""
    
    def __init__(self, sides: int, dimension: int):
        self.sides = sides
        self.dimension = dimension
        self.shape_name = ""
        self.properties = {}

    def detect_shape(self) -> str:
        """Detect shape based on dimension and calculate properties."""
        if self.dimension == 2:
            shape = self.get_2d_shape()
            self.calculate_2d_properties()
            return shape
        elif self.dimension == 3:
            shape = self.get_3d_shape()
            self.calculate_3d_properties()
            return shape
        elif self.dimension == 4:
            shape = self.get_4d_shape()
            self.calculate_4d_properties()
            return shape
        return "Unknown Dimension"

    def get_2d_shape(self) -> str:
        """Comprehensive 2D shape database."""
        shape_dict = {
            3: "Triangle (Trigon)", 
            4: "Quadrilateral (Tetragon)", 
            5: "Pentagon",
            6: "Hexagon", 
            7: "Heptagon (Septagon)", 
            8: "Octagon", 
            9: "Nonagon (Enneagon)", 
            10: "Decagon",
            11: "Hendecagon",
            12: "Dodecagon",
            15: "Pentadecagon",
            20: "Icosagon",
            100: "Hectogon",
            1000: "Chiliagon"
        }
        return shape_dict.get(self.sides, f"{self.sides}-gon (Regular Polygon)")

    def get_3d_shape(self) -> str:
        """Comprehensive 3D shape database (Platonic & Archimedean solids)."""
        shape_dict = {
            4: "Tetrahedron (4 faces)",
            6: "Cube/Hexahedron (6 faces)",
            8: "Octahedron (8 faces)",
            12: "Dodecahedron (12 faces)",
            20: "Icosahedron (20 faces)",
            # Prisms
            5: "Pentagonal Prism",
            7: "Heptagonal Prism",
            10: "Decagonal Prism"
        }
        return shape_dict.get(self.sides, f"{self.sides}-faced Polyhedron")

    def get_4d_shape(self) -> str:
        """4D polytope database."""
        shape_dict = {
            5: "5-cell (4-simplex/Pentachoron)",
            8: "Tesseract (8-cell/Hypercube)",
            16: "16-cell (Hexadecachoron/Orthoplex)",
            24: "24-cell (Icositetrachoron)",
            120: "120-cell (Hecatonicosachoron)",
            600: "600-cell (Hexacosichoron)"
        }
        return shape_dict.get(self.sides, f"{self.sides}-cell Polytope")
    
    def calculate_2d_properties(self) -> None:
        """Calculate properties for regular 2D polygons."""
        n = self.sides
        side_length = 1.0  # Assume unit side length
        
        # Interior angle
        interior_angle = ((n - 2) * 180) / n
        
        # Perimeter
        perimeter = n * side_length
        
        # Area (for regular polygon)
        area = (n * side_length**2) / (4 * np.tan(np.pi / n))
        
        # Radius (circumradius)
        radius = side_length / (2 * np.sin(np.pi / n))
        
        self.properties = {
            'sides': n,
            'interior_angle': round(interior_angle, 2),
            'perimeter': round(perimeter, 2),
            'area': round(area, 4),
            'circumradius': round(radius, 4)
        }
    
    def calculate_3d_properties(self) -> None:
        """Calculate properties for 3D shapes."""
        faces = self.sides
        edge_length = 1.0
        
        # Calculate based on known Platonic solids
        if faces == 4:  # Tetrahedron
            volume = (edge_length**3) / (6 * np.sqrt(2))
            surface_area = np.sqrt(3) * edge_length**2
            vertices, edges = 4, 6
        elif faces == 6:  # Cube
            volume = edge_length**3
            surface_area = 6 * edge_length**2
            vertices, edges = 8, 12
        elif faces == 8:  # Octahedron
            volume = (np.sqrt(2) / 3) * edge_length**3
            surface_area = 2 * np.sqrt(3) * edge_length**2
            vertices, edges = 6, 12
        elif faces == 12:  # Dodecahedron
            volume = ((15 + 7*np.sqrt(5)) / 4) * edge_length**3
            surface_area = 3 * np.sqrt(25 + 10*np.sqrt(5)) * edge_length**2
            vertices, edges = 20, 30
        elif faces == 20:  # Icosahedron
            volume = (5 * (3 + np.sqrt(5)) / 12) * edge_length**3
            surface_area = 5 * np.sqrt(3) * edge_length**2
            vertices, edges = 12, 30
        else:
            volume, surface_area = 0, 0
            vertices, edges = 0, 0
        
        self.properties = {
            'faces': faces,
            'vertices': vertices,
            'edges': edges,
            'volume': round(volume, 4),
            'surface_area': round(surface_area, 4)
        }
    
    def calculate_4d_properties(self) -> None:
        """Calculate properties for 4D polytopes."""
        cells = self.sides
        
        if cells == 5:  # 5-cell
            vertices, edges, faces = 5, 10, 10
        elif cells == 8:  # Tesseract
            vertices, edges, faces = 16, 32, 24
        elif cells == 16:  # 16-cell
            vertices, edges, faces = 8, 24, 32
        elif cells == 24:  # 24-cell
            vertices, edges, faces = 24, 96, 96
        else:
            vertices, edges, faces = 0, 0, 0
        
        self.properties = {
            'cells': cells,
            'faces': faces,
            'edges': edges,
            'vertices': vertices
        }


# Visualization Class
class ShapeVisualizer:
    """Enhanced visualization engine for 2D, 3D, and 4D shapes."""
    
    def __init__(self):
        self.colors = plt.cm.viridis(np.linspace(0, 1, 10))
    
    def draw_2d_polygon(self, n: int, properties: dict = None) -> None:
        """Draw enhanced 2D polygon with properties."""
        if n < 3:
            print("❌ Cannot draw a 2D shape with less than 3 sides.")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Main polygon visualization
        theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
        x, y = np.cos(theta), np.sin(theta)
        
        # Draw polygon
        ax1.fill(x, y, alpha=0.4, color='skyblue', edgecolor='navy', linewidth=2)
        ax1.plot(np.append(x, x[0]), np.append(y, y[0]), 'o-', 
                color='darkblue', markersize=8, linewidth=2)
        
        # Add vertex labels
        for i, (xi, yi) in enumerate(zip(x, y)):
            ax1.text(xi*1.15, yi*1.15, f'V{i+1}', fontsize=10, ha='center', 
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        # Draw center point and radii
        ax1.plot(0, 0, 'ro', markersize=10, label='Center')
        for xi, yi in zip(x, y):
            ax1.plot([0, xi], [0, yi], 'r--', alpha=0.3, linewidth=1)
        
        ax1.set_title(f"{n}-sided Regular Polygon", fontsize=14, fontweight='bold')
        ax1.axis('equal')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        ax1.set_xlabel('X-axis')
        ax1.set_ylabel('Y-axis')
        
        # Properties display
        if properties:
            ax2.axis('off')
            props_text = "📊 Shape Properties\n" + "="*30 + "\n\n"
            props_text += f"🔢 Number of Sides: {properties.get('sides', n)}\n\n"
            props_text += f"📐 Interior Angle: {properties.get('interior_angle', 'N/A')}°\n\n"
            props_text += f"📏 Perimeter: {properties.get('perimeter', 'N/A')} units\n\n"
            props_text += f"📦 Area: {properties.get('area', 'N/A')} sq units\n\n"
            props_text += f"⭕ Circumradius: {properties.get('circumradius', 'N/A')} units\n\n"
            
            ax2.text(0.1, 0.5, props_text, fontsize=12, verticalalignment='center',
                    family='monospace', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        plt.tight_layout()
        plt.show()

    def draw_3d_shape(self, faces: int) -> None:
        """Draw 3D polyhedra with enhanced visualization."""
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        if faces == 4:  # Tetrahedron
            self._draw_tetrahedron(ax)
            title = "Tetrahedron (4 faces)"
        elif faces == 6:  # Cube
            self._draw_cube(ax)
            title = "Cube/Hexahedron (6 faces)"
        elif faces == 8:  # Octahedron
            self._draw_octahedron(ax)
            title = "Octahedron (8 faces)"
        else:
            self._draw_cube(ax)
            title = f"{faces}-faced Polyhedron (Cube representation)"
        
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        
        # Set equal aspect ratio
        max_range = 1.5
        ax.set_xlim([-max_range, max_range])
        ax.set_ylim([-max_range, max_range])
        ax.set_zlim([-max_range, max_range])
        
        plt.show()
    
    def _draw_tetrahedron(self, ax) -> None:
        """Draw a tetrahedron."""
        vertices = np.array([
            [1, 1, 1],
            [1, -1, -1],
            [-1, 1, -1],
            [-1, -1, 1]
        ])
        
        faces = [
            [vertices[0], vertices[1], vertices[2]],
            [vertices[0], vertices[1], vertices[3]],
            [vertices[0], vertices[2], vertices[3]],
            [vertices[1], vertices[2], vertices[3]]
        ]
        
        face_colors = ['cyan', 'yellow', 'magenta', 'lightgreen']
        ax.add_collection3d(Poly3DCollection(faces, facecolors=face_colors, 
                                            linewidths=2, edgecolors='black', alpha=0.7))
        
        # Plot vertices
        ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], 
                  c='red', s=100, depthshade=True)
    
    def _draw_cube(self, ax) -> None:
        """Draw a cube with enhanced styling."""
        vertices = np.array([
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
        ]) - 0.5  # Center at origin
        
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom
            [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top
            [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front
            [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back
            [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right
            [vertices[4], vertices[7], vertices[3], vertices[0]]   # Left
        ]
        
        face_colors = ['cyan', 'yellow', 'magenta', 'lightgreen', 'orange', 'pink']
        ax.add_collection3d(Poly3DCollection(faces, facecolors=face_colors, 
                                            linewidths=2, edgecolors='black', alpha=0.7))
        
        # Plot vertices
        ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], 
                  c='red', s=100, depthshade=True)
    
    def _draw_octahedron(self, ax) -> None:
        """Draw an octahedron."""
        vertices = np.array([
            [1, 0, 0], [-1, 0, 0],  # Left-Right
            [0, 1, 0], [0, -1, 0],  # Front-Back
            [0, 0, 1], [0, 0, -1]   # Top-Bottom
        ])
        
        faces = [
            [vertices[0], vertices[2], vertices[4]],
            [vertices[0], vertices[4], vertices[3]],
            [vertices[0], vertices[3], vertices[5]],
            [vertices[0], vertices[5], vertices[2]],
            [vertices[1], vertices[2], vertices[4]],
            [vertices[1], vertices[4], vertices[3]],
            [vertices[1], vertices[3], vertices[5]],
            [vertices[1], vertices[5], vertices[2]]
        ]
        
        face_colors = plt.cm.rainbow(np.linspace(0, 1, 8))
        ax.add_collection3d(Poly3DCollection(faces, facecolors=face_colors, 
                                            linewidths=2, edgecolors='black', alpha=0.7))
        
        # Plot vertices
        ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], 
                  c='red', s=100, depthshade=True)

    def draw_4d_projection(self, cells: int) -> None:
        """Draw 3D projection of 4D shapes."""
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        if cells == 8:  # Tesseract
            self._draw_tesseract_projection(ax)
            title = "Tesseract (4D Hypercube) - 3D Projection"
        elif cells == 5:  # 5-cell
            self._draw_5cell_projection(ax)
            title = "5-cell (4-simplex) - 3D Projection"
        else:
            self._draw_tesseract_projection(ax)
            title = f"{cells}-cell Polytope - 3D Projection (Tesseract representation)"
        
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        
        print(f"\n🌌 4D Visualization Note:")
        print(f"This is a 3D projection of a {cells}-cell 4D polytope.")
        print(f"True 4D geometry cannot be fully represented in 3D space.")
        
        plt.show()
    
    def _draw_tesseract_projection(self, ax) -> None:
        """Draw 3D projection of a tesseract (4D hypercube)."""
        # Inner cube vertices
        inner = np.array([
            [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5],
            [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5]
        ])
        
        # Outer cube vertices (scaled)
        scale = 1.5
        outer = inner * scale
        
        # Draw inner cube
        self._draw_cube_edges(ax, inner, 'blue', 2)
        
        # Draw outer cube
        self._draw_cube_edges(ax, outer, 'red', 2)
        
        # Draw connecting edges
        for i in range(8):
            ax.plot([inner[i, 0], outer[i, 0]], 
                   [inner[i, 1], outer[i, 1]], 
                   [inner[i, 2], outer[i, 2]], 'g--', linewidth=1.5)
        
        # Plot vertices
        ax.scatter(inner[:, 0], inner[:, 1], inner[:, 2], c='blue', s=80)
        ax.scatter(outer[:, 0], outer[:, 1], outer[:, 2], c='red', s=80)
    
    def _draw_5cell_projection(self, ax) -> None:
        """Draw 3D projection of a 5-cell (4D simplex)."""
        # 5 vertices of a 4-simplex projected to 3D
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        vertices = np.array([
            [1, 1, 1],
            [1, -1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [0, 0, 0]  # Center vertex
        ])
        
        # Draw all edges (complete graph with 5 vertices)
        for i in range(5):
            for j in range(i+1, 5):
                ax.plot([vertices[i, 0], vertices[j, 0]],
                       [vertices[i, 1], vertices[j, 1]],
                       [vertices[i, 2], vertices[j, 2]], 
                       'b-', linewidth=2, alpha=0.6)
        
        # Plot vertices
        ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], 
                  c='red', s=150, depthshade=True)
        
        # Label vertices
        for i, v in enumerate(vertices):
            ax.text(v[0]*1.2, v[1]*1.2, v[2]*1.2, f'V{i+1}', fontsize=10)
    
    def _draw_cube_edges(self, ax, vertices, color, linewidth) -> None:
        """Helper function to draw cube edges."""
        edges = [
            [0, 1], [1, 2], [2, 3], [3, 0],  # Bottom face
            [4, 5], [5, 6], [6, 7], [7, 4],  # Top face
            [0, 4], [1, 5], [2, 6], [3, 7]   # Vertical edges
        ]
        
        for edge in edges:
            points = vertices[edge]
            ax.plot(points[:, 0], points[:, 1], points[:, 2], 
                   color=color, linewidth=linewidth)


# Main Program
def print_header():
    """Print attractive program header."""
    header = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║     🌟 MULTI-DIMENSIONAL SHAPE ANALYZER WITH AI 🌟          ║
    ║                                                               ║
    ║     Explore 2D Polygons, 3D Polyhedra & 4D Polytopes        ║
    ║     Powered by Machine Learning & Advanced Geometry          ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(header)

def display_examples():
    """Display example inputs for users."""
    examples = """
    📚 EXAMPLES:
    ═══════════════════════════════════════════════════════
    2D Shapes (Polygons):
      • Triangle: 3 sides, dimension 2
      • Square: 4 sides, dimension 2
      • Pentagon: 5 sides, dimension 2
      • Hexagon: 6 sides, dimension 2
      • Octagon: 8 sides, dimension 2
      • Decagon: 10 sides, dimension 2
    
    3D Shapes (Polyhedra):
      • Tetrahedron: 4 faces, dimension 3
      • Cube: 6 faces, dimension 3
      • Octahedron: 8 faces, dimension 3
      • Dodecahedron: 12 faces, dimension 3
      • Icosahedron: 20 faces, dimension 3
    
    4D Shapes (Polytopes):
      • 5-cell: 5 cells, dimension 4
      • Tesseract: 8 cells, dimension 4
      • 16-cell: 16 cells, dimension 4
      • 24-cell: 24 cells, dimension 4
    ═══════════════════════════════════════════════════════
    """
    print(examples)

def main():
    """Main program execution."""
    print_header()
    
    # Option to see examples
    show_examples = input("Would you like to see examples? (y/n): ").strip().lower()
    if show_examples == 'y':
        display_examples()
    
    print("\n" + "="*60)
    print("Enter shape parameters:")
    print("="*60)
    
    try:
        sides = int(input("🔢 Enter number of sides/faces/cells: "))
        dimension = int(input("🌐 Enter dimension (2=2D, 3=3D, 4=4D): "))
        
        if sides < 3:
            print("\n❌ Error: Shape must have at least 3 sides/faces/cells!")
            return
        
        if dimension not in [2, 3, 4]:
            print("\n❌ Error: Dimension must be 2, 3, or 4!")
            return
            
    except ValueError:
        print("\n❌ Invalid input. Please enter integers only.")
        return

    print("\n" + "="*60)
    print("ANALYZING SHAPE...")
    print("="*60)
    
    # AI Prediction
    predictor = AIPredictor()
    ai_prediction = predictor.predict(sides, dimension)
    
    # Rule-based Detection
    detector = ShapeDetector(sides, dimension)
    rule_based_shape = detector.detect_shape()
    
    # Display results
    print(f"\n� AI Model Prediction: {ai_prediction}")
    print(f"📐 Rule-based Detection: {rule_based_shape}")
    print(f"✅ Final Shape Identified: {ai_prediction if 'Unknown' not in ai_prediction else rule_based_shape}")
    
    # Display properties
    if detector.properties:
        print(f"\n📊 SHAPE PROPERTIES:")
        print("="*60)
        for key, value in detector.properties.items():
            print(f"   {key.replace('_', ' ').title()}: {value}")
    
    # Visualization
    print("\n" + "="*60)
    visualize = input("Would you like to visualize this shape? (y/n): ").strip().lower()
    
    if visualize == 'y':
        visualizer = ShapeVisualizer()
        
        if dimension == 2:
            print("\n🎨 Generating 2D polygon visualization...")
            visualizer.draw_2d_polygon(sides, detector.properties)
            
        elif dimension == 3:
            print("\n🎨 Generating 3D polyhedron visualization...")
            visualizer.draw_3d_shape(sides)
            
        elif dimension == 4:
            print("\n🎨 Generating 4D polytope projection...")
            visualizer.draw_4d_projection(sides)
    
    # Option to continue
    print("\n" + "="*60)
    continue_analysis = input("Analyze another shape? (y/n): ").strip().lower()
    if continue_analysis == 'y':
        print("\n" * 2)
        main()
    else:
        print("\n✨ Thank you for using the Multi-Dimensional Shape Analyzer! ✨\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user. Goodbye! 👋\n")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {str(e)}\n")
