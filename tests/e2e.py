from xml.dom.minidom import parseString
import requests as req
# test_scores_service - it’s purpose is to test our web service. It will get the application 
# URL as an input, open a browser to that URL, select the score element in our web page, 
# check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.

# main_function to call our tests function. The main function will return -1 as an OS exit 
# code if the tests failed and 0 if they passed.
def test_scores_service():
    # Requesting for the website
    try:
        resp = req.get('http://127.0.0.1:8777')
    except req.exceptions.RequestException as e:  # This is the correct syntax
        return False
#    print(resp.content)
    doc = parseString(resp.content)
    elements = doc.getElementsByTagName('div')
    for element in elements:
        if element.hasAttribute('id') and element.getAttribute('id') == 'score':
            if element.childNodes[0].data.isdigit() and 1<= int(element.childNodes[0].data) <= 1000:
                return True
    return False

def main_function():
    ret = -1
    if test_scores_service():
        print("ok")
        ret = 0
    else:
        print("nok")
    return ret

main_function()