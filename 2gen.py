from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
Client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

list_of_publications = ["CNN","NBC","FOX","ABC","CBS","BBC","NYT","WSJ","LAT","WP"]

def generate_methodology():
    systemmsg = "You are a methodology generator for ranking items and categories. "
    methodology_messages = list()
    methodology_messages.append({"role": "system", "content": systemmsg})
    methodology_messages.append({"role": "user", "content": f"create a methodology to rank these, this will be public facing for an article: {list_of_publications}"})
    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=methodology_messages,
    )
    response_message = response.choices[0].message.content
    # print(response_message)
    return response_message


def generate_ranking(methodology):
    rated_publications = ""
    systemmsg = f"You are a ranking system for news publications.Rate it using the following methodology: {methodology} "
    generate_ranking_messages = list()
    generate_ranking_messages.append({"role": "system", "content": systemmsg})
    for i in list_of_publications:
        generate_ranking_messages.append({"role": "user", "content": f"Rate the following publication based off the methodolgy, keep it under one paragraph and sound like a jounralist: {i}"})
        # print(generate_ranking_messages)
        response = Client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=generate_ranking_messages,
        )
        response_message = response.choices[0].message.content
        generate_ranking_messages.append({"role": "assistant", "content":response_message})
        # print(response_message)
        rated_publications += response_message + "\n\n"
        # print("\n Response Message: ",response_message)
        # print("\n All Responses: ",rated_publications)
    return rated_publications




def generate_article(table_of_contents,title,rated_publications, methodology):
    systemmsg = f"You are a writer for a news publication."
    generate_article_messages = list()
    generate_article_messages.append({"role": "system", "content": systemmsg})
    generate_article_messages.append({"role": "user", "content": f"Write an article with the following theme: {title}. With the following table of contents(include everything from the table of contents and no more or less): {table_of_contents}... \n Based off of the following methodology: {methodology}... \n the following content was generated: {rated_publications}"})
    response = Client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=generate_article_messages,
    )
    response_message = response.choices[0].message.content
    # print(response_message)
    return response_message



def edit_sudjestions(article):
    systemmsg = f"You are an pre editor for a news publication. You come up with improvements to be given to the editor without rewiting the article for him. "
    edit_article_messages = list()
    edit_article_messages.append({"role": "system", "content": systemmsg})
    edit_article_messages.append({"role": "user", "content": f"Find all potential improvments and find the keywords we might want to rank for SEO: {article}"})
    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=edit_article_messages,
    )
    response_message = response.choices[0].message.content
    # print(response_message)
    return response_message



def edit_article(sudjestions,article):
    systemmsg = f"You are an editor for a news publication. What you output will be live on the wordpress site so be sure not to say anthing that the end user shouldnt see."
    edit_article_messages = list()
    edit_article_messages.append({"role": "system", "content": systemmsg})
    edit_article_messages.append({"role": "user", "content": f"You have been given the some feedback from the pre editor about the following wordpress article: {sudjestions}...\n Edit the following article using the sudjestions: {article}"})
    response = Client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=edit_article_messages,
    )
    response_message = response.choices[0].message.content
    # print(response_message)
    return response_message


def main():
    methodology = generate_methodology()
    rated_publications = generate_ranking(methodology)
    print("Rated Publications: \n\n",rated_publications)
    title = "Top 10 News Publications"
    table_of_contents = "Table of Contents: \n Introduction\n Top Publications overview (one sentence overview)\n Methodology\n Each publication name\n"
    article = generate_article(table_of_contents,title,rated_publications, methodology)
    print("Article: \n\n",article)

    # sudjestions = edit_sudjestions(rated_publications)
    # edit_article(sudjestions,article)



if __name__ == "__main__":
    main()

##############################################################################################################
#introduction - do this after the article is written
#table of contents - do this after everything is put together
#generate overview - do this after the all sections are built out
    
    #how do i know how many sections to build based off article title?
    
#build sections
    #create methodology- do this first
    #generate ranking - do this second
    #Get images from links - will have to use assistants to run these
    #get external links
    #get internal links

#generate 


##############################################################################################################
    

