from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def index(request):
    return Response({"Success": "Index endpoint working"})

@api_view(['GET'])
def get_all_posts(request):
    all_posts = Post.objects.all()
    serializer = PostSerializer(all_posts, many=True)

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "Post successfully created"}, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success": "Post deleted successfully"}, status=200)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)

@api_view(['GET'])
def get_post_by_id(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"Error": "Post does not exist"})

@api_view(['PUT'])
def update_post(request, post_id):
    new_title = request.data.get('title')
    new_content = request.data.get('content')
    try:
        post = Post.objects.get(id=post_id)
        if new_title:
            post.title = new_title
        if new_content:
            post.content = new_content

        post.save()
        return Response({"Success": "Post successfully updated"})
    except Post.DoesNotExist:
        return Response({"Error": "Post does not exist"}, status=404)