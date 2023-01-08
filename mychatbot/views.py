from django.shortcuts import render

# Import libraries
import requests
import json
import openai
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


# Function to handle an HTTP POST request from the front-end
def handle_post_request(request):
    # Get the message from the request body
    print(request.body)
    data = json.loads(request.body)
    prompt = data["message"]
    print(data)

    # Send the message to the ChatGPT API using an HTTP POST request
    openai.api_key = "YOUR_API_KEY"
    try:
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except openai.api_errors.ApiError as e:
        # Handle API errors here
        return "An error occurred while processing your request: {}".format(e)

    # Get the response text from the ChatGPT API
    message = completion.choices[0].text
    print(message)

    # Return the response text to the front-end
    return HttpResponse(message)