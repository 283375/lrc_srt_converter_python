# lrc-srt converter

试过很多 lrc 转 srt 的小工具，但都没有下面的功能。

如果你知道有某个软件可以实现下面的功能，麻烦提个 issue，十分感谢。

## 特性

- 多行同一时间的歌词

```lrc
[00:05.56]Example line 1
[00:07.38]Example line 2
[00:07.38]这里一般会塞个翻译
[00:08.96]Example line 3
```

```srt
1
00:00:05,560 --> 00:00:07,380
Example line 1

2
00:00:07,380 --> 00:00:08,960
Example line 2
这里一般会塞个翻译

3
00:00:08,960 --> 00:00:18,960
Example line 3


```

- 堆叠时间的歌词

```lrc
[00:05.56]Example line 1
[00:07.38][00:08.96][00:12.56][00:30.87][01:30.25]Example line 2
[00:07.38][00:08.96][00:12.56][00:30.87][01:30.25]每次看到这种歌词都会有点难受，虽然这确实省空间
[00:45.77][01:02.75]Example line 3
```

```srt
1
00:00:05,560 --> 00:00:07,380
Example line 1

2
00:00:07,380 --> 00:00:08,960
Example line 2
每次看到这种歌词都会有点难受，虽然这确实省空间

3
00:00:08,960 --> 00:00:12,560
Example line 2
每次看到这种歌词都会有点难受，虽然这确实省空间

4
00:00:12,560 --> 00:00:30,870
Example line 2
每次看到这种歌词都会有点难受，虽然这确实省空间

5
00:00:30,870 --> 00:00:45,770
Example line 2
每次看到这种歌词都会有点难受，虽然这确实省空间

6
00:00:45,770 --> 00:01:02,750
Example line 3

7
00:01:02,750 --> 00:01:30,250
Example line 3

8
00:01:30,250 --> 00:01:40,250
Example line 2
每次看到这种歌词都会有点难受，虽然这确实省空间


```

就这些，没了。

## 有感而发

这应该是我初中时（大概是 16，17 年）一直想要的一个软件。

已经想不起来为什么会有这种奇葩需求了，不过依稀记得是要让我 Lumia 640 上的 ACG Player 能同时显示歌词原文和译文（就像第一个特性那样）。

现在 22 年了，人读了大学，学了点 Python，软件写出来了，

可惜我已经转安卓阵营，Lumia 640 也因为胡乱刷机成砖了。

就当了了个念想吧。
