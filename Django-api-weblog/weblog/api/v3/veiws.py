​from functools import partial
from django.core.serializers import serialize
from django.db.migrations import CreateModel
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


""" drf: 1- method """
@api_view(['GET', 'POST'])
def model_list(request):
    model = ''
    serializer_class = ''

    if request.method == 'GET':
        mod = model.objects.all()
        mod_serial = serializer_class(mod, many=True, context={'request': request})
        return Response(mod_serial.data)

    if request.method == 'POST':
        data = request.data
        mod_serial = serializer_class(data=data)
        mod_serial.is_valid(raise_exception=True)
        mod_serial.save()
        return Response(mod_serial.data)


@api_view(['GET', 'PUT', 'DELETE'])
def model_detail(request):
    model = ''
    serializer_class = ''

    mod = get_object_or_404(model, pk=id)
    if request.method == 'GET':
        try:
            mod = model.objects.get(pk=id)
            mod_after_serial = serializer_class(mod, context={'request': request})
            return Response(mod_after_serial.data)
        except Exception as e:
            return Response({'msg': 'not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data
        mod_after_serial = serializer_class(mod, data=data)
        mod_after_serial.is_valid(raise_exception=True)
        mod_after_serial.save()
        return Response(mod_after_serial.data)

    if request.method == 'DELETE':
        mod.delete()

""" drf: 2- class: APIview """
class ListDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    model = ''
    serializer_class = ''

    def get(self, request, id=None, *args, **kwargs):
        if id is None:
            model_list = self.model.objects.all()
            serializer = self.serializer_class(model_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        model_obj = get_object_or_404(self.model, pk=id)
        serializer = self.serializer_class(model_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        body_req = request.data
        serializer = self.serializer_class(data=body_req)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"created successfully"}, status=status.HTTP_201_CREATED)

    def put(self, request, id=None, *args, **kwargs):
        model_obj = get_object_or_404(self.model, pk=id)
        body_req = request.data
        serializer = self.serializer_class(model_obj, data=body_req)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'updated successfully'}, status=status.HTTP_200_OK)


    def patch(self, request, id=None, *args, **kwargs):
        model_obj = get_object_or_404(self.model, pk=id)
        body_req = request.data
        serializer = self.serializer_class(model_obj, data=body_req, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'updated successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, id=None, *args, **kwargs):
        model_obj = get_object_or_404(self.model, pk=id)
        model_obj.delete()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_200_OK)

""" drf: 3- class: GenericAPIView """
class ListGenericView(GenericAPIView):
    model = ''
    queryset = model.objects.all()
    serializer_class = ''

    def get(self, request, *args, **kwargs):
        model_list = self.get_queryset()
        serializer = self.get_serializer(model_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        body_req = request.data
        serializer = self.get_serializer(data=body_req)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"created successfully"}, status=status.HTTP_201_CREATED)

class DetailGenericView(GenericAPIView):
    model = ''
    queryset = model.objects.all()
    serializer_class = ''
    lookup_field = 'id'

    def get(self, request, id, *args, **kwargs):
        model_obj = self.get_object()
        serializer = self.get_serializer(model_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        model_obj = self.get_object()
        body_req = request.data
        serializer = self.get_serializer(model_obj, data=body_req)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'updated successfully'}, status=status.HTTP_200_OK)

    def patch(self, request, id, *args, **kwargs):
        model_obj = self.get_object()
        body_req = request.data
        serializer = self.get_serializer(model_obj, data=body_req, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'updated successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        model_obj = self.get_object()
        model_obj.delete()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_200_OK)

""" drf: 4- class: Mixin,GenericAPIView """
class ListGenericView(CreateModelMixin,ListModelMixin, GenericAPIView):
    model = ''
    queryset = model.objects.all()
    serializer_class = ''

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class DetailGenericView(DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin, GenericAPIView):
        model = ''
        queryset = model.objects.all()
        serializer_class = ''
        lookup_field = 'id'

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def patch(self, request, *args, **kwargs):
            return self.update(request, partial=True, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)


""" drf: 5- class: GenericView """
class modelListGV(ListGenericView):
    model = ''
    serializer_class = ''

class modelDetailGV(DetailGenericView):
    model = ''
    serializer_class = ''

""" drf: 6- class: ViewSet """
class modelViewSet(viewsets.ViewSet):
    model = ''
    serializer_class = ''

    def list(self, request):
        model_obj = self.get_object()
        serializer = self.serializer_class(model_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        body_req = request.data
        serializer = self.serializer_class(data=body_req)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'model create successfully'}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        model_obj = self.model.objects.get(pk=pk)
        serializer = self.serializer_class(model_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        model_obj = self.model.objects.get(pk=pk)
        body_req = request.data
        serializer = self.serializer_class(model_obj, data=body_req)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'model update successfully'}, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

""" drf: 7- class: ModelViewSet """
class modelModelViewSet(viewsets.ModelViewSet):
    model = ''
    queryset = model.objects.all()
    serializer_class = ''
















































