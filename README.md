# speee technology challenge

# 概要
指定したn番目のフィボナッチ数を返すREST APIを実装したものである。
エンドポイントは以下のようになっている。
```
- /fib
  課題の要件を満たすエンドポイント
- /docs
  Swaggerドキュメント
```

# 構成
```
- app/
  - middleware/
    - timeout.py
  - tests/
    - utils.fibonacci.py
  - utils/
    - fibonacci.py
  - main.py 
```

`app/`はメインのディレクトリであり、以下のような構成となっている。

- `middleware/`: ミドルウェア関連のソースコードを格納するディレクトリ
- `tests/`: テストコードを格納するディレクトリ
- `utils/`: ユーティリティを格納するディレクトリ
- `main.py`: Webアプリケーションの実行可能なコード

