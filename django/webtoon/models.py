from django.db import models


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.webtoon_id} {self.title}'

class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    created_date = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.episode} {self.title} {self.rating} {self.created_date}'