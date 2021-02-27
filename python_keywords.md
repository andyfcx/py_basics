# Python 關鍵字

## 輸入輸出
- import, from, as

        import requests
        from lxml import etree
        import pandas as pd

## 真偽
- True, False

## 邏輯判斷
- is, not
- and, or, in
- any, all

## 流程控制
- if, elif, else
- for, while
- pass, break, continue

## 錯誤處理
- try, except, finally, raise

        try:
            # do something
        except KeyError:
            # 處理錯誤
        finally:
            # 其他一定要做的事
            print("XXXX")

## 定義
- def, class

        def my_function(x):
            return x ** 2

        class MyClass():
            def __init__(self):
                pass

- return, yield

## 其他重要的關鍵字
- global 定義一個全域變數
- lambda 定義一個沒有名字的函數
- with 上下文資源控制
        
        with open('myfile.txt') as f:
            text = f.read()
        print(text)
- del 把物件從記憶體中刪除
- id 取得物件的記憶體位置
- assert 測試或者除錯用的斷定
- None 空值