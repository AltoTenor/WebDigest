from rest_framework.response import Response
from rest_framework.decorators import api_view

from bs4 import BeautifulSoup
import requests

def getText(url : str):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content 
    else:
        print(f"[INFO] couldn't access website data, try again")
        return
    soup = BeautifulSoup(html_content, 'html.parser')

    text_elements = soup.find_all(['p'])
    scraped_text = ' '.join(element.get_text() for element in text_elements)
        
    if len(scraped_text) > 20000:
        print(f"[ERROR] page too large to perform qna")
        return
    
    return scraped_text 


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM 

model = AutoModelForSeq2SeqLM.from_pretrained('google/flan-t5-large')
tokenizer = AutoTokenizer.from_pretrained('google/flan-t5-large')

def getAnswer(question : str, url : str):
    context = getText(url)


    inputs = tokenizer(f"context : {context}, question : {question}", return_tensors = 'pt').input_ids

    outputs = model.generate(
        inputs, 
        min_length = 10,
        max_new_tokens = 600,
        length_penalty = 1,
        num_beams = 3,
        no_repeat_ngram_size = 3,
        temperature = 0.7,
        top_k = 110,
        top_p = 0.8,
        repetition_penalty = 2.1
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens = True)

    return answer




@api_view(['POST'])
def findAnswer(request): # {url : website, question : question}
    answer = getAnswer(request.data['question'], request.data['url'])
    return Response({'question' : request.data['question'], 'answer' : answer})
    