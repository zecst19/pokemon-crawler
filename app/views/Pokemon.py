from pydoc import describe
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
import requests
import random

from app.serializers.Pokemon import PokemonSerializer
from app.models.Pokemon import Pokemon

class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        queryset = Pokemon.objects.all().order_by('number')
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        name = request.query_params['name']
        pokeapi_url = 'https://pokeapi.co/api/v2/pokemon/'+name
        res = requests.get(pokeapi_url, headers={})
        if res.status_code == 200:
            res_json = res.json()
            Pokemon.objects.update_or_create(
                name = res_json['name'],
                number = res_json['id'],
                defaults={
                    'description': '',
                    'types': [t['type']['name'] for t in res_json['types']],
                    'stats': res_json['stats']
                }
            )
            return Response('Pokemon discovered!', status=status.HTTP_201_CREATED)

        return Response('No Pokemon found!', status=status.HTTP_404_NOT_FOUND)

    def encounter(self, request):
        number = random.randint(1, 1154)
        pokeapi_url = 'https://pokeapi.co/api/v2/pokemon/'+str(number)
        
        res = requests.get(pokeapi_url, headers={})
        if res.status_code == 200:
            res_json = res.json()
            Pokemon.objects.update_or_create(
                name = res_json['name'],
                number = res_json['id'],
                defaults={
                    'description': '',
                    'types': [t['type']['name'] for t in res_json['types']],
                    'stats': res_json['stats']
                }
            )
            return Response('Random Pokemon Encounter!', status=status.HTTP_201_CREATED)

        return Response('No Pokemon found!',  status=status.HTTP_404_NOT_FOUND)


