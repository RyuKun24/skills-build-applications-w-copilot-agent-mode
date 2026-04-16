from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Use ORM deletes instead of low-level MongoDB drops
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Crear equipos
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='1234', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='1234', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='1234', team=dc)

        # Crear actividades
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        octo_models.Activity.objects.create(user=spiderman, type='cycle', duration=45, distance=20)
        octo_models.Activity.objects.create(user=batman, type='swim', duration=25, distance=1)
        octo_models.Activity.objects.create(user=superman, type='run', duration=60, distance=10)

        # Crear leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, points=100)
        octo_models.Leaderboard.objects.create(user=spiderman, points=80)
        octo_models.Leaderboard.objects.create(user=batman, points=90)
        octo_models.Leaderboard.objects.create(user=superman, points=110)

        # Crear workouts
        octo_models.Workout.objects.create(name='Full Body', description='Entrenamiento completo', duration=60)
        octo_models.Workout.objects.create(name='Cardio', description='Entrenamiento cardiovascular', duration=45)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
