import grpc
from concurrent import futures
import drawing_pb2
import drawing_pb2_grpc
import json

class DrawingAPIService(drawing_pb2_grpc.DrawingAPIServicer):
    def DrawCircle(self, request, context):
        shape_data = json.loads(request.shape_data)
        return drawing_pb2.DrawResponse(
            render_result=f"Drawing {request.api_type} circle at ({shape_data['x']}, {shape_data['y']}) "
                          f"with radius {shape_data['radius']}"
        )

    def DrawRectangle(self, request, context):
        shape_data = json.loads(request.shape_data)
        return drawing_pb2.DrawResponse(
            render_result=f"Drawing {request.api_type} rectangle at ({shape_data['x']}, {shape_data['y']}) "
                          f"with width {shape_data['width']} and height {shape_data['height']}"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drawing_pb2_grpc.add_DrawingAPIServicer_to_server(DrawingAPIService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Drawing APIs service started on port 50052")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()