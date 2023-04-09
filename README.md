# Introduction of Title-to-URL Generator

[![Visit GitHub Page](https://img.shields.io/badge/Visit-GitHub%20Page-blue?logo=github)](https://yin-renlong.github.io/Title-to-URL/)

![Jekyll Build](https://github.com/YIN-Renlong/Title-to-URL/actions/workflows/jekyll-gh-pages.yml/badge.svg)


"Title to URL" is a web-based tool that helps users generate SEO-friendly URLs for their articles based on the title and date, designed with clean HTML, CSS, and JavaScript to create an easy-to-use user interface. The tool allows users to input the article title and select the month and day, and generates a normalized URL that follows the practices for URL structure and readability in popular CMS platforms (such as WordPress). The app allows users to input their domain address, article title, and choose between two options to generate a URL in a specific format. 

---

{% include title-to-url.html %}

---

The two options are:

1. Using Date method (year, month, and day)
2. Using Subdirectory method


## Usage

To use the URL Generator, simply input your domain address, article title, and select the preferred URL format option. Then, click the "Generate URL" button to display the generated URL on the page.

## Features

- Responsive design
- Clean and intuitive user interface
- Two URL format options: date or subdirectory
- Form validation and error handling

## Example of Output

An example of a generated URL using the "Use Date" option:

```
https://www.example.com/2023/04/08/my-article-title/
```

An example of a generated URL using the "Use Subdirectory" option:

```
https://www.example.com/blog/my-article-title/
```

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

## Credit

This app was created by by [[YIN Renlong](https://github.com/YIN-Renlong)]. - Feel free to use and modify this code for your projects, but please give credit to the original author.

