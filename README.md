# Create static website to display resume

## Purpose

This README provides step-by-step instructions on how to format and host a resume as a static website using [**Pelican**](https://getpelican.com/) and [**GitHub Pages**](https://pages.github.com/). It is intended for readers with minimal experience in static site generations and **Git** but who have basic knowledge of **Markdown**.

***

## Prerequisites

Before proceeding, ensure you have the following installed on your computer:

#### Required Software:

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
1. **Create a new directory for your project:**
   ```sh
   mkdir example
   ```
2. **Make a new Pelican project:**
   ```sh
   pelican-quickstart
   ```
3. **Answer the following questions:**
   - **Site title**: My Resume Website
   - **Author name**: Peter Johnson
   - **URL prefix**: `https://username.github.io/resume`
   - **Use GitHub Pages?** Yes
   - **Timezone**: `America/Winnipeg`

### Step 2: Write your resume in Markdown


Markdown allows simple formatting and it really easy to use

1. **Create a new directory inside your project:**
   ```sh
   cd example
   mkdir content
   ```
2. **Write your resume in Markdown and save it as (.md) file**    
<br>
3. **Include the following content at the top of the file**  
   ```sh
   Title: Resume for Peter Johnson
   Date: 2025-03-01
   Category: Resume
   ```
4. **Then add your desired content**
<br>
5. **Move (.md) file inside 'content' folder**

### Step 3: Applying the desired Theme

1. **Download and install desired theme:**
   ```sh
   git clone https://github.com/alexandrevicenzi/Flex.git themes/Flex
   ```
2. **Alternative way:**
   ```sh
   Install complete Pelican default theme package:

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
   ```sh
   pelican content
   ```
2. **Run a local server to preview:**
   ```sh
   pelican --listen
   ```
3. **Copy the local host adress and put it inside your browser**

### Step 5: Deploying to GitHub Pages

1. **Initialize a new Git repository:**
   - On [Github](https://github.com/) press "Create New" -> "New repository"
   - Make Sure to make repositry **Public** if you want others to contribute
  <br>
2. **Clone the repository to your local machine**  
   ```sh
   git clone https://github.com/RepositoryName/example.git
   ```

3. **Push to GitHub:**
   ```sh
   pelican content -s publishconf.py
   ghp-import output -b gh-pages
   git push origin gh-pages
   ```

4. **Check the live site:**  [https://userNameExample.github.io/example](https://userNameExample.github.io/example)

***

## Further Resources

1. **Pelican Documentation** - [https://docs.getpelican.com](https://docs.getpelican.com)
2. **Markdown Guide** - [https://www.markdownguide.org/](https://www.markdownguide.org/)
3. **GitHub Pages Guide** - [https://pages.github.com/](https://pages.github.com/)
4. **Flex Theme Github page** - [https://github.com/alexandrevicenzi/Flex](https://github.com/alexandrevicenzi/Flex)

***

## FAQ

**Q1: Why use Markdown instead of raw HTML?**\
A: Markdown is much simplier to read and write rather than HTML, which can make it more accessible for people with very little technical background.

**Q2: I updated my resume, but the changes don’t appear on the live site. Why?**\
A: Make sure that you **regenerate** the site like in [Step 4](#step-4-generating-and-testing-the-site) and **redeploy** to GitHub Pages like in [Step 5](#step-5-deploying-to-github-pages).

***

## Credits

- **Author:** Davud Habibullah
- **Static Site Generator:** Pelican
- **Theme:** Flex by Alexandre Vicenzi


