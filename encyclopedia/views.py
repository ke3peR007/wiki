from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request, name):
    page_details = util.get_entry(name)
    if not page_details:
        return render(request, "encyclopedia/apology.html", {
            "name": name
        })
    return render(request, "encyclopedia/wiki_page.html", {
        "name": name,
        "page_details": page_details
    })