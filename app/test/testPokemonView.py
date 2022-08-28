from http import client
from unittest import TestCase
from app.models.Pokemon import Pokemon
from rest_framework.test import APIClient


class testPokemonView(TestCase):
    def setUp(self):
        super().setUp()
        
    def test_pokedex(self):
        url_path = '/pokedex/'
        client = APIClient()
        res = client.get(url_path)

        print(res.json())

        self.assertEqual(res.status_code, 200)

    def test_pokemon_found(self):
            url_path = '/pokedex/?name=pikachu'
            client = APIClient()
            res = client.post(url_path)

            print(res.json())
            self.assertEqual(res.status_code, 201)

            poke = Pokemon.objects.get(name='pikachu')
            self.assertNotEqual(poke, None)

    def test_pokemon_not_found(self):
        url_path = '/pokedex/?name=pikachulini'
        client = APIClient()
        res = client.post(url_path)

        self.assertEqual(res.status_code, 404)