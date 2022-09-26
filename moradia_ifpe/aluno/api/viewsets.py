from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from moradia_ifpe.aluno.api.serializers import AlunoSerializer, PostAlunoSerializer
from moradia_ifpe.aluno.models import Aluno


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(request_body=PostAlunoSerializer)
    def create(self, request, *args, **kwargs):
        self.serializer_class = PostAlunoSerializer
        return super(AlunoViewSet, self).create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(AlunoViewSet, self).get_queryset()
        params = {index: value[0] for index, value in self.request.query_params.items()}
        queryset = queryset.filter(**params)
        return queryset
