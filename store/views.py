from django.http import HttpResponse

from .models import Album


def index(request):
    # request albums
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)


def listing(request):
    albums = ["<li>{}</li>".format(album.title) for album in Album.objects.all()]
    message = "<ul>{}</ul>".format("\n".join(albums))
    return HttpResponse(message)


def detail(request, album_id):
    id = int(album_id)
    album = Album.objects.get(pk=id)
    artists = " ".join([artist['name'] for artist in album.artists])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = Album.objects.filter(title__icontains=query)

        if albums.exists() == 0:
            albums = Album.objects.filter(artists__name__icontains=query)

        if albums.exists() == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)
