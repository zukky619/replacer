replacer
-----------------------------------------------------
ファイルやフォルダの置換スクリプト


## Overview

指定フォルダに置かれたファイルやフォルダをconfファイルの記載に基づき、コピーするスクリプトです。

RAMDISK動作の組み込み機器の開発フェーズおいて、ログ領域等の不揮発領域にファイルを置いておき、起動時に本スクリプトで置換を行うことで、設定変更を容易にします。

既存のファイルやディレクトリが存在する場合は、パーミッションや所有者情報もコピーします。


## Configuration File

設定ファイルとして、ソースとなる置換ファイル(またはフォルダ)とコピー先のパスをコロン区切りで記載します。

```
"path/of/src" : "path/to/copy"
```

## Run Script

下記コマンドにより本スクリプトを実行できます。

```
python3 file_replacer.py [-c CONF] [-s SOURCE_DIR]
```

SOURCE_DIRのデフォルトは、/var/log/replacementです。
CONFのデフォルトは、/var/log/relacement/replacer.logです。