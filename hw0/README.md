# Computer Security Fall 2020 HW0 writeup

## Web - owoHub
> FLAG{owo_ch1wawa_15_th3_b35t_uwu!!!}

1. Check *source code*
   - how to get flag?
   ```js
   if (givemeflag === "yes" && userInfo.admin) response.send(FLAG);
   ```
   - where can be used?
      1. only check that `cute` end with `true` or `false`
      ```js
      if (typeof username !== "string" || typeof cute !== "string" || username === "" || !cute.match("(true|false)$"))
      ```
      2. asdf
      ```js
      const userInfo = `{"username":"${username}","admin":false,"cute":${cute}}`;
      ```
      3. asdf
      ```js
      const api = `http://127.0.0.1:9487/?data=${userInfo}&givemeflag=no`;
      ```
2. 