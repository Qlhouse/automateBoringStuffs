# delete line

## Delete a range of lines

> `[Starting Line Number], [Ending Line Number] d`

> `:5,7d`

Delete line number 5 to line number 7

## Delete line with pattern

> `:g/linux/d`

Delete lines include the word **linux**.

> `:g/^T/d`

Delete lines start with **T**

> `:g/^$/d`

Delete all blank lines

# Replace

> **`[addr]s/源字符串/目的字符串/[option]

+ **`addr`**，表示检索范围，`addr`省略时表示当前行
  + `1,n`，表示从第1行到n行
  + `%`，表示整个文件
  + `.,$`，表示从当前行到文件尾

+ **`option`**，表示操作类型，省略时仅对每一个匹配字符串进行替换
  + `g:global`，表示全局替换
  + `c:confirm`，表示进行确认
  + `p`，表示替代结果逐行显示（CTRL + L）恢复屏幕
  + `i:ignore`，表示不区分大小写

# Insert
