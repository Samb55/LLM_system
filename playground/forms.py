# forms.py
from django import forms

class LLMForm(forms.Form):
    text = forms.CharField(label="LLM Question", widget=forms.Textarea(attrs={"rows": 5, "cols":100}), help_text="Enter your question here.")
