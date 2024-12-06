# Bridge Pattern Implementation for a Drawing Application

from abc import ABC, abstractmethod

# Implementor Interface (Drawing Implementation)
class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        pass

    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        pass

# Concrete Implementations of Drawing API
class VectorDrawingAPI(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"Vector Drawing: Drawing circle at ({x}, {y}) with radius {radius}")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        print(f"Vector Drawing: Drawing rectangle at ({x}, {y}) with width {width} and height {height}")

class RasterDrawingAPI(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"Raster Drawing: Drawing circle at ({x}, {y}) with radius {radius}")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        print(f"Raster Drawing: Drawing rectangle at ({x}, {y}) with width {width} and height {height}")

# Abstraction
class Shape(ABC):
    def __init__(self, drawing_api: DrawingAPI):
        self._drawing_api = drawing_api
    
    @abstractmethod
    def draw(self) -> None:
        pass
    
    @abstractmethod
    def resize(self, factor: float) -> None:
        pass

# Refined Abstractions
class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self) -> None:
        self._drawing_api.draw_circle(self.x, self.y, self.radius)
    
    def resize(self, factor: float) -> None:
        self.radius *= factor

class Rectangle(Shape):
    def __init__(self, x: float, y: float, width: float, height: float, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self) -> None:
        self._drawing_api.draw_rectangle(self.x, self.y, self.width, self.height)
    
    def resize(self, factor: float) -> None:
        self.width *= factor
        self.height *= factor

# Client code
def main():
    # Create drawing APIs
    vector_api = VectorDrawingAPI()
    raster_api = RasterDrawingAPI()

    # Create shapes with different drawing APIs
    vector_circle = Circle(10, 10, 5, vector_api)
    raster_circle = Circle(20, 20, 7, raster_api)
    
    vector_rectangle = Rectangle(5, 5, 10, 15, vector_api)
    raster_rectangle = Rectangle(15, 15, 8, 12, raster_api)

    # Draw shapes
    print("Drawing Shapes:")
    vector_circle.draw()
    raster_circle.draw()
    vector_rectangle.draw()
    raster_rectangle.draw()

    # Resize shapes
    print("\nResizing Shapes:")
    vector_circle.resize(2)
    raster_circle.resize(0.5)
    vector_rectangle.resize(1.5)
    raster_rectangle.resize(0.75)

    # Draw resized shapes
    print("\nDrawing Resized Shapes:")
    vector_circle.draw()
    raster_circle.draw()
    vector_rectangle.draw()
    raster_rectangle.draw()

if __name__ == "__main__":
    main()