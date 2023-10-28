from django.db import models
from django.contrib.auth.models import User


class Sportnews(models.Model):
    sport = [
        (1, "футбол"),
        (2, "хоккей"),
        (3, "баскетбол"),
        (4, "теннис"),
        (5, "волейбол"),
        (6, "бокс")
    ]

    tsport = models.PositiveSmallIntegerField('tsport', choices=sport)
    title = models.CharField(max_length=100)
    news = models.TextField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def votes(self):
        v = self.coment_set.all().values_list('owner__id', flat=True)
        return v

    def votes_count(self):
        i = self.coment_set.all()
        up_votes = i.filter(value='up').count()
        total_votes = i.count()
        ratio = (up_votes/total_votes)*100
        self.vote_total = total_votes
        self.vote_ratio = ratio
        self.save()


 # Комментарий к статье, 1 пользователь = 1 комментарий
class Coment(models.Model):
    rating = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Sportnews, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=50, choices=rating)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['owner', 'post']]

