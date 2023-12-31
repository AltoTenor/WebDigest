![Logo](../chandu2.png#gh-light-mode-only)
![Logo](../dk.png#gh-dark-mode-only)

# Table of contents
- [Built with](#built-with)
- [Installation](#installation)
- [Usage](#usage)
- [Useful resources](#useful-resources)
- [Authors](#authors)


## Built with
- Python
- Flask
- RESTful API

## Installation
- Clone the repository
```bash
    git clone https://github.com/AltoTenor/WebDigest.git
```
- Navigate to project directory
```bash
    cd ./WebDigest/backendFinalBuild_flask/
```
- Install requried dependancies
```bash
    pip install -r requirements.txt
```
- run code in localhost using 
```bash
    python app.py
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
- [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/) - Flask is a lightweight python framework for developing quick and scalable backend services and RESTful APIs
- [Flask RESTful Docs](https://flask-restful.readthedocs.io/en/latest/) - Flask_RESTful is a library that makes developing REST APIs easier using Flask

## Authors
- Diljith P D - [Portfolio](https://th3bossc.github.io/Portfolio)
- Aritro Ghosh - [github](https://github.com/AltoTenor)
- Arshiya Hafis - [github](https://github.com/ArshiyaHafis)
- Chandrakant V B - [github](https://github.com/CVB003)