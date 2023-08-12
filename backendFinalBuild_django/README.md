![Logo](../chandu2.png)

# Table of contents
- [Built with](#built-with)
- [Installation](#installation)
- [Usage](#usage)
- [Useful resources](#useful-resources)
- [Authors](#authors)


## Built with
- Python
- Django
- RESTful API

## Installation
- Clone the repository
```bash
    git clone https://github.com/AltoTenor/WebDigest.git
```
- Navigate to project directory
```bash
    cd ./WebDigest/backendFinalBuild_django/drf/
```
- Install requried dependancies
```bash
    pip install -r requirements.txt
```
- run code in localhost using 
```bash
    python manage.py runserver 
```

## Usage 
- python
```python
    import requests
    postData = {'question' : "<your question here>", 'url' : "<target website url>"}
    apiData = requests.post('http://localhost:8000/question', json = postData)
    answer = apiData['answer']
```
- curl
```bash
    curl -X POST -H "Content-Type: application/json" -d '{
    "question": "<your question here>",
    "url": "<target website url>"
    }' http://localhost:8000/question

```

- javascript
```javascript
    let answer;
    const getAnswer = async () => {
        const postData = {question : "<your question here>", url : "<target website url>"};
        const apiData = await fetch('http://localhost:8000/question', { method : 'POST', body : JSON.stringify(postData)});
        
        answer = apiData.json()['answer']
    }

    getAnswer();
```


### Useful resources
- [Django Documentation](https://docs.djangoproject.com/en/4.2/) - Django is a batteries-included python framework for developing backend services and RESTful APIs and is famous for it's built in support for a lot of features

## Authors
- Diljith P D - [Portfolio](https://th3bossc.github.io/Portfolio)
- Aritro Ghosh - [github](https://github.com/AltoTenor)
- Arshiya Hafis - [github](https://github.com/ArshiyaHafis)
- Chandrakant V B - [github](https://github.com/CVB003)