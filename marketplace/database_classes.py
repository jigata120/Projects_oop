from marketplace.models import *

for it in Post.objects.all():
    print(it)
