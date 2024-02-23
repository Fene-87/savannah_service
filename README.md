# savannah_service
Technical challenge for Savannah Informatics

# 📗 Table of Contents
  - [🛠 Built With ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
    - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Author ](#-author-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

# 📖 Project Description <a name="about-project"></a>

This is a Django project that is meant to work similarly to a shopping cart. A user can be authenticated using his/her social account. Once authenticated, the user can view available items and make orders. When an order is created, the user gets an SMS. This has been made possible using the Africa's Talking SMS gateway.


## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

  <ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
  </ul>
  <ul>
    <li><a href="https://postresql.org/">PostgreSQL</a></li>
  </ul>

### Key Features <a name="key-features"></a>

- **OAuth2**
- **Customer and Order models**
- **Create orders**
- Africa's Talking SMS gateway

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python312
- IDE eg Pycharm or VS Code
- PostgreSQL

### SetUp

Clone this Repository to your desired folder:

``` sh
cd my-folder
git clone https://github.com/Fene-87/savannah_service.git
```
### Install 
Install this project with:
 
``` sh
pip install -r requirements. txt
```

### Usage
To run the project, execute the following commands:
``` sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
There is an existing migration to prepopulate the items table.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 👥 Author <a name="author"></a>
👤 **Mark Fenekayas**

- GitHub: [@Fene-87](https://github.com/Fene-87)
- LinkedIn: [@Mark Fenekayas](https://www.linkedin.com/in/mark-fenekayas/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🔭 Future Features <a name="future-features"></a>

- [Implement authentication using OIDC]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ⭐️ Show your support <a name="support"></a>

If you like this project consider giving it a star ⭐️.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank Savannah Informatics for this platform to showcase my skills as well as continuous learning.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


