from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import json

load_dotenv()
Client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

keyword = "top us media publications"


def upload_file(file_path, purpose):
    with open(file_path, "rb") as file:
        response = Client.files.create(file=file, purpose=purpose)
    return response.id


def methodology(keyword):
    systemmsg = "You are a methodology section generator for {keyword} ranking its items and or categories. You only output markdown for the article."
    messages = list()
    messages.append({"role": "system", "content": systemmsg})
    prompt = f"Generate a methodology section in plain text but as markdown starting at h2 for a wordpress article titled{keyword}. Include a heading for the section"
    messages.append({"role": "user", "content": prompt})
    response = Client.chat.completions.create(model="gpt-3.5-turbo-1106",messages=messages,)
    response_message = response.choices[0].message.content
    # print(response_message)
    return response_message


def introduction(article):
    systemmsg = "You are an introduction section generator for wordpress articles. You generate a very short introduction"
    messages = list()
    messages.append({"role": "system", "content": systemmsg})
    prompt = f"Generate an short introduction section for a wordpress article format it in plain text but as markdown starting at h2 {article}"
    messages.append({"role": "user", "content": prompt})
    response = Client.chat.completions.create(model="gpt-3.5-turbo-1106",messages=messages,)
    response_message = response.choices[0].message.content
    # print(response_message)
    return response_message



def read_publications(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['publications']


def generate_sections(methodology,keyword,publications):
    rated_publications = ""
    messages = list()
    systemmsg = f"You are a section generator for wordpress articles. Write in a journalist tone and based off {methodology}."
    messages.append({"role": "system", "content": systemmsg})
    for publication in publications:
        name = publication['Title']
        link = publication['URL']
        photo = publication['Image URL']
        prompt = f"Generate a short (one paragraph) section in plain text but as markdown about {name} for the article title {keyword}. Be sure to add their link whenever you mention their name: {link} and include their logo: {photo}."
        messages.append({"role": "user", "content": prompt})
        response = Client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )
        response_message = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_message})
        # print(response_message)
        rated_publications += f"###{publication['Title']}: {response_message}\n\n"
    return rated_publications


def overview(keyword, rated_publications):
    systemmsg = "You are an article overview generator for wordpress articles. You generate the overview with this format in markdown: \n ##Top Tech Publications: \[WIRED](https://www.wired.com/) for tech news presented in a fun, stylish way targeted towards young professionals Top tech publication for readers under age 40 \n [ReadWrite](https://readwrite.com/) for detailed articles on subjects such as SEO, fintech, and software development Top tech publication for e-commerce"
    messages = list()
    messages.append({"role": "system", "content": systemmsg})
    prompt = f"Generate an overview of this article in plain text but as markdown for the article titled {keyword}. Keep it one sentence MAX for each, include a heading h1 for the section. {rated_publications}."
    messages.append({"role": "user", "content": prompt})
    response = Client.chat.completions.create(model="gpt-3.5-turbo-1106",messages=messages,)
    response_message = response.choices[0].message.content
    return response_message

def table_of_contents(article):
    systemmsg = "You are an table of contents generator for wordpress articles. You generate the table of contents with this format in markdown: ##Table of Contents \n [Top Tech Publications](#top-tech-publications) \n ..."
    messages = list()
    messages.append({"role": "system", "content": systemmsg})
    prompt = f"Generate a table of contents for this article in plain text but as markdown with links to headings, include a heading for the section: {article}."
    messages.append({"role": "user", "content": prompt})
    response = Client.chat.completions.create(model="gpt-3.5-turbo-1106",messages=messages,)
    response_message = response.choices[0].message.content
    return response_message

# def grading(article):
#     systemmsg = "You are an editor for wordpress articles."
#     messages = list()
#     messages.append({"role": "system", "content": systemmsg})
#     prompt = f"Come up with potential issues with this article and what could be improved. {article}."
#     messages.append({"role": "user", "content": prompt})
#     response = Client.chat.completions.create(model="gpt-4-1106-preview",messages=messages,)
#     response_message = response.choices[0].message.content
#     return response_message

# def generate_article(article,grading):
#     systemmsg = "You are an writer for wordpress articles."
#     messages = list()
#     messages.append({"role": "system", "content": systemmsg})
#     prompt = f"You are an wordpress article writer fix this article based off the potential improvments, be sure to use markdown as plain text: {grading} and the article: {article}."
#     messages.append({"role": "user", "content": prompt})
#     response = Client.chat.completions.create(model="gpt-4-1106-preview",messages=messages,)
#     response_message = response.choices[0].message.content
#     return response_message



# Example usage
methodology_ = methodology(keyword)
publications = read_publications('publications.json')
sections = generate_sections(methodology_,keyword,publications)
# print("Rankings: ",sections)
overview_ = overview(keyword,sections)
# print("Whole Overview: ",overview_)
article = overview_ +"\n\n"+ methodology_ + "\n\n"+ sections
introduction_ = introduction(article)
table_of_contents_ = table_of_contents(article)
#need to add space between sections
article = introduction_ +"\n\n"+ table_of_contents_ +"\n\n"+ overview_ + "\n\n" + methodology_ +"\n\n"+ sections
print("\n\n\n ARTICLE: ", article)




#TODO def generate_all_publications():
    #basicly create the JSON of all publications with their names and links based off {keyword}


#TODO def screenshot_all_publications():
    #run throught JSON and screenshot all publications homepage - Note: scroll down to avoid ads.


#TODO def generate_ranking(methodology): 
    #prompt: generate ranking for {category} based off {methodology} in JSON format: {category: {publication: {rank: 1, link: https://www.wired.com/, photo: https://www.wired.com/logo.png}}}
    #will give it the doc using assistants API. 

#TODO add assitants API to use doc of our interal links to add to the sections.