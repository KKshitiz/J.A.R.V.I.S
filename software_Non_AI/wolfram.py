from wolframalpha import Client 
#pip install wolframalpha


def setupWolfram():
    app_id='RWAGV2-6QGHW7Y95J'
    global client
    client=Client(app_id)

def startWolfram(question):
    try:
        res=client.query(question)
        res=next(res.results).text
        print(res)
        return res
    except:
        print("Not found on Wolfram alpha")
        return None

if __name__ == "__main__":
    setupWolfram()
    startWolfram("What is 2+3/4")