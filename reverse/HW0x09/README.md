# HW0x0C writeup

## ChristmasGift
> FLAG{what_a_boaring_challnge_but_you_did_it_yeah_yeah}

1. Given a *gzip compressed data*, `gift.zip`. Decompress and get an *64-bit ELF*, `gift`.

2. Decompile `gift` and find that the file will take an input and compare with a hardcoded string. If matched, it will stdout some content.

3. Save the output content and check its file type.

   ```shell
   1: gzip compressed data, was "gift", last modified: Thu Dec 24 22:50:30 2020, max speed, from Unix
   ```

   Decompress and get an *64-bit ELF*. Decompile it to find out that it's similar to `gift` but with a different required matched input.

4. Write a script to automate the process, get required input from ELF, run ELF given the required input and save the output, decompress the output file, change the permission.

5. After repeating the process 1000 times, get an ELF which is slightly different. It comes with a shorter required input, `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@terrynini@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`, and output smaller content. Execute, give the input, and get the flag.

   ```shell
   ./999
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@terrynini@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   Ok, that sounds good
   FLAG{what_a_boaring_challnge_but_you_did_it_yeah_yeah}
   ```

# JustOnLinux
> FLAG{7h1s-i5-ac7ua11y-a-b4s364enc0d3-alg0r1thm}

1. Execute `JustOnLinux` and guess that it use some encoding algorithm to encode `argv[1]`.

   $\rightarrow$ find an input that will match the string given in `flag`

2. Decompile the file and find the following part implements the encode algorithm.

   ```c
     v13 = (v26 << 8) + (v25 << 16) + v12;
     out_0 = out_4;
     out_2 = out_4 + 1;
     *((_BYTE *)out_str + out_0) = aVwxyzabcdefghi[(v13 >> 18) & 0x3F];
     out_1 = out_2++;
     *((_BYTE *)out_str + out_1) = aVwxyzabcdefghi[(v13 >> 12) & 0x3F];
     *((_BYTE *)out_str + out_2) = aVwxyzabcdefghi[(v13 >> 6) & 0x3F];
     out_3 = out_2 + 1;
     out_4 = out_2 + 2;
     *((_BYTE *)out_str + out_3) = aVwxyzabcdefghi[v13 & 0x3F];
   }
   if ( inputLen % 3 )
   {
     for ( i = 0; i < 3 - inputLen % 3; ++i )
       *((_BYTE *)out_str + v22 + inputLen % 3 + i - 3) = ' ';
   }
   ```

   Google `>> 18) & 0x3F` and find it's actually **base64 encoding** with table `aVwxyzabcdefghi` and padding `space`.

3. Find an implementation of *base64 encode/decode* online, [gehaxelt/Python-MyBase64](https://github.com/gehaxelt/Python-MyBase64/blob/master/mybase64.py), and replace its **table and padding**.

4. Use it to decode the given string and get flag.