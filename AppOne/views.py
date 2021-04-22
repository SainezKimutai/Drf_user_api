from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

# ================== Function Based View ======================================

# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         AllArticles = Article.objects.all()
#         MySerializer = ArticleSerializer(AllArticles, many=True)
#         return JsonResponse(MySerializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         MySerializer = ArticleSerializer(data=data)
#         if MySerializer.is_valid():
#             MySerializer.save()
#             return JsonResponse(MySerializer.data, status=201)
#         return JsonResponse(MySerializer.errors, status=400)
#
#
# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article_instance = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         error_message = {"message": "Not Found"}
#         return JsonResponse(error_message, status=404)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article_instance)
#         return JsonResponse(serializer.data)
#
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         MySerializer = ArticleSerializer(article_instance, data=data)
#         if MySerializer.is_valid():
#             MySerializer.save()
#             return JsonResponse(MySerializer.data, status=201)
#         return JsonResponse(MySerializer.errors, status=400)
#
#     if request.method == 'DELETE':
#         article_instance.delete()
#         response_message = {"Object deleted successfully"}
#         return HttpResponse(response_message, status=200)


# # ============================= API View ======================================
@api_view(["GET", "POST"])
def article_list(request):
    if request.method == 'GET':
        AllArticles = Article.objects.all()
        MySerializer = ArticleSerializer(AllArticles, many=True)
        return Response(MySerializer.data)

    elif request.method == 'POST':
        #  request.POST or request.data
        data = request.POST
        MySerializer = ArticleSerializer(data=data)
        if MySerializer.is_valid():
            MySerializer.save()
            return Response(MySerializer.data, status=status.HTTP_201_CREATED)
        return Response(MySerializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, pk):
    try:
        article_instance = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        error_message = {"message": "Not Found"}
        return JsonResponse(error_message, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = request.data
        MySerializer = ArticleSerializer(article_instance, data=data)
        if MySerializer.is_valid():
            MySerializer.save()
            return Response(MySerializer.data)
        return Response(MySerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        article_instance.delete()
        response_message = {"message": "Object deleted successfully"}
        return Response(response_message, status=status.HTTP_200_OK)


# ============================= Class Based Views ============================
class ArticleAPIView(APIView):

    def get(self, request):
        AllArticles = Article.objects.all()
        MySerializer = ArticleSerializer(AllArticles, many=True)
        return Response(MySerializer.data)

    def post(self, request):
        data = request.POST
        MySerializer = ArticleSerializer(data=data)
        if MySerializer.is_valid():
            MySerializer.save()
            return Response(MySerializer.data, status=status.HTTP_201_CREATED)
        return Response(MySerializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            error_msg = {"message": "Not Found"}
            return JsonResponse(error_msg, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article_instance = self.get_object(id)
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data)

    def put(self, request, id):
        data = request.data
        article_instance = self.get_object(id)
        MySerializer = ArticleSerializer(article_instance, data=data, partial=True)
        if MySerializer.is_valid():
            MySerializer.save()
            return Response(MySerializer.data)
        return Response(MySerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article_instance = self.get_object(id)
        article_instance.delete()
        response_message = {"message": "Object deleted successfully"}
        return Response(response_message, status=status.HTTP_200_OK)


# ================= Generic Views ====================================
class ArticleGenericApiView(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            ):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ArticleDetailsGenericApiView(generics.GenericAPIView,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# ================= View Set ====================================

class ArticlesViewSet(viewsets.ViewSet):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            error_msg = {"message": "Not Found"}
            return JsonResponse(error_msg, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        AllArticles = Article.objects.all()
        MySerializer = ArticleSerializer(AllArticles, many=True)
        return Response(MySerializer.data)

    def create(self, request):
        data = request.POST
        MySerializer = ArticleSerializer(data=data)
        if MySerializer.is_valid():
            MySerializer.save()
            return Response(MySerializer.data, status=status.HTTP_201_CREATED)
        return Response(MySerializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        article_instance = self.get_object(pk)
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data
        article_instance = self.get_object(pk)
        MySerializer = ArticleSerializer(article_instance, data=data, partial=True)
        if MySerializer.is_valid():
            MySerializer.save()
            return Response(MySerializer.data)
        return Response(MySerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        article_instance = self.get_object(pk)
        article_instance.delete()
        response_message = {"message": "Object deleted successfully"}
        return Response(response_message, status=status.HTTP_200_OK)


# =============== GenericViewSet ========================================
class ArticlesGenericViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# =============== ModelViewSet ========================================
class ArticlesModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
