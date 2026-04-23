from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create_user(username='alice', email='alice@example.com', password='password')
        user2 = User.objects.create_user(username='bob', email='bob@example.com', password='password')
        user3 = User.objects.create_user(username='carol', email='carol@example.com', password='password')

        # Create teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Create activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, calories_burned=300, date=timezone.now().date(), team=team1)
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, calories_burned=400, date=timezone.now().date(), team=team1)
        Activity.objects.create(user=user3, activity_type='Swimming', duration=60, calories_burned=500, date=timezone.now().date(), team=team2)

        # Create leaderboard
        Leaderboard.objects.create(team=team1, total_points=700)
        Leaderboard.objects.create(team=team2, total_points=500)

        # Create workouts
        Workout.objects.create(user=user1, name='Morning Cardio', description='Cardio session', date=timezone.now().date(), personalized=True)
        Workout.objects.create(user=user2, name='Evening Strength', description='Strength training', date=timezone.now().date(), personalized=False)
        Workout.objects.create(user=user3, name='Yoga Flow', description='Yoga and stretching', date=timezone.now().date(), personalized=True)

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with test data'))
