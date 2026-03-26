from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Team, Activity, Workout, LeaderboardEntry

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        LeaderboardEntry.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', first_name='Tony', last_name='Stark')
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', first_name='Steve', last_name='Rogers')
        bruce = User.objects.create_user(username='bruce', email='bruce@dc.com', first_name='Bruce', last_name='Wayne')
        clark = User.objects.create_user(username='clark', email='clark@dc.com', first_name='Clark', last_name='Kent')
        marvel.members.add(tony, steve)
        dc.members.add(bruce, clark)

        # Create Activities
        from datetime import date
        Activity.objects.create(user=tony, activity_type='Run', duration=30, calories_burned=300, date=date.today(), team=marvel)
        Activity.objects.create(user=steve, activity_type='Swim', duration=45, calories_burned=400, date=date.today(), team=marvel)
        Activity.objects.create(user=bruce, activity_type='Bike', duration=60, calories_burned=500, date=date.today(), team=dc)
        Activity.objects.create(user=clark, activity_type='Yoga', duration=50, calories_burned=200, date=date.today(), team=dc)

        # Create Workouts
        Workout.objects.create(user=tony, name='Avengers HIIT', description='High intensity workout for Marvel heroes')
        Workout.objects.create(user=bruce, name='Justice League Strength', description='Strength training for DC heroes')

        # Create Leaderboard
        LeaderboardEntry.objects.create(user=tony, team=marvel, score=1000)
        LeaderboardEntry.objects.create(user=steve, team=marvel, score=900)
        LeaderboardEntry.objects.create(user=bruce, team=dc, score=950)
        LeaderboardEntry.objects.create(user=clark, team=dc, score=980)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
