# crypto writeup

## POA - Padding Oracle Attack
> FLAG{31a7f10f1317f622}

1. Gain information from [server.py](./POA/server.py).
    ```python
    def encrypt(plain):
        # random iv
        iv = os.urandom(16)
        # encrypt
        aes = AES.new(key, AES.MODE_CBC, iv) 
        cipher = aes.encrypt(pad(plain))
        return iv + cipher
    ```
    - Use **AES CBC** to encrypt.
      - Check if the server return special error message for **Padding Error**

        ```python
        try:
            decrypt(bytes.fromhex(input('cipher = ')))
            print('YESSSSSSSS')
        except PaddingError:
            print('NOOOOOOOOO')
        ```

        - Reponse with `NOOOOOOOOO` when **Padding Error**. Therefore, we can use it to seperate **Padding Error** from other errors.
          - Vulnerable to **Padding Oracle Attack**

      - The given *cipher* contain a random **iv** before the actual cipher text.

    - Observe the *padding mechanism*.

      ```python
      def pad(data):
          padlen = 16 - len(data) % 16
          return data + int('1' + '0' * (padlen * 8 - 1), 2).to_bytes(padlen, 'big')
      ```

      - e.g. <u>0x10 0x11 0x36 0x67 0x38 0xBC 0x03 0x21 0xEF **0x80 0x00 0x00**</u>
      - Test it with different data length
        - pad with `0x80 + 0x00 * ?` to the desire size
        - Mechanism: **ISO 7816-4 Padding**
      - Block Size = **16**

2. Connect to server.

    ```shell
    ❯ nc 140.112.31.97 30000
    cipher = 4b07382f90edbf6be35aa9a3b7e183537e031af7cf37556046096be183a2d999d1da866aad7843c1e0378e3d68e8e60a
    cipher = 
    ```

    Transfrom *hex* back to *bytes*. Find that it contains 3 blocks with the first one being *iv*.

3. Implement **Padding Oracle Attack** to find the plain text.

## COR - Correlation Attack
> FLAG{dfuihj}

1. Gain information from [generate.py](./COR/generate.py).

   - Combine *three* LFSR generators, with **Boolean function**, to generate the [output](./COR/output.py).

   - All *three* LFSR use part of **flag** as initials and **hard-coded** feedback coefficients.

   - **Boolean function**: (x1 & x2) ^ ((not x1) & x3)

     |  x1  |  x2  |  x3  | output |
     | :--: | :--: | :--: | :----: |
     |  0   |  0   |  0   |   0    |
     |  0   |  0   |  1   |   1    |
     |  0   |  1   |  0   |   0    |
     |  0   |  1   |  1   |   1    |
     |  1   |  0   |  0   |   0    |
     |  1   |  0   |  1   |   0    |
     |  1   |  1   |  0   |   1    |
     |  1   |  1   |  1   |   1    |
     | 50%  | 75%  | 75%  |  100%  |

     (last row show the percentage of the column which is **same as output**)

     - Both **x2, x3** has 75% of its input same as the output
     - Brute force to get generated keystream of all posibilities of **x2, x3**, compare them with known output and only keep those with same bit rate around 75%.

   - Since use part of **flag** as initials, instead of 256<sup>2</sup> posibilities for each initials, there is only 95<sup>2</sup> posibilities.

2. Use all possible initials of **x2, x3** to generate the output and only keep those has same bit rate **over 70%**.

3. Use all possible initials of **x1** to generate the output and combine them all pairs of possible **x2, x3** output using **Boolean function**. Find the only combined **x1, x2, x3** outputs that generate the *exact output*.

4. Flag of the question will then be `FLAG{ + initials of that x1 + initials of that x2 + initials of that x3 + }`.