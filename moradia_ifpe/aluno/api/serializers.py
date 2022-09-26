from rest_framework import serializers

from moradia_ifpe.aluno.models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    pontuacao = serializers.IntegerField(read_only=True)

    class Meta:
        model = Aluno
        fields = '__all__'

    def to_representation(self, instance):
        instance.pontuacao = instance.get_point()
        return super(AlunoSerializer, self).to_representation(instance)


class PostAlunoSerializer(serializers.ListSerializer):
    child = AlunoSerializer()
