from flask import request, render_template, Blueprint
import sys, logging
from concepts import list_of_terms,question_types
from gpt_endpoints import consultant,textToAudio

logger = logging.getLogger(__name__)
stream_handler =  logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)
#SINGLE ROUTE OF THE APPLICATION
home=Blueprint('home',__name__)


@home.route('/',methods=["GET","POST"]) 
def index():
    options =list_of_terms
    logger.info(request.method)
    logger.info(request.form)
    if request.method == 'POST':
        data= request.form #capture the information from the form
        input = data['input-text'] if data['question-type'] == 'text' else data['option']
        logger.info(input)
        logger.info(data)
        #textResponse =consultant(input)
        #textToAudio(textResponse)
        textResponse ="no response"
        return render_template("./index.html", questions=question_types,select=options, textResponse=textResponse)

    else:
        textResponse=""
        audioResponse=""
        return render_template("./index.html", questions=question_types,select=options, textResponse=textResponse, audioResponse=audioResponse)

        
    

