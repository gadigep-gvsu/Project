import grpc
import drawing_pb2
import drawing_pb2_grpc
import time

class DrawingClient:
    def __init__(self):
        # Connect to shapes and drawing API services
        self.shapes_channel = grpc.insecure_channel('shapes:50051')
        self.drawing_channel = grpc.insecure_channel('drawing_apis:50052')
        
        self.shapes_stub = drawing_pb2_grpc.ShapesStub(self.shapes_channel)
        self.drawing_stub = drawing_pb2_grpc.DrawingAPIStub(self.drawing_channel)

    def create_and_draw_shapes(self):
        # Create and draw a vector circle
        vector_circle = self.shapes_stub.CreateCircle(
            drawing_pb2.CircleRequest(x=10, y=10, radius=5)
        )
        vector_circle_draw = self.drawing_stub.DrawCircle(
            drawing_pb2.DrawRequest(
                shape_data=vector_circle.shape_data, 
                api_type="Vector"
            )
        )
        print(vector_circle_draw.render_result)

        # Create and draw a raster rectangle
        raster_rect = self.shapes_stub.CreateRectangle(
            drawing_pb2.RectangleRequest(x=15, y=15, width=8, height=12)
        )
        raster_rect_draw = self.drawing_stub.DrawRectangle(
            drawing_pb2.DrawRequest(
                shape_data=raster_rect.shape_data, 
                api_type="Raster"
            )
        )
        print(raster_rect_draw.render_result)

def main():
    # Wait for services to be ready
    time.sleep(10)
    
    client = DrawingClient()
    client.create_and_draw_shapes()

if __name__ == '__main__':
    main()