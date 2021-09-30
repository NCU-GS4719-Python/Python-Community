# 文字相關方法
```python
name="Benjamin"
print(str1.find("n")) # 2
print(str1.index("k")) # ValueError: substring not found

print(name.upper()) # BENJAMIN

print(name.lower()) # benjamin

tuple1=('a', 'b', 'c')
print('-'.join(tuple1)) # a-b-c

string1='     Beanjmin'
print(string1.strip()) # 移除字串左右兩側空白字串(space)
print(string1.lstrip()) # 移除字串左側空白字串(space)
print(string1.rstrip()) # 移除字串右側空白字串(space)

string2='1;2;3'
print(string2.split(';')) # ['1', '2', '3']

# 使用成員運算子 in 判斷字串有無被包含在另一個字串內
print('B' in name)
# True
print('k' in name)
# False

print('Benjamin'.isalpha()) # 判斷是否為文字
# True
print('314'.isdigit()) # 判斷是否為數字
# True
print('28C'.isalnum()) # 判斷是否為文數字，注意28C沒有空格
# True
print('28 C'.isalnum()) #  判斷是否為文數字，注意28 C有空格
# False
print(' '.isspace()) # 判斷是否為空白字串
# True

print('Benjamin'.islower()) # 判斷字串是否全為大寫
# False
print('Benjamin'.islower()) # 判斷字串是否全為小寫
# False


```

# 文字相關運算

假設字串 a 為 'Hello'，字串 b 為 'Python'

|運算|說明|舉例|
|-|-|-|
|`+`|文字相加|`a+b`結果為'HelloPython'|
| `*` | 文字重複 | `a*2`結果為'HelloHello' |
|`[]`  | 索引 | `a[1]` 得到 `'e'` |
| `[:]` | 切片 | `a[1:4]` 得到 `'ell'` |
| in | 成員運算 | `'H' in a` 得到 `1(True)` |
| not in | 成員運算 | `'m' not in a` 得到 `1(True)` |
| `r/R` | Raw String，保留特殊字元，“r” 不分大小寫，必須緊連著左引號 | `print(r'\n')` : 印出 '\n' `print(R'\n')` : 印出 '\n' |
|  len() | 內建函數，求文字長度 | `len(a)` 結果為 `5` |
| str() | 內建函數，將資料轉成文字 | `str(45)` 結果為 `'45'` |


# 文字格式化輸出
有三種方法，分別為：
1. f字串 (f-string)
2. 文字format方法 (str.format())
3. 文字格式化運算子 (% Operator)

## f字串 (f-string)
```python
temperature = 28.812345
print(f'今天的溫度是{temperature}度')
# 今天的溫度是28.812345度
print(f'今天的溫度是{temperature:.2f}度')
# 今天的溫度是28.81度
print(f'今天的溫度是{temperature:.0f}度')
# 今天的溫度是29度
print(f'今天的溫度是{temperature:3.0f}度')
# 今天的溫度是 29度
```

## 文字format方法 (str.format())
```python
temperature = 28.812345
print('今天的溫度是{}度'.format(temperature))
# 今天的溫度是28.812345度
print('今天的溫度是{temp}度'.format(temp=temperature))
# 今天的溫度是28.812345度
print('今天的溫度是{:.2f}度'.format(temperature))
# 今天的溫度是28.81度
print('今天的溫度是{:.0f}度'.format(temperature))
# 今天的溫度是29度
print('今天的溫度是{:3.0f}度'.format(temperature))
# 今天的溫度是 29度
```

## 文字格式化運算子 (% Operator)
```python
temperature = 28.812345
print('今天的溫度是%f度'%temperature)
# 今天的溫度是28.812345度
print('今天的溫度是%.2f度'%temperature)
# 今天的溫度是28.81度
print('今天的溫度是%.0f度'%temperature)
# 今天的溫度是29度
print('今天的溫度是%3.0f度'%temperature)
# 今天的溫度是 29度
```