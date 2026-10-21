from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PostModel
from .serializers import PostSerializer
from drf_spectacular.utils import extend_schema

# Create your views here.

def get_post(pk):
    return PostModel.objects.filter(pk=pk).first()


NOT_FOUND = {'error': 'Post topilmadi'}


class PostListView(APIView):
    @extend_schema(tags=['Posts'], summary="Postlar ro'yxati", responses=PostSerializer(many=True))
    def get(self, request):
        posts = PostModel.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostCreateView(APIView):
    @extend_schema(tags=['Posts'], summary="Yangi post yaratish", request=PostSerializer, responses=PostSerializer)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class PostDetailView(APIView):
    @extend_schema(tags=['Posts'], summary="Bitta postni ko'rish", responses=PostSerializer)
    def get(self, request, pk):
        post = get_post(pk)
        if post is None:
            return Response(NOT_FOUND, status=404)
        return Response(PostSerializer(post).data)

class PostUpdateView(APIView):
    @extend_schema(tags=['Posts'], summary="Postni yangilash", request=PostSerializer, responses=PostSerializer)
    def put(self, request, pk):
        post = get_post(pk)
        if post is None:
            return Response(NOT_FOUND, status=404)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class PostDeleteView(APIView):
    @extend_schema(tags=['Posts'], summary="Postni o'chirish", responses={204: None})
    def delete(self, request, pk):
        post = get_post(pk)
        if post is None:
            return Response(NOT_FOUND, status=404)
        post.delete()
        return Response(status=204)