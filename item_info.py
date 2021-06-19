import requests
import urllib
from pprint import pprint

from common import execute_api

# 定数は上部で定義する
RAKUTEN_PRODUCT_URL = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
APP_ID = "1019079537947262807"


# タスク３
def item_info(keyword: str):
    '''
    指定したキーワードでAPIを実行して
    商品情報のうち、最高価格と最低価格を取得する
    '''
    # キーワード入力、リクエストパラメーター作成
    params = {
        "keyword": keyword,
        "format": "json",
        "applicationId":APP_ID  
    }
    
    # APIを実行
    res = execute_api(url=RAKUTEN_PRODUCT_URL, params=params)
    
    #　結果を表示
    for obj in res["Products"]:
        print(f'product_name: {obj["Product"]["productName"]} / max_price: {obj["Product"]["maxPrice"]} / min_price: {obj["Product"]["minPrice"]}')

    return res
    
if __name__ == "__main__":
    keyword = input("検索キーワードを入力してください >>> ")
    item_info(keyword)

# # 1
# VSCODEにREST Clientプラグインをインストールして楽天の商品APIを実行して結果が返ってくることを確認してみましょう。  
# REST Clientの使い方:https://protoout.studio/posts/visual-studio-code-api-rest-client
# 商品検索APIの仕様:https://webservice.rakuten.co.jp/api/ichibaitemsearch/

# # 2
# 以下の仕様を参考にして、任意のキーワードでAPIを検索した時の
# 商品名と価格の一覧を取得してみましょう
# https://webservice.rakuten.co.jp/api/ichibaitemsearch/

# # 3 
# 以下のAPIを使って、任意の商品の最安値と最高値を取得してみましょう  
# https://webservice.rakuten.co.jp/api/productsearch/

# # 4
# 以下のAPIを使って、任意のジャンルのランキング一覧を取得し、CSV出力してみましょう
# https://webservice.rakuten.co.jp/api/ichibaitemranking/

# # 5
# pytestをinstallして、単体テストを実施してみましょう<BR>
# - インストール<BR>
# `pip install pytest`<BR>
# - テスト実行<BR>
# `python -m pytest <pyファイルのpath>::<テストしたい関数名> -s`  <BR>
