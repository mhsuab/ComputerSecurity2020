#include <stdio.h>
#include <string.h>
#include <stdint.h>
#define CBC 1

#include "aes.h"

int main(int argc, char *argv[])
{
    unsigned char buf[1024 * 128];
    FILE *fp, *fp2;
    int i, ret, c;
    fp = fopen(argv[1], "r");
    ret = fread(buf, 1, sizeof(buf), fp);
    fclose(fp);

    uint8_t key[] = {0xE9, 0x31, 0xDF, 0xC0, 0xC3, 0x7A, 0xEE, 0xAC, 0x6E, 0xC9, 0x87, 0x1C, 0x8A, 0x7A, 0xF6, 0xEC};
    uint8_t iv[] = {0xA1, 0xA4, 0xc4, 0x1c, 0x1c, 0x5b, 0xc5, 0x2e, 0x90, 0xda, 0xb8, 0xfe, 0x46, 0x23, 0xbf, 0xbb};
    struct AES_ctx ctx;

    AES_init_ctx_iv(&ctx, key, iv);
    AES_CBC_encrypt_buffer(&ctx, buf, ret);


    fp2 = fopen(argv[2], "w");
    for (i = 0; i < ret; i++)
    {
        c = buf[i];
        fputc(c, fp2);
    }
    fclose(fp2);

    return 1;
}