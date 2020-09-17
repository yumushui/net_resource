# Linux性能优化实战

10分钟帮你找到系统瓶颈

## You will get

+ Linux常用的性能分析工具合集；
+ 30个Linux性能问题诊断思路；
+ 读懂CPU、内存、I/O等指标；
+ 5个真实的线上环境分析案例。

## The teacher introduction

倪鹏飞，微软Azure资深工程师，同时也是 Kubernetes 项目维护者，主要负责开源容器编排系统 Kubernetes 在Azure的落地实践。曾任职于盛大云和腾讯，一直从事云计算领域，特别专注于IasS和容器技术。而近十年的云计算工作经验，也让他对 Linux的系统原理、常见性能问题已经优化方式了如指掌。

## The course introduction

Linux性能问题一直都是程序员头上的“紧箍咒”，哪怕是工作多年的资深工程师也不例外。日常工作中我们总是会遇到这样或那样的问题：

+ 应用程序响应太慢，从哪儿入手找原因？
+ 服务器总是时不时丢包，到底要怎么办？
+ 一个SQL查询要30秒，究竟是怎么回事？
+ 内存泄漏了，该怎么定位和处理？

面对这些问题，很多人都会发怵，似乎性能问题总是不那么简单。那如何才能搞定性能优化呢？

啃下所有的大块头原理书籍？多数人都会望而却步，不能坚持，即便是学了很多底层原理，碰到问题 时依然会不知所措、无从下手。向牛人请教有效的方法？但管的了一时，管不了永远，你很难形成系统的知识体系。实际上，找到正确的学习方法，你完全可以更轻松、更高效地掌握性能问题的解决之道。

鹏飞会以**案例驱动**的思路，从实际的问题出发，带你由浅入深学习一些基本底层原理，掌握常见的性能指标和工具，学习实际工作中的优化技巧，让你可以准确分析和优化大多数性能问题。还会有大量的案例分析，通过实战演练，更好地 消化和吸收巩固所学。

专栏共6个模块。

前4个模块从**资源使用的视角**出发，带你分析各种Linux资源可能碰到的性能问题，包括**CPU性能、磁盘I/O性能、内存性能、网络性能**，让你掌握必备的基础知识，会用常见的性能工具和解决方法。

第5个**综合实战模块**，将还原真实的工作场景，介绍一些开源项目、框架或者系统设计的案例的观测、剖析和 调优方法，让你在“高级战场”中学习演练。

## The course catalog

《Linux性能优化实战》
```
https://time.geekbang.org/column/intro/140
```

### 导读
```
开篇词  别再让Linux性能问题成为你的绊脚石

01 如何学习Linux性能优化？

```

### CPU性能篇
```
02 基础篇：“平均负载”到底是什么鬼？

03 基础篇：经常说的CPU上下文切换是什么意思？（上）

04 基础篇：经常说的CPU上下文切换是什么意思？（下）

05 基础篇：CPU使用率居然是 100% ？我该怎么办

06 案例篇：系统CPU使用预警，可高CPU应用到底在哪儿？

07 案例篇：大量不可中断进程和僵尸进程出现，怎么办？（上）

08 案例篇：大量不可中断进程和僵尸进程出现，怎么半？（下）

09 基础篇：怎么理解Linux软中断？

10 案例篇：软中断CPU使用率很高，我该怎么办？

11 套路篇：如何“快准狠”找到系统CPU的瓶颈？

12 套路篇：CPU性能优化的几个思路

13 答疑篇：CPU性能综合答疑（一）

14 答疑篇：CPU性能综合答疑（二）

```

### 内存性能篇
```
15 基础篇：Linux内存是怎么工作的？

16 基础篇：怎么理解内存中的Buffer和Cache？

17 案例篇：如何利用系统缓存优化程序的运行效率？

18 案例篇：内存泄漏了，我该如何定位和处理？

19 案例篇：为什么系统的Swap变高了？（上）

20 案例篇：为什么系统的Swap变高了？（下）

21 套路篇：如何“快准狠”找到系统内存的问题？

22 答疑篇：内存性能综合答疑（三）

```

### I/O性能篇
```
23 基础篇： Linux文件系统是怎么工作的？

24 基础篇： Linux磁盘I/O是怎么工作的？（上）

25 基础篇： Linux磁盘I/O是怎么工作的？（下）

26 案例篇： 如何找出狂打日志的“内鬼”？

27 案例篇： 为什么我的磁盘I/O延迟很高？

28 案例篇： 一个SQL查询要30秒，究竟是怎么回事？

29 案例篇： Redis 响应严重延迟，要怎么解决？

30 套路篇： 如何“快准狠”找出系统I/O的瓶颈？

31 套路篇： 磁盘I/O性能优化的几个思路

32 答疑篇： I/O性能综合答疑（四）

33 加餐（一）：Linux系统原理和性能优化书籍推荐

```

### 网络性能篇
```
34 基础篇：关于Linux网络，你必须知道这些（上）

35 基础篇：关于Linux网络，你必须知道这些（下）

36 基础篇：C10K 和 C100K 回顾

37 套路篇：如何评估系统的网络性能？

38 案例篇：DNS解析，时快时慢，我该怎么办？

39 案例篇：怎么使用 tcpdump 和 wireshark 分析网络流量？

40 案例篇：DDoS攻击使性能下降了，我该怎么缓解？

41 案例篇：网络请求延迟变大了，我该怎么半？

42 案例篇：如何优化NAT性能？ （上）

43 案例篇：如何优化NAT性能？ （下）

44 套路篇：网络性能优化的几个思路（上）

45 套路篇：网络性能优化的几个思路（下）

46 答疑篇：网络性能综合答疑（五）

47 加餐（二）：网络原理和Linux内核书籍推荐

```

### 综合实战篇
```
48 案例篇：应用容器化后，为什么启动变慢了？

49 案例篇：服务器总是时不时丢包，我该怎么办？（上）

50 案例篇：服务器总是时不时丢表，我该怎么办？（下）

51 案例篇：内核线程CPU利用率太高，我该怎么办？

52 案例篇：动态追踪（BPF、bcc）怎么用？（上）

53 案例篇：动态追踪（BPF、bcc）怎么用？（下）

54 案例篇：服务吞吐量下降很厉害，怎么分析？

55 套路篇：系统监控的综合思路

56 套路篇：应用监控的综合思路

57 套路篇：分析性能问题的一般步骤

58 套路篇：优化性能问题的一般方法

59 套路篇：Linux性能工具速查

60 答疑篇：从知道到做到（六）

结束语：愿你公攻克性能难关


```

## Linux 性能工具速查

Linux 的性能工具
![Linux performance tools](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/Linux%20performance%20tools.png  "Linux performance tools")


常见的 CPU 性能指标
![cpu_performance_metric](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/cpu_performance_metric.png  "cpu_performance_metric")

CPU 性能工具速查表
![cpu_performance_tools](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/cpu_performance_tools.png  "cpu_performance_tools")

常见的内存性能指标
![memory performance metric](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/memory%20performance%20metric.png  "memory performance metric")

内存性能工具速查表
![memory performance tools](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/memory%20performance%20tools.png  "memory performance tools")

常见的 I/O 性能指标
![IO_performance_metric](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/IO_performance_metric.png  "IO_performance_metric")

文件系统和磁盘 I/O 性能工具速查表
![IO_performance_tools](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/IO_performance_tools.png  "IO_performance_tools")

常见的网络性能指标
![network_performance_metric](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/network_performance_metric.png  "network_performance_metric")

网络性能工具速查表
![network_performance_tools](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/network_performance_tools.png  "network_performance_tools")

Brendan Gregg 整理的 Linux 基准测试工具图谱
![linux_performance_banchmark_tools](https://github.com/yumushui/net_resource/blob/master/linux_performance_optimization/picture/linux_performance_banchmark_tools.png  "linux_performance_banchmark_tools")


