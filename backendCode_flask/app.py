from qnabackend import create_app 


app = create_app()

@app.route('/')
def home():
    return "hello world"


# if __name__ == '__main__':
#     app.run(debug = True, port = 5000)

if __name__ == '__main__':
    app.run(debug = False, host = "0.0.0.0", port = 7860)
