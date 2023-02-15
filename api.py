from fastapi import FastAPI, UploadFile, File, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse, StreamingResponse


app = FastAPI()
# allow communication from all frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#TODO this shoud take in a variable 'CAT' of 'FTT'
# and return questions generated from sample.py
async def question_streamer():
    n = 10
    while n > 0:
        n -= 1
        yield (str(n) + "\n")

#TODO should be able to generate all subject questions from
# one function otherwise multiple functions
@app.get('/', response_class=PlainTextResponse)
def root():
    return StreamingResponse(question_streamer())
