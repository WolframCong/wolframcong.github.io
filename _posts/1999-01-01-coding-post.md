---
layout: post
title:  "Hello jekyll! Hello Github-pages!"
description: 国际惯例
date:   1999-01-01 21:00:00 +0800
categories: Javascript NodeJS
---
"Hello jekyll! Hello Github-pages!"

搞了半天终于成功发布了，不过我对这个Jekyll还不是十分了解，markdown文件中一些语法特征在网页中显示并不完整。我会在这篇post中进行调试。

```javascript
const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello World')
})

app.listen(3000)
```

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题

```markdown
1. 有序列表项 一
2. 有序列表项 二
3. 有序列表项 三
```

1. 有序列表项 一
2. 有序列表项 二
3. 有序列表项 三

```markdown
*斜体*
**粗体**
***加粗斜体***
~~删除线~~
<u>下划线</u>
`背景高亮`
<kbd>ctrl</kbd> + <kbd>C</kbd>
:smile:
```

*斜体*  
**粗体**  
***加粗斜体***  
~~删除线~~  
<u>下划线</u>  
`背景高亮`  
<kbd>Ctrl</kbd> + <kbd>C</kbd>  
:smile:  

```markdown
* * *
***
*****
- - -
---
```
* * *
***
*****
- - -
---
```markdown
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |
```

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |

```markdown
行内$E=mc^2$公式
<br/>
行间$$E=mc^2$$公式
```

行内$E=mc^2$公式  
<br/> 
行间$$E=mc^2$$公式  

```markdown
>  这是引用

>还
>是
>引
>用
```
> 这是引用
>>还是引用  

[test](postimage/test.jpg)