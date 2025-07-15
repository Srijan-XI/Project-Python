import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# AI Model Trainer
class AIPredictor:
    def __init__(self):
        self.model = self.train_model()

    def train_model(self):
        X = [
            [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2],
            [3, 3], [4, 3], [5, 3], [6, 3],
            [3, 4], [4, 4], [5, 4]
        ]
        y = [
            "Triangle", "Quadrilateral", "Pentagon", "Hexagon", "Heptagon", "Octagon",
            "Triangular Prism", "Cube or Tetrahedron", "Pentagonal Prism", "Hexagonal Prism",
            "5-cell (4-simplex)", "Tesseract (4D Hypercube)", "Penteract"
        ]
        model = KNeighborsClassifier(n_neighbors=1)
        model.fit(X, y)
        return model

    def predict(self, sides, dimension):
        try:
            return self.model.predict([[sides, dimension]])[0]
        except Exception:
            return "Unknown Shape"


# Shape Detector
class ShapeDetector:
    def __init__(self, sides, dimension):
        self.sides = sides
        self.dimension = dimension
        self.shape_name = ""

    def detect_shape(self):
        if self.dimension == 2:
            return self.get_2d_shape()
        elif self.dimension == 3:
            return self.get_3d_shape()
        elif self.dimension == 4:
            return self.get_4d_shape()
        return "Unknown Dimension"

    def get_2d_shape(self):
        shape_dict = {
            3: "Triangle", 4: "Quadrilateral", 5: "Pentagon",
            6: "Hexagon", 7: "Heptagon", 8: "Octagon", 9: "Nonagon", 10: "Decagon"
        }
        return shape_dict.get(self.sides, "Unknown 2D Shape")

    def get_3d_shape(self):
        shape_dict = {
            3: "Triangular Prism", 4: "Cube or Tetrahedron",
            5: "Pentagonal Prism", 6: "Hexagonal Prism"
        }
        return shape_dict.get(self.sides, "Unknown 3D Shape")

    def get_4d_shape(self):
        shape_dict = {
            3: "5-cell (4-simplex)", 4: "Tesseract (4D Hypercube)", 5: "Penteract"
        }
        return shape_dict.get(self.sides, "Unknown 4D Shape")


# Visualization Class
class ShapeVisualizer:
    def draw_2d_polygon(self, n):
        if n < 3:
            print("Cannot draw a 2D shape with less than 3 sides.")
            return
        theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
        x, y = np.cos(theta), np.sin(theta)
        x, y = np.append(x, x[0]), np.append(y, y[0])
        plt.figure(figsize=(5, 5))
        plt.plot(x, y, marker='o')
        plt.fill(x, y, alpha=0.3)
        plt.title(f"{n}-sided Polygon (2D)")
        plt.axis('equal')
        plt.grid(True)
        plt.show()

    def draw_3d_cube(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        verts = [
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
        ]
        faces = [
            [verts[0], verts[1], verts[2], verts[3]],
            [verts[4], verts[5], verts[6], verts[7]],
            [verts[0], verts[1], verts[5], verts[4]],
            [verts[2], verts[3], verts[7], verts[6]],
            [verts[1], verts[2], verts[6], verts[5]],
            [verts[4], verts[7], verts[3], verts[0]]
        ]
        ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='black', alpha=0.5))
        ax.set_title("3D Cube")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def draw_4d_tesseract(self):
        print("\n[4D Shape Visualization - Tesseract]")
        print("A tesseract is the 4D analogue of a cube.")
        print("Visualized as a cube inside a cube, with connecting lines.")
        print("(True 4D can't be rendered in 3D space)\n")


# Main Program
def main():
    print("=== Multi-Dimensional Shape Analyzer ===\n")
    try:
        sides = int(input("Enter number of sides (base polygon or shape faces): "))
        dimension = int(input("Enter the dimension (2, 3, or 4): "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    predictor = AIPredictor()
    ai_prediction = predictor.predict(sides, dimension)

    detector = ShapeDetector(sides, dimension)
    rule_based_shape = detector.detect_shape()

    print(f"\n🧠 AI Predicted Shape: {ai_prediction}")
    print(f"📐 Rule-based Shape: {rule_based_shape}")
    print(f"📊 Final Decision: {ai_prediction if ai_prediction != 'Unknown Shape' else rule_based_shape}\n")

    visualizer = ShapeVisualizer()
    if dimension == 2:
        visualizer.draw_2d_polygon(sides)
    elif dimension == 3:
        if sides == 4:
            visualizer.draw_3d_cube()
        else:
            print("Only cube visualization (4-sided base) supported for 3D.")
    elif dimension == 4:
        visualizer.draw_4d_tesseract()
    else:
        print("Unsupported dimension.")

if __name__ == "__main__":
    main()
