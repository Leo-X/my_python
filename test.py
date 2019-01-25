# text2numbers.py
# A program to convert a textual message into a sequence of
# numbers, utilizing the underlying Unicode encoding.


def main():
    str = "aBcabc"
    # 仅首字符大写 副本             result:Abcabc
    print(str.capitalize())
    # 全部转小写 副本             result:abcabc
    print(str.lower())
    # 全部转大写 副本             result:abcabc
    print('upper:', str.upper())

    # 给定宽度字段里居中 副本        result: aBcabc
    print(str.center(9))
    # 给定宽度字段里居左 副本        result:aBcabc
    print(str.ljust(9))
    # 给定宽度字段里居右 副本        result:   aBcabc
    print(str.rjust(9))

    # str中 ab 出现次数             result:3
    print(str.count("ab"))
    # str中 ab 首次出现的位置   result:3,找不到返回-1
    print('find:', str.find("ab"))
    # str中 ab 最后一次出现的位置（从右往左算） result:3
    print('rfind:', str.rfind("ab"))

    # 列表转字符串， 逗号作为分割符  result:11,22,bb
    print(",".join(["11", "22", "bb"]))
    # a,b,c,d 字符串列表， 逗号作为分割符      result:a,b,c,d
    print(",".join("abcd"))

    # 字符串分割，默认按空格分割      result:['11','22']
    print('split:', "11,22".split(","))

    # 删除字符串前导空格    result:abc
    print("  abc".lstrip())
    # 删除字符串后面空格    result:abc
    print("  abc ".rstrip())

    # old_str,new_str;bb替换str中所有出现的 aB  result:bbcabc
    print(str.replace("aB", "bb"))
    # 每个单词首字母大写,其余小写 副本  result:Wang Chuang
    print("wanG chuanG".title())


main()
