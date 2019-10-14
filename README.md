# HorcruxCollegeExtract
 魂器学院图片提取

## 使用方法

编译
```
gcc src\decrypt.c src\xxtea.c -o decrypt
```

提取PNG

```
decrypt [infile] [outfile]
```

`decrypt.py`是一个基于此程序的简单封装，可以批量解码图片。

```
python decrypt.py [file / directory]
```

## 参考资料

https://www.52pojie.cn/thread-594286-1-1.html