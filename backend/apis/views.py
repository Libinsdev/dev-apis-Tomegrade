from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
import csv



class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


@api_view(['GET'])
def userinfo(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
def university_course(request,pk):
    courses=course_offer_university.objects.all().get(university_name=pk)
    serializer=universitycourseSerializer(courses)
    return Response(serializer.data)


@api_view(["GET"])
def course_books(request,pk):
    temp=[]
    course_books=books.objects.only(eng_branch=pk)
    for x in course_books:
        serializer=coursebooksSerializer(x)
        temp.append(serializer.data)
    return Response(temp)


class CustomFiltering(APIView):

    def get(self,request,*args,**kwargs):
        queryset=books.objects.only('course_name')
        print(queryset.query)
        print(queryset) 

        course_name=self.request.query_params.get('course_name')
        branch=self.request.query_params.get('eng_branch')
        semester=self.request.query_params.get('semester')

        if branch:
            queryset=queryset.filter(eng_branch=branch)
        if course_name:
            queryset=queryset.filter(course_name=course_name)
        if semester:
            queryset=queryset.filter(semester=semester)
            
        serializer=CustomSearchSerializer(queryset,many=True)
        print(serializer)

        return Response(serializer.data)


fs=FileSystemStorage(location='tmp/')

@api_view(['POST'])
def upload_data(request):
    file=request.FILES["file"]
    content =file.read()
    file_content=ContentFile(content)
    file_name=fs.save(
    "_tmp.csv" , file_content
    )
    tmp_file=fs.path(file_name)
    csv_file=open(tmp_file,errors="ignore")
    reader=csv.reader(csv_file)
    next(reader)
    book_list=[]

    for id_, row in enumerate(reader):
        (Semester,Department,Course_Name,NULLy,Textbook_Name
        )=row 
            
        book_list.append(
                books(
                 semester=Semester,
                 eng_branch=Department,
                 course_name=Course_Name,
                 book_code=NULLy,
                 book_name=Textbook_Name
                )
        )

        
    books.objects.bulk_create(book_list)

    return Response('uploaded')



