from openai import OpenAI
import json
from dotenv import load_dotenv
import os
import requests
from pexels_api import API
import random

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to search and download images from Pexels
def search_and_download(search_term, filename='image.jpg'):
    PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
    api = API(PEXELS_API_KEY)
    api.search(search_term)
    photos = api.get_entries()

    if photos:
        # Select a random image from the first page of results
        selected_photo = random.choice(photos)
        image_url = selected_photo.original

        # Download the selected image
        img_data = requests.get(image_url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)
        return json.dumps({"search_term": search_term, "image_url": image_url, "saved_as": filename})
    else:
        return json.dumps({"search_term": search_term, "image_url": "None", "saved_as": "None"})




def run_conversation(keyword):
    systemmsg = "You are a article image finder for wordpress articles."

    messages = [{"role": "system", "content": systemmsg}]
    messages.append({"role": "user", "content": f"Find an image for this article titled: {keyword} be sure not to serch for the title but for images that might repesent article e.g: News, or Journalist."})
    tools = [
        {
            "type": "function",
            "function": {
                "name": "search_and_download",
                "description": "Search and downloads a random image from the search term, only call this function once per message. - May have to input the same exact search term a few times to get the perfect image.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_term": {
                            "type": "string",
                            "description": "The term to search for, e.g., 'news'",
                        },
                        "filename": {
                            "type": "string",
                            "description": "File name for the downloaded image, should always be: 'image.jpg'",
                        },
                    },
                    "required": ["search_term"],
                },
            },
        }
    ]

    #loop through this
    while True:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )
        response_message = response.choices[0].message
        print("\n\nResponse 1:",response_message.content)
        tool_calls = response_message.tool_calls

        if tool_calls:
            available_functions = {"search_and_download": search_and_download}
            messages.append(response_message)
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                function_response = function_to_call(
                    search_term=function_args.get("search_term"),
                    filename=function_args.get("filename", "image.jpg"),
                )
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )
            second_response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=messages,
            )
        
            print("\n\nResponse 2:",second_response.choices[0].message.content)
            messages.append(second_response.choices[0].message)

            image_url = json.loads(function_response)["image_url"]
            image_messages = [
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"is this image sutatble for the article titled {keyword}? If not then say no, explain what the image was in one sentence and say try again, you can use the same search term again or a new one if it still isnt working. Note: The image doesnt have to be perfect but it should resemble something in the article."},
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                    },
                    },
                ],
                }
            ]
            
            third_response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=image_messages,
            )

            print("\n\nThird Response: ",third_response.choices[0].message.content)
            messages.append({"role": "user", "content": third_response.choices[0].message.content})

            if "no" in third_response.choices[0].message.content.lower():
                #restart loop
                print("\n\nRestarting loop")
                print(messages)
                continue
                
            else:
                #stop loop
                print("\n\nStopping loop because of yes in response")
                print(messages)
                break
        else:
            #stop loop
            print(messages)
            print("\n\nStopping loop because no tool calls")
            break  


keyword = "top us media publications"
print(run_conversation(keyword))


"""
I can just have one gpt do all the work. 
Wheres it does the search and then the image
comes back to it when its doen with the search asking if this is 
right for the article title
and then it calls the generate new image function if not
and then it repeates if the image is not right..
"""