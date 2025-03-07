from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer
# Create your views here.
@api_view(['GET','POST'])
def index(request):
    courses={
        'course_name':'python',
        'learn':['Flask','Django','Tornado','Fastapi'],
        'course_provider':'scaler'
    }
    if request.method=='GET':
        print("You Have hit the get api")
        return Response(courses)
    elif request.method=='POST':
        print("You have hit the post api")
        return Response(courses)
    
@api_view(['GET','POST','PUT','PATCH'])
def person(request):
        if request.method=="GET":
            Objs=Person.objects.all()
            serializers=PeopleSerializer(Objs, many="true")
            return Response(serializers.data)
        elif request.method=="POST":
            Data=request.data
            serializers=PeopleSerializer(data=Data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        elif request.method=="PUT":
             Data=request.data
             Obj=Person.objects.get(id=Data['id'])
             serializers=PeopleSerializer(Obj,data=Data)
             if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
             else:
                return Response(serializers.errors)
        elif request.method=="PATCH":
            Data=request.data
            Obj=Person.objects.get(id=Data['id'])
            serializers=PeopleSerializer(Obj,data=Data,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)



             

 