# ndic
Python module for NAVER English-Korean and Korean-English dictionaries

## Introduction
Search of both English-Korean and Korean-English dictionaries is provided.

## Requirements
This module crawl the web <http://endic.naver.com/>, so all you need is an **Internet connection**.


## Installation
Install via pip:

```
$ pip install ndic
```

## Usage
The usage is very simple.

```
>>> from ndic import ndic
```
Entering an English word as the function argument will return the corresponding Korean word(s).

```
>>> ndic('apple')
'사과'
```
Conversely, entering a Korean word as the function argument will return the corresponding English word(s).

```
>>> ndic('안녕하세요')
'Hi!'
```
Phrases or words may also be searched.

```
>>> ndic('in order to')
'(목적) 위하여'
```

Entering a nonexistent word as the function argument will return the empty string.

```
>>> ndic("aslkjfwe")
''
>>> ndic("아댜리야")
''
```

If your network connection is lost, you will get below message.

```
>>> ndic('...')
'Network connection is lost. Please check the connection to the Internet.'
```
