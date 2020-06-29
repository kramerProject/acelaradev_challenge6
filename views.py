from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
import json
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from collections import Counter




# Create your models here.

class Numbers(models.Model):
    question = models.CharField('question', max_length=40)

    @property
    def set_questions(self):
        data=json.loads(self.question)
        result = [item for items, c in Counter(data).most_common()
                  for item in [items] * c]
        final=[]
        for unidade in result:
            final.append(unidade)
        return final

    def __str__(self):
        return f'{self.question} e {self.solution}'

    @property
    def solution(self):
        data=json.dumps(self.set_questions)
        return data

# Serializers
class NumbersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ['question', 'solution']

#views
class NumbersApiViewSet(viewsets.ModelViewSet):
    queryset = Numbers.objects.all()
    serializer_class = NumbersModelSerializer


@api_view(["POST"])
def lambda_function(request):
    solution={}
    data=request.data.get('question')
    result=[item for items, c in Counter(data).most_common()
                  for item in [items] * c]
    solution['solution']=result
    return Response(data=solution)




