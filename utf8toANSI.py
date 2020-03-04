# 把utf8編碼的cpp檔改為ANSI編碼

import glob

targetdir = "C:/Users/Leno/Desktop/cpp_m_ANSI/"
fs = glob.glob("C:/Users/Leno/Desktop/cpp_m/*")

for f in fs:
    with open(f, "r", encoding="utf-8") as ff:
        filename = f.split("/")[-1].split("\\")[-1]
        fc = ff.read()
        ff.close()
        with open(targetdir + filename, "w", encoding="ANSI") as ww:
            ww.write(fc)
            ww.close()

print(filename)
print(fc)
