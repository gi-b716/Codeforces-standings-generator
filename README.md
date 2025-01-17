# Codeforces-standings-generator

## zh

这是一个可以根据 Codeforces 评测记录计算排行榜的工具。

在比赛界面点击上方的 `ADM.`，找到 `Export the judgment log to DAT-file`，勾选你需要的选手类型，点击 `Show Log`，就获取到了评测记录。

下载 `main.py`，通过命令行运行，其中 `[file]` 为评测记录文件名。

```bash
python main.py [file]
```

输出由三部分组成。

```
[比赛名]
"example"

[排名]
1.xxxxxx A:xxx B | xxx(xxx)

[一血情况]
A: xxx
B:
```

`main.py` 前三行的三个变量可自行修改。

1. `ignoreCE`：忽略 CE 的提交
2. `ignore_submission_after_AC`：忽略 AC 了本题之后的所有提交
3. `prettyTime`：更好看的时间输出

## en

This is a tool that calculates the standings based on Codeforces judgment logs.

Click on `ADM.` at the top of the contest screen, find `Export the judgment log to DAT-file`, check the type of player you want, click on `Show Log`, and you will get the judgment log.

Download `main.py` and run it from the command line, where `[file]` is the name of the judgment log file.

```bash
python main.py [file]
```

The output consists of three parts.

```
[contest name]
“example”

[Ranking]
1.xxxxxx A:xxx B | xxx(xxx)

[First Blood]
A: xxx
B: xxx
```

The three variables in the first three lines of `main.py` can be modified at your discretion.

1. `ignoreCE`: ignore CE submissions
2. `ignore_submission_after_AC`: Ignore all submissions after AC's question.
3. `prettyTime`: better looking time output.
