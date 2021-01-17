import datetime
import urllib
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# 検索用URL。検索パラメータ部分は{}
URL_MERCARI = 'https://www.mercari.com/jp/search/?sort_order=price_asc&keyword={}&status_on_sale=1' # メルカリ
URL_RAKUMA = 'https://fril.jp/search/{}?order=asc&sort=sell_price&transaction=selling' # ラクマ

# 最安値の要素取得用セレクタ
SELECTOR_MERCARI = '.items-box-price' # メルカリ
SELECTOR_RAKUMA = '.item-box__item-price' # ラクマ

CAT_CHAR = ' ' # AND検索キーワード連結用文字
NOT_CHAR = '-' # NOT検索キーワードの冒頭に付与する文字。ラクマは未対応
DATA_FILE = 'data.csv' # CSVファイル

# 検索キーワード
keywords_all = [
    {
        'and': ['Ibanez', 'TS-9'],
        'not': ['TS9DX', '808', 'TS5']
    },
    {
        'and': ['Ibanez', 'RG350'],
        'not': ['ジャンク']
    },
    {
        'and': ['BOSS', 'GT-1', 'エフェクター'],
        'not': ['GT-10', 'GT-100', 'GT-1000', 'GT-1B', 'ACアダプタ', '教科書']
    },
]

def get_min_price(browser, base_url, query_params, selector):
    """指定したキーワードの商品の最安値を取得
    :param browser: ブラウザ
    :param base_url: 検索用URL
    :param query_params: 連結したキーワード
    :param selector: 価格の要素のセレクタ
    :return: 最安値の文字列
    """
    # 取得した価格内の余計な文字削除用辞書
    dic = str.maketrans({
        '\': '',
        '￥': '',
        ',': '',
        ' ': '',
    })

    # キーワードをエンコードし、URLに埋め込んでアクセス
    url = base_url.format(urllib.parse.quote(query_params))

    try:
        # 最安値の要素を取得して返す
        browser.get(url)
        elm_min = browser.find_element_by_css_selector(selector)
    except NoSuchElementException as e:
        print(f'指定した要素が見つかりませんでした:{e.args}')
    except TimeoutException as e:
        print(f'読み込みがタイムアウトしました:{e.args}')

    return(elm_min.text.translate(dic)) # 余計な文字を削除してから返す

# ブラウザ準備
browser = webdriver.Chrome('chromedriver.exe')
browser.set_page_load_timeout(30) # 読み込みタイムアウト設定

# CSV保存用リストを用意
record = []

# 実行時の日付を取得・文字列化して保存用リストに追加
record.append(datetime.date.today().strftime('%Y/%m/%d'))

# 商品ごとに最安値を取得
for keywords in keywords_all:
    # 商品ごとの検索キーワードを連結
    query_params_and = CAT_CHAR.join(keywords['and']) # AND用
    query_params_not = CAT_CHAR.join([NOT_CHAR + kw for kw in keywords['not']]) # NOT用

    # メルカリの最安値を取得し、保存用リストに追加。
    query_params_mercari = query_params_and + CAT_CHAR + query_params_not
    min_price = get_min_price(browser, URL_MERCARI, query_params_mercari, SELECTOR_MERCARI)
    record.append(min_price)

    # ラクマの最安値を取得し、保存用リストに追加
    query_params_rakuma = query_params_and # ANDのみ
    min_price = get_min_price(browser, URL_RAKUMA, query_params_rakuma, SELECTOR_RAKUMA)
    record.append(min_price)

browser.quit() # ブラウザ終了

# CSVに書き込み
try:
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(record)
except OSError as e:
    print(f'ファイル処理でエラー発生:{e.args}')
