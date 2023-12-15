from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LLMForm
from .llm_service import LLMService  # Import the LLMService class
import markdown 

def markdownify(text):
    return markdown.markdown(text,extensions=["fenced_code"])


# def index(request):

#     return render(request, "index.html")


def llm_ser(request):
    form = LLMForm()
    if request.method == "POST":
        form = LLMForm(request.POST)
        if form.is_valid():
            llm_service = LLMService()
            text = form.cleaned_data["text"]
            response = llm_service.get_response(text)
            response = markdownify(response)

            context = {"question": text, "response": response, "form": form}
            return render(request, "index.html", context)
    else:
        context = {"form": form}
        return render(request, "index.html", context)
             


    return render(request, "index.html", {"form": form})

