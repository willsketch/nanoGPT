from fastapi import FastAPI, UploadFile, File, Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# allow communication from all frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {"message": "Hello World"}


@app.post("/uploadfile/")
def upload_video(file: UploadFile):
    return Response(content=file.filename)
