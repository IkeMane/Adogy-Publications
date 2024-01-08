# Project README

## Overview
This Python project is designed to automate the process of generating structured content for digital publications. Leveraging a keyword-driven approach, the script generates comprehensive articles complete with SEO data and images. The methodology involves creating an article structure based on a given keyword, building an overview, a table of contents, and an introduction, followed by the automatic generation of SEO data and sourcing images from Pexels or Dalle 3.


## Features
- **Keyword-Driven Content Generation:** The script uses a specified keyword from the `.env` file to generate a methodical and structured article.
- **Section Building:** Each section of the article is constructed based on the generated data, including an overview, table of contents, and introduction.
- **Screenshoting homepage:** If there is a valid link it will screenshot the link given.
- **SEO Optimization:** Automatically generates SEO data for the article.
- **Image Sourcing:** Sources images from Pexels. If a suitable image is not found, it uses Dalle 3 to generate one.


## Getting Started

### Installation
1. **Install Dependencies:**
   - Clone or download this repository to your local machine.
   - Navigate to the project directory.
   - Install the required packages using the following command:
     ```bash
     pip install -r requirements.txt
     ```

2. **Environment Setup:**
   - Rename the provided `env_example` file to `.env`.
   - Open the `.env` file and fill in your secret keys and other required information.

3. **Configuration:**
   - Within the `.env` file, specify the keyword around which you want your article to be written. For example, "top baby toys", "top news publications", or "top restaurants".


## Google
Setup your Google API including the Custom Search API key, Search Engine ID, Sheet ID, and column letter for URL entries. The workbook name refers to your Google Sheet's name.

### Setup Instructions
Follow these steps to properly set up your environment and dependencies for running the script.

1. **Google Cloud Services Setup**:
   - Create a project in the Google Cloud Console.
   - Enable the Google Sheets and Drive API.
   - Create credentials for your project and download the JSON key file.
   - Store the JSON key file as `google_sheets_api.json` in your project directory.
   - Share your Google Sheet with the email from your JSON key file.

2. **Google Custom Search Setup**:
   - Enable the Google Custom Search API for your project.
   - Set up a search engine at [Google Custom Search Engine](https://cse.google.com/cse/all) and note down your Search Engine ID.
   - Insert your Google API key and Search Engine ID into the script.

3. **Google Sheet ID and Workbook Name**:
   - Find the Sheet ID from your Google Sheets URL.
   - Define the workbook name as the title of your Google Sheet.

4. **Installation**:
   - Install required Python packages from `requirements.txt`.
   - Set up your `.env` file with necessary API keys and credentials.

5. **Execution**:
   - Run the script using `python main.py` to generate and post content.

# Keywords
Specify the main keyword for your article content in the configuration.

```plaintext
KEYWORD='Top tech publications'
```

# Running the Script
Ensure all configurations are correctly set in the `.env` file.

- Execute the main script by running `main.py` from your command line:
  ```bash
  python main.py
  ```

# Upcoming Features (TODO)
- Add randomized author IDs.
- Enable category selection for articles.
- Implement a tagging system.
- Introduce more controls for product-oriented content.

# License
This project is licensed under the MIT License.