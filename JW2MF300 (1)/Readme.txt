=====================================================================
【ソフト名】 『JwwToMF』Ver3.00
【登 録 名】 JW2MF300.ZIP
【作 者 名】 Nemoto
【対応機種】 OS:WindowsXP, Vista, 7
【開発言語】 WinXP + Delphi XE
【圧縮ﾌｧｲﾙ】 JwwToMF.exe / JwwToMF.hlp / Readme.txt
【作成方法】 解凍後、任意のフォルダーに保存して下さい。
【ＳＷ種別】 フリーウェア（寄付歓迎）
【転　　載】 転載禁止
=====================================================================

◆『JwwToMF』は、「Jw_cad or windows」で【範囲】選択した図形データを
　 メタファイル形式等でクリップボードに転送するツールで、EXCELやWordの
   アプリにJww図面の貼付(図面の伸縮が可能)が可能です。
   また、EMF,BMP,JPEG,PNG,GIF形式で画像データのファイル保存も出来ます
   加えて、表などの文字列を範囲コピーし、エディタやEXCELに貼付（テキ
   ストデータ）すると文字列データ別に行列毎、左詰にて貼付を行います。
   （EXCELの場合、セル毎に文字列が挿入します。）

---------------------------------------------------------------------

【 注 意 】
 ---------
　全てのJwwデータに対応しておりませんので、正確な描写を保証しません。
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

　◎対応が出来ないか、簡略したJwwデータ

　　(1) 正確な線種パターン。ランダム線一部対応。
　　(2) 正確な文字サイズ・間隔、等
　　(3) 文字列の均等割付、特殊文字指定、等
　　(4) ソリッド図の対応未了
　　(5) 他色々

---------------------------------------------------------------------

【 使用方法 】

　(1) 『Jw_cad for windows』で貼り付けしたい図面の一部、または全部を
  　　【範囲】で選択し、【コピー】コマンドでデータを保持します。
  　　或いは、Jwwデータをファイルより読み込みます（全データを対象）
  　　※ このデータはクリップボードに転送されます ※
  (2) 『JwwToMF』を起動して下さい。範囲選択した図形を表示します。
  (3) 『JwwToMF』の[ファイル]＞[クリップボードにコピー]でクリップ
　　　ボードにコピーします。
　　　EXCELやWord等のアプリに【貼り付け※2】してご利用下さい｡

  　　a) [ファイル]＞[画像データで保存]で「WMF,EMF,BMP,JPEG,PNG,GIF」
　　　　　形式のファイル保存をします。
  　　b) 貼り付け時、縦横比が合わない場合があります。
　　　　　アプリ側で修正して下さい。
  (4) Jw_winで新たに【範囲】選択しコピーした場合は、[再描画]で新たな
　　　図形を描画します。


　※1 多量のデータの場合、描画に時間が掛かります。
  ※2 メタファイル図、ビットマップ図等を貼り付ける場合は、
      【形式を選択して貼り付け】にて貼付を行ってください。
　　　<<通常の【貼り付け】の時、テキストデータのみの場合が有り>>

---------------------------------------------------------------------

◆サポート
　サポートは、基本的に行っていませんが、TriPod公開ホームページの
　掲示板で質問、あるいはメール等の問い合わせに出来る範囲でお答え
　します。（「Jw_win 関連ツール・サポート掲示板」にて）

　　※ http://www.e-tripod.net/
　　※ E-mail:nemoto@survey.office.ne.jp


----------------------------------------------------------------------
2011/01/21　：　Ver3.00
   1) Jww7.00データバージョンに対応した。
   2) 開発言語を、Delphi XEに変更した。（※UNICODE文字関連で、表示に
      不具合が発生する可能性があります。）
   3) 画像ファイル作成のサイズを、解像度(dpi)指定に変更した。
   3) 全般的な修正作業。

----------------------------
2007/11/24　：　Ver3.00β1
   1) Jww6.00データバージョンに暫定対応した。
   2) マウス操作による画面表示の拡大縮小操作に対応した。（表示のみ）
   3) 全般的な修正作業。

----------------------------
2007/06/02　：　Ver2.60a
   1) 出力画像サイズが、表示画面サイズに固定され出力されていた不具合を
      修正した。

----------------------------
2007/06/01　：　Ver2.60
   1) Ver4.20で変更のあった寸法図形の仕様拡張を考慮する対応をした。
   2) 描画時の余白の不具合に対応した。
   3) メタファイルの描画（等倍）を見直しをした。
   4) 全般的な修正作業。

----------------------------
2006/02/07　：　Ver2.50
   1) Ver4.10で追加された埋込み文字[%m1,%m2,%SS,%ss,%SP,%sp]に対応
   2) データバージョン4.20に対応した
   3) 全般的な修正作業。

----------------------------
2005/02/11　：　Ver2.40
   1) クリップボードにメタファイル画像がある場合、これをBitMap画像にし、
      ファイル保存をする機能を追加した。
   2) 全般的な修正作業。

----------------------------
2005/01/27　：　Ver2.38a
   1) 使用Jw_cadがVer4.04(4.05)未満の場合、起動時や図形描画時にエラー
      表示をする不具合を調整した。

----------------------------
2005/01/25　：　Ver2.38
   1) 画像データ描画の相対パス記述に対応した。
   2) 縦字表示の[ー,（,）,［,］,『,』]等を正しく描画するよう調整した。
   3) Ver4.04-4.05で追加された制御文字[^%,^\,^&,%mm]に概ね対応した。
   4) Ver4.04-4.05の文字輪郭／文字列範囲の背景色描画に対応した。
   5) 全般的な修正作業。

----------------------------
2004/06/21　：　Ver2.37
   1) 画像出力モードに「GIF」形式を追加した。
   2) 全般的な修正作業。

----------------------------
2004/05/27　：　Ver2.36
   1) 不正なJwwデータの読み込みを調整した。
   2) 半角縦字が正しく描画出来ていなかったものを調整した。
   3) 補助線を表示しないオプションを新たに設けた。
   4) PNG画像出力の背景の透明化のオプションを新たに設定した。
   5) 全般的な修正作業。

----------------------------
2004/05/06　：　Ver2.35
   1) 図形データ読み書きを廃止した。
   2) 不正なJwwデータの読み込みを調整した。
   3) Jwwデータをクリップボード経由でJw_winにコピーをするように改良
   4) 点データのコード番号図形の一部が描画されていなかったものを表示
      出来るよう改良した。
   5) 特殊文字が正しく描画出来ていなかったものを調整改良した。
   6) 白黒BMPデータを２色データ形式に変更した。
   7) 全般的な修正作業。

----------------------------
2003/12/22　：　Ver2.34
   1) ファイル読みしたJwwデータの情報（Jwwデータバージョン、用紙サイズ
      メモ欄）を表示するメニューを追加した。
　　　これにより、メモ欄等の変更を可能とし、Jwwデータ保存時に設定値が
      有効となる。
   2) Jwwデータ保存が正しく出来ていなかった不具合を修正した。
   3) 全般的な修正作業。

----------------------------
2003/12/14　：　Ver2.33
   1) オプション「線幅を[1]に固定」チェック時の、メタファイル図描画を
      改良修正した。
   2) 全般的な修正作業。

----------------------------
2003/11/04　：　Ver2.32.1
   1) 「クリップボード監視設定」にチェックを入れても、描画やクリップ
      ボードにデータ転送が出来ていなかった不具合を修正した。

----------------------------
2003/11/04　：　Ver2.32
   1) Jw_win Ver3.51（Jwwデータバージョン Ver3.51）への対応版。

----------------------------
2003/06/20　：　Ver2.31
   1) JwwデータのVer2.00以前のものも表示できるように改良した。
   2) 画像の挿入されたJwwデータの場合、エラーとなる不具合を修正した。
   3) 全般的な修正作業。

----------------------------
2003/06/09　：　Ver2.30.2
   1) 文字列の描画に置いて、表示されない場合の有った不具合を修正した。

----------------------------
2003/06/08　：　Ver2.30.1
   1) メタファイル化時の背景色の透過関連を調整した。

----------------------------
2003/06/05　：　Ver2.30
   1) JwwデータRead/Write/Toolユニットを全面的に改良した。
   2) 取込図形データの図形表示範囲の改良をした。
   3) 未対応だった点データ(Ver3.00)のコード番号図形を表示出来るよう
      改良した。
   4) 全般的な修正作業。

----------------------------
2003/05/02　：　Ver2.26
   1) 全般的な修正作業のみ。

----------------------------
2003/03/30　：　Ver2.25
   1) 文字列データの貼付時、文字列データが正しい列位置にならない場合も
      あった不具合を修正した。
   2) 「画像・ソリッドを最初に描画」にチェックを入れても、先に線や円弧
      等のデータ描写となっていた不具合を修正した。
   3) 傾きのある円弧データの描画方法を一部改良した。
   4) 全般的な修正作業。

----------------------------
2003/01/21　：　Ver2.24
   1) 文字データを、クリップボードにテキストデータとして保存する機能を
      オプション設定にてon/off出来るよう改良した。
   2) 不正なJwwDataFileをテストロードする機能を仮追加した。
      （正常に作動するかは不明）
   3) 全般的な修正作業。

----------------------------
2003/01/20　：　Ver2.23.1
   1) Jw_winで範囲コピーした図形が表示されない不具合を修正した。

----------------------------
2003/01/19　：　Ver2.23
   1) 文字データを、クリップボードにテキストデータとして保存する機能を
      追加をした。
   2) オプション設定において、設定した「線色」をソリッド図にも有効とす
      る設定を設けた。
   3) 全般的な修正作業。

----------------------------
2003/01/02　：　Ver2.22
   1) Jw_win Ver3.00 への対応版(点データのコード番号図形は非表示）。

----------------------------
2002/12/03　：　Ver2.21
   1) オプション設定が記録されていない不具合を修正した。
   2) 全般的な修正作業。

----------------------------
2002/11/16　：　Ver2.20
   1) 文字の高さ／幅が逆になっていた不具合を修正した。
   2) 文字の均等縮小が正しく描画出来ていない不具合を修正した。
   3) ランダム線に一部対応した。
   4) 全般的な修正作業。

----------------------------
2002/10/17　：　Ver2.10.0
   1) 開発言語のDelphi6をDelphi7に移行し、コンパイルした。
   2) 文字フォントが正しく描画されていなかった不具合を修正した。
   3) ソリッド図形全般で、意味不明な線やべた塗り等する場合が有った
      不具合を修正した。
   4) ソリッド図形の円環ソリッドと円外ソリッド（不完全）に対応した。
   5) オプション設定を保存（INIファイル）するようにした。
   6) 全般的な修正をした。

----------------------------
2002/08/20　：　Ver2.04.0
   1) Jwwデータをファイル読込時に「読み取り専用JWWファイル」の場合、
      エラーとなる不具合を修正した。
   2) ランダム線／倍長線種が描画されていなかった不具合を修正した。
      但し、ランダム線の対応はしていないため、直線での表示。
   3) 全般的な修正をした。

----------------------------
2002/06/27　：　Ver2.03.0
   1) 拙作：Susie 32bit Plug-in [ifjww.spi]を利用し、図形をプレビュー
      選択可能とした。
   2) 全般的な修正をした。

----------------------------
2002/06/22　：　Ver2.02.1
   1) クリップボードへの転送並びに、画像データ保存時、縦長の図形が
      正しく出力していなかった不具合を修正した。
   2) 全般的な修正をした。

----------------------------
2002/06/21　：　Ver2.02.0
   1) 「出力画像サイズ」の設定値が結果に正しく反映していなかった
      不具合を修正した。
   2) クリップボードへ転送するデータに画像データ(BMP)を加えた。
   3) 文読画像データの表示／非表示をする設定を新設した。
   4) 全般的な修正をした。

----------------------------
2002/06/20　：　Ver2.01.0
   1) Windows98系に於いて、メニューより「画像・ｿﾘｯﾄﾞ図先行描画」を
      チェックした場合、JwwToMFが反応しなくなる不具合を修正した。
   2) オプション設定のソリッドハッチングパターンを、線色別等に指定
      出来るように改良した。
   3) 全般的な修正をした。

----------------------------
2002/06/20　：　Ver2.00.0
  1) クリップボードを監視し、Jwwデータがクリップボードに書き込まれた
     時、即座にメタファイル化を行う設定を新設した。
  2) [画像データで保存]にPNG形式を追加した。
  3) オプション設定にソリッド図形の塗り潰しパターンの選択を新設。
     （お遊びモードです。）
  4) 全般的な修正をした。

----------------------------
2002/06/14　：　Ver1.99β2.0
  1) 正しく円弧が描けなかった不具合を修正した。
  2) 文字描画時、特殊文字に一部対応した。
  3) 画像描画にテスト対応した。
  4) 全般的な修正をした。

----------------------------
2002/06/09　：　Ver1.99β1.1
  1) 「QTINTF.DLL」の関係する不具合を修正した。
  2) 全般的な修正をした。

----------------------------
2002/06/07　：　Ver1.99β1
  1) 初公開です。

