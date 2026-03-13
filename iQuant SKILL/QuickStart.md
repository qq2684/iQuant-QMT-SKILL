# 🚀 iQuant QMT Python SKILL 完整知识库

## 👋 欢迎使用

这是一个**完全按照迅投QMT内置Python知识库规范**编制的**模块化SKILL库**。

为QMT量化交易者提供：
- 📖 系统化的学习文档
- 💻 完整可运行的代码示例
- 🔍 详细的API参考
- 🛡️ 风险管理最佳实践

---

## 📂 项目结构一览

```
qmt-skill/
│
├── 📋 入口文档
│   ├── README.md              ← 项目说明书（推荐首先阅读）
│   ├── INDEX.md               ← 总索引与快速导航
│   └── SUMMARY.md             ← 项目完成总结
│
├── 📚 核心学习模块
│   ├── overview.md            ← 系统概述与基础概念
│   ├── execution-mechanisms.md ← 三种运行机制详解
│   ├── backtesting-guide.md   ← 完整的回测指南
│   ├── live-trading-guide.md  ← 完整的实盘指南
│   ├── market-data-api.md     ← 行情数据API参考
│   ├── trading-api.md         ← 交易函数API参考
│   └── best-practices.md      ← 编码规范与最佳实践
│
├── 💻 代码示例库
│   └── examples/
│       ├── backtest.md        ← 回测完整示例（600+ 行代码）
│       ├── live-trading.md    ← 实盘完整示例（500+ 行代码）
│       ├── subscribe.md       ← 事件驱动示例（多个完整策略）
│       └── run-time.md        ← 定时任务示例（多个完整策略）
│
└── ✅ 项目文档（当前文件）
```

---

## 🎯 快速开始指南

### 📖 如果你是初学者

**推荐的学习顺序** (总耗时：约2小时)

1. **阅读这个文件** (5分钟)
   - 了解项目结构

2. **打开 README.md** (10分钟)
   - 了解项目概况和快速开始

3. **阅读 overview.md** (15分钟)
   - 理解QMT系统基本概念
   - 了解回测vs实盘

4. **阅读 execution-mechanisms.md** (20分钟)
   - 理解三种运行机制
   - 选择合适的方式

5. **根据你的需求选择**：
   - **我想做回测** → 阅读 backtesting-guide.md + examples/backtest.md
   - **我想做实盘** → 阅读 live-trading-guide.md + examples/live-trading.md
   - **我想做高频** → 阅读 examples/subscribe.md
   - **我想做定时** → 阅读 examples/run-time.md

6. **查询API** (随时)
   - market-data-api.md - 行情函数
   - trading-api.md - 交易函数

7. **学习最佳实践** (20分钟)
   - best-practices.md - 规范和最佳做法

---

### 🧑‍💼 如果你有编程经验

**建议的浏览方式**

1. 快速扫一遍 [INDEX.md](./INDEX.md)
2. 直接跳到对应的 [examples/](./examples/) 目录查看示例
3. 需要详细说明时查询 [market-data-api.md](./market-data-api.md) 或 [trading-api.md](./trading-api.md)
4. 性能/风险问题查看 [best-practices.md](./best-practices.md)

---

## 📋 文件索引

### 入门文档 (必读)

| 文件 | 用途 | 阅读时间 |
|------|------|--------|
| [README.md](./README.md) | 项目说明书 | 10分钟 |
| [INDEX.md](./INDEX.md) | 全索引，导航工具 | 5分钟 |
| [SUMMARY.md](./SUMMARY.md) | 项目完成信息 | 5分钟 |

### 核心学习模块 (重点)

| 文件 | 主题 | 适合人群 | 阅读时间 |
|------|------|--------|--------|
| [overview.md](./overview.md) | QMT系统概述 | 所有人必读 | 15分钟 |
| [execution-mechanisms.md](./execution-mechanisms.md) | 三种运行机制 | 需要选择机制 | 20分钟 |
| [backtesting-guide.md](./backtesting-guide.md) | 完整的回测指南 | 想做回测 | 30分钟 |
| [live-trading-guide.md](./live-trading-guide.md) | 完整的实盘指南 | 想做实盘 | 40分钟 |
| [market-data-api.md](./market-data-api.md) | 行情API参考 | 需要查询数据 | 15分钟 |
| [trading-api.md](./trading-api.md) | 交易API参考 | 需要下单交易 | 20分钟 |
| [best-practices.md](./best-practices.md) | 最佳实践 | 编写高质量代码 | 25分钟 |

### 代码示例 (实践)

| 文件 | 类型 | 代码行数 | 难度 |
|------|------|--------|------|
| [examples/backtest.md](./examples/backtest.md) | 回测策略 | 600+ | ⭐⭐ |
| [examples/live-trading.md](./examples/live-trading.md) | 实盘策略 | 500+ | ⭐⭐⭐ |
| [examples/subscribe.md](./examples/subscribe.md) | 事件驱动 | 400+ | ⭐⭐⭐ |
| [examples/run-time.md](./examples/run-time.md) | 定时任务 | 500+ | ⭐⭐ |

---

## 🎯 选择你的学习路径

### 路径1️⃣：我想学习如何回测

```
1. overview.md           (理解基本概念)
   ⬇️
2. execution-mechanisms.md (理解handlebar)
   ⬇️
3. backtesting-guide.md  (学习详细流程)
   ⬇️
4. examples/backtest.md  (查看完整示例)
   ⬇️
5. market-data-api.md    (查询数据函数)
   ⬇️
6. best-practices.md     (优化你的代码)
```

### 路径2️⃣：我想学习实盘交易

```
1. overview.md           (理解基本概念)
   ⬇️
2. execution-mechanisms.md (理解handlebar)
   ⬇️
3. live-trading-guide.md (学习详细流程)
   ⬇️
4. examples/live-trading.md (查看完整示例)
   ⬇️
5. trading-api.md        (查询下单函数)
   ⬇️
6. market-data-api.md    (查询行情函数)
   ⬇️
7. best-practices.md     (风险管理)
```

### 路径3️⃣：我想做分笔级别高频交易

```
1. overview.md           (理解基本概念)
   ⬇️
2. execution-mechanisms.md (理解subscribe)
   ⬇️
3. examples/subscribe.md (查看完整示例)
   ⬇️
4. market-data-api.md    (理解行情订阅)
   ⬇️
5. trading-api.md        (理解下单)
   ⬇️
6. best-practices.md     (性能优化)
```

### 路径4️⃣：我想做定时监控

```
1. overview.md           (理解基本概念)
   ⬇️
2. execution-mechanisms.md (理解run_time)
   ⬇️
3. examples/run-time.md  (查看完整示例)
   ⬇️
4. market-data-api.md    (查询数据函数)
   ⬇️
5. best-practices.md     (优化代码)
```

---

## 🔑 核心概念速览

### 编码规范

```python
#coding:gbk  # ← 必须在第一行

import pandas as pd
import numpy as np

def init(C):
    C.stock = C.stockcode + '.' + C.market

def handlebar(C):
    data = C.get_market_data_ex(['close'], [C.stock], count=100, subscribe=False)
```

### 两种交易模式

- **回测模式**：使用历史数据，验证策略
- **实盘模式**：实时交易，接收真实行情

### 三种运行机制

```
handlebar  - 逐K线驱动（最常用）
subscribe  - 事件驱动（分笔推送）
run_time   - 定时任务（固定间隔）
```

### 关键上下文对象（ContextInfo对象）

```python
C.stockcode       # 股票代码部分（如'600000'）
C.market          # 市场代码（'SH'或'SZ'）
C.period          # K线周期（'1d', '5m'等）
C.barpos          # 当前K线位置
C.is_last_bar()   # 是否最后一根K线

# 数据处理
C.get_market_data_ex()
C.get_full_tick()
C.get_bar_timetag()

# 绘图
C.draw_text()
```

---

## 📊 SKILL库规模

| 指标 | 数值 |
|------|------|
| 文档总数 | **12个** |
| 总字数 | **~50,000字** |
| 代码示例 | **4个完整策略** |
| 代码行数 | **1500+ 行** |
| 函数覆盖 | **所有主要函数** |
| 最佳实践 | **50+ 条** |
| 常见问题 | **30+ 项** |

---

## ⚡ 快速参考

### 最常用的函数

```python
# 获取历史数据
data = C.get_market_data_ex(['close'], [stock], count=100, subscribe=False)

# 获取最新行情
tick = C.get_full_tick([stock])

# 下单
passorder(23, 1101, account, stock, 14, -1, 100, C)

# 查询账户
account = get_trade_detail_data(account, 'stock', 'account')

# 查询持仓
holds = get_trade_detail_data(account, 'stock', 'position')

# 查询成交
deals = get_trade_detail_data(account, 'stock', 'deal')
```

### 最常见的问题

| 问题 | 查看文件 |
|------|---------|
| 如何回测? | [backtesting-guide.md](./backtesting-guide.md) |
| 如何实盘? | [live-trading-guide.md](./live-trading-guide.md) |
| 如何获取数据? | [market-data-api.md](./market-data-api.md) |
| 如何下单? | [trading-api.md](./trading-api.md) |
| 回测和实盘的区别? | [overview.md](./overview.md) |
| 三种运行机制的区别? | [execution-mechanisms.md](./execution-mechanisms.md) |
| 如何优化性能? | [best-practices.md](./best-practices.md) |

---

## 🎓 推荐阅读顺序

### 第一天 (入门)
1. README.md (10分钟)
2. overview.md (15分钟)
3. execution-mechanisms.md (20分钟)

### 第二天 (选择路径)
1. 选择你的场景对应指南 (30-40分钟)
2. 查看对应的示例代码 (20分钟)

### 第三天 (深入学习)
1. 查询相关API文档 (20分钟)
2. 学习best-practices.md (25分钟)
3. 开始编写你的策略

---

## 💡 使用建议

### ✅ 推荐做法

- 📖 完整读一遍对应的指南
- 💻 运行示例代码，理解原理
- 🛡️ 先回测验证，再实盘交易
- 🔍 经常查阅API文档
- 📝 遵循最佳实践编写代码

### ❌ 不推荐做法

- ❌ 跳过概念，直接抄代码
- ❌ 混淆回测和实盘参数
- ❌ 忽视错误处理和风险管理
- ❌ 未测试就用真实资金交易
- ❌ 忽视编码规范

---

## 🔗 相关链接

- 📱 [QMT官方网站](http://www.thinktrader.net/)
- 📚 [官方知识库](https://dict.thinktrader.net/)
- 💬 [迅投社区](https://xuntou.net/)

---

## 📝 版本信息

- **SKILL库名称**: iQuant QMT Python SKILL
- **版本**: 1.0
- **更新日期**: 2026年3月13日
- **覆盖范围**: QMT 2024+ 版本
- **状态**: 完整可用 ✅

---

## 🎯 现在就开始

👇 选择你要做的事情：

### 我想从头学起
→ 打开 [README.md](./README.md)

### 我想快速上手
→ 打开 [INDEX.md](./INDEX.md)

### 我想看代码示例
→ 打开 [examples/](./examples/) 目录

### 我想查API文档
→ 打开 [market-data-api.md](./market-data-api.md) 或 [trading-api.md](./trading-api.md)

### 我想学最佳实践
→ 打开 [best-practices.md](./best-practices.md)

---

**祝你使用愉快！如有任何问题，请参考本库的各个模块。** 🚀

