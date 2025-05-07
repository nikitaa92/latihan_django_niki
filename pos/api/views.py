from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from pos_app.models import User,TableResto
from api.serializers import TableRestoSerializer
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer


class TableRestoListApiView(APIView):
    serializer_class=TableRestoSerializer
    def get (self,request,*args,**kwargs):
        table_restos= TableResto.objects.all()
        serializers= TableRestoSerializer(table_restos,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        # serializers=self.serializer_class(data=request.data)
        
        data={
            'code':request.query_params.get('code'),
            'name':request.query_params.get('name'),
            'capacity':request.query_params.get('capacity')
        }
        serializers = TableRestoSerializer (data=data)
        if serializers.is_valid():

            serializers.save()
            response={
                'status':status.HTTP_201_CREATED,
                'message':'Data created successfully...',
                'data':serializers.data
            }
            #return Response (serializers.data,status=status.HTTP_201_CREATED)
            return Response (response,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
class TableRestoDetailApiView(APIView):
    def get_object(self, id):
        try:
            return TableResto.objects.get(id=id)
        except TableResto.DoesNotExist:
            return None
        
    def get(self, request, id, *args, **kwargs):
        table_resto_instance = self.get_object(id)
        if not table_resto_instance:
            return Response(
                {
                'status':status.HTTP_404_BAD_REQUEST,
                'message':'Data does not exists...',
                'data': {}
            
                },status= status.HTTP_400_BAD_REQUEST
            )
        
        serializer = TableRestoSerializer(table_resto_instance)
        response = {
            'status':status.HTTP_404_BAD_REQUEST,
            'message':'Data retrieve successfully...',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
        
    def put(self, request, id, *args, **kwargs):
        table_resto_instance = self.get_object(id)
        if not table_resto_instance:
            return Response(
                {
                    'status':status.HTTP_404_BAD_REQUEST,
                    'message':'Data does not exists...',
                    'data': {}
                }, status= status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'code': request.query_params.get('code'),
            'name': request.query_params.get('name'),
            'capacity': request.query_params.get('capacity'),
            'table_status':request.query_params.get('table_status'),
            'status': request.query_params.get('status'),
        }
        serializer = TableRestoSerializer(instance = table_resto_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status':status.HTTP_200_OK,
                'message':'Data updated successfully...',
                'data': serializer.data
            }
            return Response(response, status= status.HTTP_200_OK)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, *args, **kwargs):
        table_resto_instance = self.get_object(id)
        if not table_resto_instance:
            return Response(
                {
                    'status':status.HTTP_400_BAD_REQUEST,
                    'message':'Data does not exists...',
                    'data': {}
                }, status= status.HTTP_400_BAD_REQUEST
            )
        table_resto_instance.delete()
        response ={
            'status':status.HTTP_200_OK,
            'message':'Data deleted successfully...', 
        }
        return Response(response, status= status.HTTP_200_OK)

class RegisterUserApiView(APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Selamat anda telah terdaftar...',
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({
            'status':status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)