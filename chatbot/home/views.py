from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import openai

openai.api_key = "Enter your Api Key"


def chat(request):
    return render(request,'index.html')


def chatapi(request):
    if request.method=='POST':
        prompt= request.POST['prompt']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        return JsonResponse(response)
    else:
        HttpResponse(" Bad Request")
 