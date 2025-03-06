# Create static website to display resume

## Purpose

This README provides step-by-step instructions on how to format and host a resume 
as a static website using [**Pelican**](https://getpelican.com/) and [**GitHub Pages**](https://pages.github.com/). It is intended for readers with 
minimal experience in static site generations and **Git** but who have basic knowledge of **Markdown**.The primary goal of this guide is to help you create a modern, professional 
online resume that is both easily maintainable and visually appealing.

***

## Prerequisites

Before proceeding, ensure you have the following installed on your computer:

#### Required Software:
- [VSCode](https://code.visualstudio.com/download) (Or any another text editors)
- [Python](https://www.python.org)
- [Git](https://git-scm.com)
- [A GitHub Account](https://github.com)
- [Pelican](#installation-commands) 
- [ghp-import](#installation-commands)

***

#### Installation Commands:

Run the following in your terminal to install **Pelican** and **ghp-import**:

```sh
python -m pip install "pelican[markdown]"
python -m pip install ghp-import
```

***

## Step-by-Step Instructions

This section provides a structured workflow for creating and deploying the resume website. 

### Step 1: Getting started
Make sure to follow instructions carefully for optimal setup.  
1. **Create a new directory for your project:**
- Open your terminal and create a new directory for your project. This directory will contain all the files for your static website. Run:
   ```sh
   mkdir example
   ```
2. **Make a new Pelican project:**
- Move into your project directory and use Pelican quickstart command to set up the basic structure of your website. Run:
   ```
   pelican-quickstart
   ```
3. **Answer the following questions:**
   - **Site title**: `Your answer`
   - **Author name**: `Your answer`
   - **URL prefix**: `https://username.github.io/nameOftheFolder`
   - **Use GitHub Pages?** Yes
   - **Timezone**: `Your answer`

### Step 2: Write your resume in Markdown


Markdown allows simple formatting and it really easy to use

1. **Create a new directory inside your project:**
Inside your project folder, create a subdirectory called content where you will store your files in Markdown format. In your terminal, run:
   ```sh
   cd example
   mkdir content
   ```
2. **Write your resume in Markdown and save it as (.md) file**    
<br>
3. **Include the following content at the top of the file**  
   ```
   Title: Resume for Peter Johnson
   Date: 2025-03-01
   Category: Resume
   ```
4. **Below this metadata, add your resume details formatted using Markdown syntax**
<br>
5. **Move (.md) file inside 'content' folder**
In your terminal run:
   ```sh
   mv resume.md content
   ```
 

### Step 3: Applying the desired Theme

1. **Download and install desired theme:**
To customize the look of your resume website, you can choose from a variety of 
Pelican themes. I personally chose theme `Flex` by Alexandre Vicenzi. To install it, run:
   ```sh
   git clone https://github.com/alexandrevicenzi/Flex.git themes/Flex
   ```
2. **Alternative way:**
If you prefer to have options, you can download the complete Pelican themes package by running:
   ```sh
   git clone https://github.com/getpelican/pelican-themes.git themes
   ```

3. **Locate the pelicanconf.py File inside your project folder**  
<br>
4. **Change the parameter 'THEME' inside the File to path of desired theme**
   ```sh
   THEME = "themes/Flex"
   ```

### Step 4: Generating and Testing the Site


1. **Generate the website:**
With your content and configuration in place, you can now generate your website. In the terminal, run:
   ```
   pelican content
   ```
2. **Run a local server to preview:**
To see how your site looks before deploying it online, run a local server:
   ```
   pelican --listen
   ```
3. **Copy the local host URL adress and put it inside your browser**

### Step 5: Deploying to GitHub Pages

1. **Initialize a new Git repository:**

   - On [Github](https://github.com/) press "Create New" -> "New repository"
   - Make Sure to make repositry **Public** if you want others to contribute
  <br>
2. **Clone the repository to your local machine**  
In your terminal, clone the GitHub repository into your project directory:
   ```sh
   git clone https://github.com/RepositoryName/example.git
   ```

3. **Generate the website and push to GitHub:**
   ```sh
   pelican content -s publishconf.py
   ghp-import output -b gh-pages
   git push origin gh-pages
   ```

4. **Check the live site:**  [https://userNameExample.github.io/NameOfTheFolder](https://userNameExample.github.io/NameOfTheFolder)

***

## Further Resources

1. **Pelican Documentation** - [https://docs.getpelican.com](https://docs.getpelican.com)
2. **Markdown Guide** - [https://www.markdownguide.org/](https://www.markdownguide.org/)
3. **GitHub Pages Guide** - [https://pages.github.com/](https://pages.github.com/)
4. **Flex Theme Github page** - [https://github.com/alexandrevicenzi/Flex](https://github.com/alexandrevicenzi/Flex)
5. **VSCode Documentation** - [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

***

## FAQ

**Q1: Why use Markdown instead of raw HTML?**\
A: Markdown is much simplier to read and write rather than HTML, which can make it more accessible for people with very little technical background.

**Q2: I updated my resume, but the changes don’t appear on the live site. Why?**\
A: Make sure that you **regenerate** the site like in [Step 4](#step-4-generating-and-testing-the-site) and **redeploy** to GitHub Pages like in [Step 5](#step-5-deploying-to-github-pages).

**Q3: I can't see my theme on the website that I've made. What should I do?**  
A: If you are viewing the site on localhost, check the pelicanconf.py file and ensure that you have set the **THEME** variable correctly (for example, `THEME = "themes/Flex"`). 
If you are hosting your site on GitHub Pages, verify that the **SITEURL** in publishconf.py variable is set properly to your GitHub Pages URL (for example, `SITEURL = "https://username.github.io/FolderName"`). If these configurations are not 
correctly set, Pelican will display default theme rather than displaying your chosen theme.



***

## Credits

- **Author:** Davud Habibullah
- **Static Site Generator:** Pelican
- **Theme:** Flex by Alexandre Vicenzi

***
## Contact

Davud Habibullah  - habibuld@myumanitoba.ca
Project Link: https://github.com/DavkaSnaixl/Assignment2





*** 

## Licence

The Unlicense

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


