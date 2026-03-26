from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, LeaderboardEntry

class BasicModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(user=self.user, activity_type='Run', duration=30, calories_burned=300, date='2024-01-01', team=self.team)
        self.workout = Workout.objects.create(user=self.user, name='Morning Routine', description='A simple workout', suggested=True)
        self.leaderboard = LeaderboardEntry.objects.create(user=self.user, team=self.team, score=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_activity_str(self):
        self.assertIn('testuser', str(self.activity))

    def test_workout_str(self):
        self.assertIn('Morning Routine', str(self.workout))

    def test_leaderboard_str(self):
        self.assertIn('testuser', str(self.leaderboard))
