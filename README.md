# Project README

## Overview
This Python project is designed to automate the process of generating structured content for digital publications. Leveraging a keyword-driven approach, the script generates comprehensive articles complete with SEO data and images. The methodology involves creating an article structure based on a given keyword, building an overview, a table of contents, and an introduction, followed by the automatic generation of SEO data and sourcing images from Pexels or Dalle 3.

## Getting Started

### Prerequisites
Before you begin, ensure you have Python installed on your system. This project requires Python 3.x.

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

### Running the Script
- Execute the main script by running `main.py` from your command line:
  ```bash
  python main.py
  ```

## Features
- **Keyword-Driven Content Generation:** The script uses a specified keyword from the `.env` file to generate a methodical and structured article.
- **Section Building:** Each section of the article is constructed based on the generated data, including an overview, table of contents, and introduction.
- **Screenshoting homepage:** If there is a valid link it will screenshot the link given.
- **SEO Optimization:** Automatically generates SEO data for the article.
- **Image Sourcing:** Sources images from Pexels. If a suitable image is not found, it uses Dalle 3 to generate one.

## Upcoming Features (TODO)
- **Randomized Author IDs:** This feature will add variability in the authorship of the articles.
- **Category Selection:** Users will be able to choose categories under which their articles will be classified.
- **Tagging System:** Implementation of a tagging system to enhance article discoverability and relevance.
- **More controls:** I will add more controls for using with products rather than ranking items.


## License
This project is open-source and available under the MIT License.
