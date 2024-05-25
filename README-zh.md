# Shell Helper

记不住晦涩的shell命令？

没问题：只需输入`? do the thing`，让你的LLM朋友们来处理。

![示例用法](sample_usage.png)

## 安装指南

我将原库中的openai调用换成了国内的大模型（01的yi），实测需要智力稍高的llm才能够完美的执行任务，推荐（yi-large-turbo），因为01的模型调用也兼容了openai的api，所以还是需要安装对应的openai库

```bash
pip3 install openai
```

根据操作系统的环境、使用的终端类型、大模型平台和对应的key，修改代码中开头的4个变量，就可以完成配置。然后给脚本加一个别名：

```bash
alias ?='shell_helper.py $@'
```
注：有的操作系统'?'是有意义的关键字，所以可以替换为别的方便记的字母，比如'q'或者'a'

如果需要fork该库并且修改代码，记得不要提交key！！