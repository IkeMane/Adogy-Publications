# README for WordPress Article Generation Script

## Overview

This script is designed to automate the creation of WordPress articles using OpenAI's GPT models. It focuses on generating different sections of an article about "Top US Media Publications," including methodology, introduction, sections for each publication, an overview, and a table of contents. The script uses JSON data for publications and outputs the article content in Markdown format.


## Setup

1. **Install Required Packages**: Ensure you have the all the required packages installed. You can install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **API Key**: Store your OpenAI API key in an `.env` file in the following format:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Publications JSON File**: Prepare a JSON file named `publications.json` with the structure:

   ```json
   {
       "publications": [
           {
               "Title": "CNN News",
               "URL": "https://news.cnn.com",
               "Image URL": "https://images.cnn.com/logo.png"
           },
           ...
       ]
   }
   ```

This can be used for anything from products to collections

## Functions

- `upload_file(file_path, purpose)`: Uploads a file to OpenAI and returns its ID.
- `methodology(keyword)`: Generates a methodology section in Markdown.
- `introduction(article)`: Creates an introduction section for the article.
- `read_publications(filename)`: Reads publication data from a JSON file.
- `generate_sections(methodology, keyword, publications)`: Generates sections for each publication.
- `overview(keyword, rated_publications)`: Creates an overview section for the article.
- `table_of_contents(article)`: Generates a table of contents for the article.

## Usage

Run the script to generate an article. The final output will be printed in the console. It will include:

- An introduction.
- A table of contents.
- An overview of the article.
- A methodology section.
- Individual sections for each publication listed in the `publications.json` file.

## Example Article Structure

The generated article will be structured as follows:

1. Introduction
2. Table of Contents
3. Overview
4. Methodology
5. Sections for Each Publication

Each section will be formatted in Markdown, suitable for WordPress article creation.

## Notes

- The script assumes you have a valid OpenAI API key and sufficient tokens for API calls.
- The quality of the generated content depends on the input prompts and the GPT model's capabilities.
- Remember to review and edit the generated content as needed to ensure accuracy and coherence.

## Future Enhancements

- Integration with WordPress API for direct publishing.
- Enhanced error handling and response validation.
- Dynamic content generation based on real-time data.
- Improved Handling of Markdown for seamless automation
