import sys

Numbers_In_Line = 16  # 一行有几个数字
'''
* 将一个文件转换为二进制文件(binary)
* python3 tran_to_binary.py input_file out_file
* 20190713
'''


class TranStrToBinary():
    def tran_string_to_binary(self, buf):
        bytes_str = bytes(buf, encoding='utf-8')

        strbuf = ""
        for i in range(0, len(bytes_str)):
            tmp_str = str(hex(bytes_str[i]))
            tmp_str = tmp_str[2:].rstrip()
            if len(tmp_str) < 2:
                strbuf += "0" + tmp_str + " "
            else:
                strbuf += tmp_str + " "

        num = Numbers_In_Line * 3
        listBuf = list(strbuf)
        line_count = len(listBuf)
        if line_count / num > 0:
            for i in range(0, int(line_count / num)):
                pos = (i + 1) * num
                listBuf[pos - 1] = '\n'
        strbuf = "".join(listBuf)
        return strbuf.rstrip()

    def tran_binary(self, inputFile, outputFile):
        try:
            with open(inputFile, "r") as fp_r:
                bufs = fp_r.read()
        except FileNotFoundError:
            print("The input files is not exist !")
            exit(2)

        print(self.tran_string_to_binary(bufs))
        with open(outputFile, "w") as fp_w:
            fp_w.write(self.tran_string_to_binary(bufs))


if __name__ == '__main__':
    print(str(sys.argv[0]) + " enter")

    tstb = TranStrToBinary()

    if len(sys.argv) != 3:
        print("The Bad Parameters !")
        exit(1)

    tstb.tran_binary(sys.argv[1], sys.argv[2])