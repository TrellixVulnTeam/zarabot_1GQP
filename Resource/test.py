import pprint
from flask import Flask , request

## from{ name of your file } import search
from wolf import search_wiki

app = Flask(__name__)

access_token ="cEOJvRa3nKHWbGOMfrKsmskR9z4TWk2AWn3zK06a14wzeR1UJbw3ihyGlgOiCgjItX1CIbeBW++vmE6ZEvSwYEZJdyHxjnTXJmblv0ttRwZl9yranqTBdMv25mmjInbtA66jKd5GsS2adhGDrNLvlwdB04t89/1O/w1cDnyilFU="

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':

        pp = pprint.PrettyPrinter(indent=3)
        ### dictionary from line
        data = request.json
        data_show = pp.pprint(data) #เอา JSON  มาดู โครงสร้าง

        ## extract text from line
        text_fromline = data['events'][0]['message']['text']
        ## ค้นหาคำจาก wikipedia
        result = search_wiki(text_fromline)

        ### import function ในการส่งmessage reply.py
        from reply import ReplyMessage

        ReplyMessage(Reply_token=data['events'][0]['replyToken'],
        TextMessage=result,
        Line_Accees_Token= access_token
        )


        return 'OK'

    elif request.method == 'GET':
        return 'นี้คือลิงค์เว็บสำหรับรับ package'

if __name__ == "__main__":
    app.run(port=200)
