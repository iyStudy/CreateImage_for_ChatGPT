import openai
import requests
from PIL import Image
from io import BytesIO

openai.organization = "<Organization IDをここに入力>"
openai.api_key      = "<APIシークレットキーをここに入力>"

# 画像生成
def create_image_from_text(text):

    # 応答設定
    response = openai.Image.create(
                  prompt=text,              # 画像生成に用いる説明文章
                  n=1,                      # 何枚の画像を生成するか
                  size='512x512',           # 画像サイズ
                  response_format="url"     # API応答のフォーマット
                )

    # API応答から画像URLを指定
    image_url = response['data'][0]['url']
    
    # 画像をローカルに保存
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))
    image.save("output-image.png", "PNG")
        
    return image_url

if __name__ == "__main__":
    # 生成するイメージを文章で定義
    text = "電車に乗る猫"


    img = create_image_from_text(text)
