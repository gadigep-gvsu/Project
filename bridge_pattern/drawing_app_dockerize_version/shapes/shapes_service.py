import grpc
from concurrent import futures
import drawing_pb2
import drawing_pb2_grpc
import json

class Shape:
    def __init__(self, x, y, width=None, height=None, radius=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius

class ShapesService(drawing_pb2_grpc.ShapesServicer):
    def CreateCircle(self, request, context):
        circle = Shape(
            x=request.x, 
            y=request.y, 
            radius=request.radius
        )
        return drawing_pb2.ShapeResponse(
            shape_id="circle_" + str(hash(f"{circle.x}_{circle.y}_{circle.radius}")),
            shape_data=json.dumps({
                "type": "circle",
                "x": circle.x,
                "y": circle.y,
                "radius": circle.radius
            })
        )

    def CreateRectangle(self, request, context):
        rectangle = Shape(
            x=request.x, 
            y=request.y, 
            width=request.width, 
            height=request.height
        )
        return drawing_pb2.ShapeResponse(
            shape_id="rect_" + str(hash(f"{rectangle.x}_{rectangle.y}_{rectangle.width}_{rectangle.height}")),
            shape_data=json.dumps({
                "type": "rectangle", 
                "x": rectangle.x,
                "y": rectangle.y,
                "width": rectangle.width,
                "height": rectangle.height
            })
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drawing_pb2_grpc.add_ShapesServicer_to_server(ShapesService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Shapes service started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()