from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from apps.users.api.serializer import UserSerializer
from rest_framework.response import Response
from apps.users.models import User
from rest_framework import status
from django.db.models import Q

# Create your views here.


def home(request):
    return HttpResponse('<h1>True Value Access machine test by Karshinas Kans</h1>')


class UserView(APIView):
    def get_object(self, offset, limit, search, sort=None):
        if search:
            return User.objects.filter(Q(first_name=search) | Q(last_name=search)).order_by(sort)[offset:limit]
        return User.objects.all().exclude(is_staff=True).order_by(sort)[offset:limit]

    def get_paginate(self, page, request):
        data = {
            'user': {},
            'links': {}
        }
        if page == 1:
            data['user'] = self.get_object(offset=int(request.GET.get(
                'offset', 0)), limit=int(request.GET.get('limit', 5)), search=request.GET.get('search', None), sort=request.GET.get('sort', 'id'))
            data['links'] = {
                'next': request.build_absolute_uri()+'?'+'page='+str(page+1),
            }
        else:
            data['user'] = self.get_object(
                offset=page*5-5, limit=page*5, search=request.GET.get('search', None))
            data['links'] = {
                'next': request.build_absolute_uri()+'?'+'page='+str(page+1),
                'previous': request.build_absolute_uri()+'?'+'page='+str(page-1),
            }
        return data

    def get(self, request):
        page = int(request.GET.get('page', 1))
        if page*5-5 > User.objects.count():
            return Response(status=404)
        data = self.get_paginate(page, request)
        serializer = UserSerializer(data['user'], many=True)
        return Response({'links': data['links'], 'results': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass


class UserDetailsView(APIView):
    def get_object(self, pk=None, search=None):
        if pk:
            try:
                return User.objects.get(id=pk)
            except:
                raise Http404
        try:
            return User.objects.get(email__icontains=search)
        except:
            raise Http404

    def get(self, request, pk=None):

        user = self.get_object(
            pk=pk, search=request.GET.get('search_email', None))
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        user = self.get_object(
            pk=pk, search=request.GET.get('search_email', None))
        serializer = UserSerializer(instance=user)
        serializer.update_user(request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        user = self.get_object(
            pk, search=request.GET.get('search_email', None))
        user.delete()
        return Response('user deleted', status=status.HTTP_200_OK)
