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
