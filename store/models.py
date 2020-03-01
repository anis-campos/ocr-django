from django.db import models


class Artist(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True)


class Album(models.Model):
    def __str__(self):
        return self.title

    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()

    artists = models.ManyToManyField(Artist, related_name="albums", blank=True)


class Contact(models.Model):
    def __str__(self):
        return self.name

    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)


class Booking(models.Model):
    def __str__(self):
        return self.contact.name

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
