import uvicorn as uvicorn
from correction import ErrorCorrect
from differ import diff
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from predict import *
from pydantic import BaseModel
from transformers import BartForConditionalGeneration, BertTokenizer


class Item(BaseModel):
    content: str


app = FastAPI()
# 配置允许域名
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
# 配置允许域名列表、允许方法、请求头、cookie等
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
ec = ErrorCorrect()


@app.get("/")
async def root():
    return {
        "a": 1,
        "b": 2
    }


@app.post("/correct")
async def create_item(item: Item):
    print(item)
    content = item.content
    content_corrected = ec.correct(content)
    with open(r"test.txt", "w", encoding="utf-8") as f:
        f.write(content_corrected)
    predict()
    with open(r'res.txt', 'r') as f:
        content_corrected_2 = f.read()
    content_corrected_2 = content_corrected_2.replace(" ", "")
    print(content_corrected_2)

    differs = diff(content, content_corrected_2)
    print(differs)
    ret = {
        "old_content": content,
        "new_content": content_corrected_2,
        "edit_list": differs
    }
    print(ret)
    return ret


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5555, reload=True)
