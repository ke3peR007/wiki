from django.shortcuts import render
from django.http import HttpResponse
from . import util
from django import forms
import re

class SearchForm(forms.Form):
    search = forms.CharField(label="")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_form": SearchForm()
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

def search(request):
    if request.method == "POST":
        print("inside search ")
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["search"]
            page_details = util.get_entry(data)
            if page_details:
                return render(request, "encyclopedia/wiki_page.html", {
                    "name": data,
                    "page_details": page_details
                })
            if not page_details:
                regex = data
                matched_patterns = []
                entries = util.list_entries()
                for entry in entries:
                    match = re.search(regex, entry)
                    if match != None:
                        print(entry)
                        print(match.group(0))
                        matched_patterns.append(entry)
                if len(matched_patterns) == 0:
                    return render(request, "encyclopedia/apology.html", {
                        "name": data
                    })
                else:
                    return render(request, "encyclopedia/index.html", {
                        "entries" : matched_patterns,
                        "search_form": SearchForm()
                    })
        return HttpResponse("inside search")
