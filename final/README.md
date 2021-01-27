# Final CTF Writeup

# Reverse
## Ransomware
1. 觀察 `wannaSleep.exe` 的行為
    - 取得同目錄下的所有檔案，並將其加密
    - 在目錄下寫檔案 `ransomeware.jpg`
2. 加密檔案方式
    - 利用檔案大小、部分檔案中的內容計算出 `idx`
    - `VirtualAlloc` 一塊將<u>檔案大小 pad 至 `0x000` 結尾</u>的空間
        - 將檔案的內容讀至此 buffer 中，剩餘部分則維持 `0x00`
    - 從 memory 中 `byte_402020(key)` 的第 `idx % 16384` 個開始和檔案的內容 **XOR**
    - 將加密過後的檔案覆蓋掉原本的檔案
3. 還原檔案
    1. 推測 `idx` 的值  
        原始檔案 pad 完最後殘留 `0x00`，且 `0x00` 與任何值 **XOR**，都會保留其原始的值  
        => 藉由比較檔案最後的值和 `key` 即可知該部分的原始檔案和哪一部分的 `key` **XOR**，便可以推測出加密檔案時的 `idx` 為何  
    2. **XOR** 檔案
        由於 `idx` 已知，且因 <!-- $pt\ \oplus\ key=\ ct\rightarrow ct\ \oplus\ key=pt$ --> <img style="transform: translateY(0.1em); background: white;" src="../svg/R3HY5I4k11.svg"> ，即可將加密過後的檔案解密
        ```python=
        # raw[:i + 1] => 將最後面的 padding 去掉
        result = bxor(raw[: i + 1], key[idx:] + key[:idx])
        ```
4. `readme.txt`
    ```shell=
    Sort them by size to get the right order, and there are 11*13 pieces of images. 
    PIL may save your life.
    ```
    可知需要將 143 個 jpg 檔組合出一張圖片才能知道最後的 flag
5. 組裝圖片
    將 143 個檔案每 11 個橫的組合出共 13 張長條形的圖，再將 13 張圖值得合併在一起，便可以得到很長的 flag

## DuRaRaRa
1. `VirtualAlloc` 一塊 `0x5A492` 的空間，將 memory 中的值複製到該區域中，並建立新的 process
2. 用 x32dbg 在 `VirtualAlloc` 下硬斷點，紀錄其回傳值（即為此空間的 `base address`），並在執行完 `memcpy` 後將整塊 memory dump 出來
3. 同時，在此 `base address` 的地方下 **Memory Execute** 的短點，`F9` 後便可以進入到創建的 process 中
4. 動態執行並比對 dumped memory `disassemble, decompile` 的結果
    > 主要行為在 0x2D28, `sub_2D28`,  的 functioin 中
5. function `sub_2D28`
    1. 用寫死的`ct, key` **XOR** 解密出目標檔案檔名 `C:\Users\terrynini38514\Desktop\flag.txt`
    2. `fopen("C:\\Users\\terrynini38514\\Desktop\\flag.txt", "r")` 將其開啟，失敗則直接結束
    3. 用 `ExpandEnvironmentStringsA`, `PathCombineA` 產生最後加密出來檔案所要存取的位置 `%temp%\secret.txt` 的完整路徑
        -> 即題目所提供的 `secret.txt`
    4. 以**某種演算法**將每 5 個 bytes 轉換為 16 個 bytes，並其和 hardcoded key **XOR**，再寫入 `secret.txt` 中
6. **某種演算法？**
    找到 magic number `1732584193, 4023233417, 2562383102, 271733878`，google 後可知其應為 ***MD5***
7. 將 `secret.txt` 轉回 bytes 並和 hardcoded key **XOR** 後有 18 個 ***MD5*** 後的結果，嘗試用 [online MD5 cracker](https://crackstation.net/) 卻無法將 FLAG 完成解出
    ![](https://i.imgur.com/iWxepkN.png)
8. 經由語句可繼續推測出部分內容，且可用 ***MD5*** 後的值檢查其正確性
9. 由於以解出的部分除了開頭的 `FLAG{` 外，皆為英文字母小寫和 `_`，便 *brute force* 剩下的部分，即可解出最後一個以外所有的值
10. 猜測最後一個除了 `_}` 外可能還有其他標點符號，加入標點符號在 *brute force* 一次，便可取得完整的 flag

## abexcm100
1. 用 `Detect It Easy` 發現檔案經過 `PESpin` 加殼
2. 動態直接執行可發現被 MessageBox 所印出來的 message 其實都在 `0x402000` 這邊
    而且在 *abex' 1st crackme* 後，雖然是 *Error*，但可以發現此時 *YEAH!* 已經在 memory 中了
3. 重新執行，在 `0x402000` 下 Memory Write Singleshoot breakpoint，此時 `F9` 便會使程式停在第一次嘗試寫入此 memory 的地方
4. 因為最後是用 MessageBox，將訊息顯示出來，嘗試在各個 MessageBox 相關的 address 下斷點，最後發現其會呼叫到 `MessageBoxTimeOutA`
    -> 在 `MessageBoxTimeOutA` 下斷點
5. 第一次 trigger 時，會顯示 *abex' 1st crackme*，之後便 `F8` 一步一步執行
6. 可在 `0x401026` 看到 `je`，且其正常情況並不會跳轉，之後便會將 `Error` 何其對應到的訊息 push 到 stack 上
    -> 在執行到此處時，強制 `ZF=1`，便可使其印出 flag
> 實際解的時候在看到 `YEAH!` 後面的訊息後，直接把前面五個跟 `FLAG{` XOR 發現**結果都是 199** 後，就把整串訊息跟 119 XOR 取得 flag 了XD

## Jwang's Terminal
1. 靜態分析後便可以發現在這個 terminal 中只有 `dir, cd, type` 可以用，且其維護的檔案都是加密過後的，只有用 `type [filename]` 時可以直接將其解密
    > 本來打算直接開始爆搜找 flag，嘗試了以後發現這真的不可能......
2. 仔細看 main function 便可發現 `unpackFileSystem` 就是用來將 `0x408020` 到 `0x197590B` 的檔案轉為其檔案的型態，用 ida python 將資料 dump 出來
    ```python=
    start = 0x408020
    end = 0x197590B
    raw = ida_bytes.get_bytes(start, end - start + 1)

    with open('raw.bin', 'wb') as f:
        f.write(raw)

    print('end')
    ```
    - 不論檔名或資料夾名稱其一定會以 `b'\x00'` 結尾，所以每成功 parse 完檔案或資料夾，只要找到下一個 `b'\x00'`，在其前面的部分即為其名稱
        - 檔名
            - 正常檔案
                - 名稱
                    不論檔名、大小，其檔名最後一定是 `b' \x1b'`，因此只要找到以此結尾的都將其判斷為檔案（包含 `b'\x00'`，2 個 bytes 之後才是檔案內容）
                - 內容
                    檔案的最後一定是 `b'\x00' * 4`，因此從名稱後開始找下一個 `b'\x00' * 4` 的位置，中間這一整段極為該加密檔案的內容（包含 `b'\x00' * 4`，10 個 bytes 之後才是檔案內容）
            - README.txt
                - 名稱
                    以此方法找出的檔名為 `b'README.txto\x01'`（同樣，包含 `b'\x00'`，2 個 bytes 之後才是檔案內容）
                - 內容
                    找法和上述相同
            - `Deprogrammer`
                - 名稱
                    以此方法找出的檔名為 `b'Deprogrammer\xd0'`（同樣，包含 `b'\x00'`，3 個 bytes 之後才是檔案內容）
                - 內容
                    找法和上述相同
        - 資料夾
            > 因為此題實際的檔案路徑並不重要，資料夾的部分只要沒有不小心取錯代表該資料夾的長度，使後面的檔案 parse 錯即可，便沒有仔細的了解名稱後那些數字所代表的意思
            > 整個是以 preorder traverse 的方式表現出整個檔案的架構

            以此方法找出名稱後，包含 `b'\x00'`，14 個 bytes 之後便是下一個檔案、資料夾
3. `file_decrypt`
    觀察 `file_decrypt` 中的 function，可以發現其演算法的實作其實是用 [tiny-AES-c](https://github.com/kokke/tiny-AES-c)，與寫死的 *key, iv*
    - 設定
        - `AES128`
        - `AES_BLOCKLEN = 16`
        - `CBC-mode`
    - `AES_init_ctx_iv`
        - 用此來初始化
    - `type [filename]`
        - call `AES_CBC_encrypt_buffer` 講檔案還原

    用 `c` 寫一個簡單將檔案還原的程式，可以讀進 `argv[1]` 的檔案，透過 `AES_init_ctx_iv` 初始化、 `AES_CBC_encrypt_buffer` 還原檔案，在將結果寫入 `argv[2]`  
    最後，在透過 python 寫一個自動化的 program 將所有的檔案都還原出來
4. 利用 `grep -rnw ./ -e 'Flag'` 可以找到 `lBq5NknLuUW` 還原的結果中就包含了 flag
    > 本來直接找有沒有 `FLAG{` 卻還找不到東西，以為要悲劇了，結果其實是因為被打成 **FALG{**，複製了以後卻不管是 **FLAG** 還是 **FALG** 都通過不了，以為我找到了假的  
    > 最後居然是我後面多了 EOF......