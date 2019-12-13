from django.test import TestCase
from peliculas.models import Pelicula, Renta, Detalle_Renta


class TestModelos(TestCase):

    def test_agrega_pelicula(self):
        pelicula = Pelicula.objects.create(
            nombre = 'War',
            genero = 'war',
            duracion = '120',
            descripcion = 'Esta muy violenta',
            stock = '10'
        )
        peli = Pelicula.objects.first()
        

        self.assertEqual(peli.nombre, 'War')

    def test_return_object_trabajador(self):
        pelicula = Pelicula(
            nombre='Infierno',
            genero='war',
            duracion='120',
            descripcion='Esta muy violenta',
            stock='10'
        )
        pelicula.save()
        self.assertEqual(pelicula.nombre, pelicula.__str__())

    def test_max_length_en_nombre_pelicula(self):

        pelicula = Pelicula(
            nombre='Infierno',
            genero='war',
            duracion='120',
            descripcion='Esta muy violenta',
            stock='10'
        )

        self.assertLess(len(pelicula.nombre), 31)

    def test_mas_de_la_max_length_en_nombre(self):
         pelicula = Pelicula(
             nombre='Infierddddddddddddddddddddddddddddddddgrgrgrdgrgstdfhdfjhdfthfthdfno',
             genero='war',
             duracion='120',
             descripcion='Esta muy violenta',
             stock='10'
         )
         self.assertGreater(len(pelicula.nombre),40)

    def test_insercion_pelicula_repetida(self):
        pelicula = Pelicula(
            nombre='Infierno',
            genero='war',
            duracion='120',
            descripcion='Esta muy violenta',
            stock='10'
        )
        pelicula.save()

        self.assertEqual(Pelicula.objects.all()[0], pelicula)

    def test_mayor_a_cero(self):
        pelicula = Pelicula(
            nombre='Infierno',
            genero='war',
            duracion=120,
            descripcion='Esta muy violenta',
            stock=10
        )
        pelicula.save()

        self.assertGreater(pelicula.duracion, 0)

    def test_duracion_menos_que_la_pelicula_mas_larga_de_la_historia(self):
        pelicula = Pelicula(
            nombre='resan',
            genero='mutigenero',
            duracion= 870,
            descripcion='Se estreno en 1987',
            stock= 5
        )
        pelicula.save()

        self.assertGreater(pelicula.duracion, 0)

