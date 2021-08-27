## 文件夹中所有的JPG文件都被按照某个统一的规则重命名。
## 先根据文件最后修改时间，对文件排序
## 新的图片文件名形如连接ISBN和一个2位的数字。

$i = 1
$YEAR = 2021
$ISBN = 9787559433879

Get-ChildItem -Path c:\pictures -Filter *.jpg | 
Sort-Object LastWriteTime | 
ForEach-Object {
    $extension = $_.Extension
    $newName = '{0}_{1}_{2:d2}{3}' -f $YEAR, $ISBN, $i, $extension
    $i++
    Rename-Item -Path $_.FullName -NewName $newName
}
