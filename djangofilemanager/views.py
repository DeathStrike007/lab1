from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os


TESTPATH = os.path.dirname(__file__) + '/' + 'TestFolder'


@api_view(['GET'])
def index(request):
    return Response(os.listdir(TESTPATH))


@api_view(['GET'])
def view(request, name):
    directory = TESTPATH + '/' + str(name)
    if os.path.exists(directory):
        return Response(os.listdir(directory))
    else:
        return Response({'response' : 'Wrong part' + directory + '!'})


@api_view(['GET'])
def download(request, name):
    directory = TESTPATH + '/' + str(name)
    for file in os.listdir(TESTPATH):
        if name == file.split('.')[0]:
            name = file
    filepath = directory
    if os.path.exists(filepath):
        thisfile = open(filepath, "r")
        response = HttpResponse(thisfile)
        response['Content-Disposition'] = 'attachment; filename=NameOfFile'
        return response
    else:
        return Response({'response': 'path ' + filepath + ' is not exist'})


@api_view(['GET'])
def create(request, name):
    directory = TESTPATH + '/' + name
    if os.path.exists(directory):
        response = 'Directory' + str(name) + 'already exists!'
    else:
        os.mkdir(directory)
        response = 'Directory' + str(name) + 'created!'
    return Response({"response": response})


@api_view(['DELETE'])
def delete(request, name):
    directory = TESTPATH + '/' + str(name)
    if os.path.exists(directory):
        if not os.path.isfile(directory):
            os.rmdir(directory)
            response = 'Directory' + str(name) + 'deleted!'
        else:
            response = 'It is file, not a directory!'
    else:
        response = 'Wrong directory!'
    return Response({"response":response})






