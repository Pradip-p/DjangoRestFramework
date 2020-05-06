from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
from . models import product
from rest_framework import status



@api_view(['GET','POST'])
def product_list(request):
    if request.method=='GET':
        obj=product.objects.all()
        serializer=ProductSerializers(obj,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def  product_detail(request,pk):
    try:
        obj=product.objects.all()
    except product.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
    serializer=ProductSerializers(obj)
    return Response(serializer.data)