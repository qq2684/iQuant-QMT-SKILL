---
name: "QMT Python策略开发SKILL"
type: skill
description: "迅投QMT内置Python知识库 - 完整的策略开发指南、API参考和代码示例"
version: "1.0.0"
author: "QMT知识库"
tags: ["QMT", "策略开发", "Python", "回测", "实盘交易", "量化交易"]
---

# QMT Python策略开发 SKILL库

这是一个完整的QMT（迅投极速策略交易系统）Python开发SKILL库，包含系统概述、三大执行机制、完整的回测和实盘指南、API参考，以及即插即用的代码示例。

## 📚 核心模块

### 基础学习
- **[QMT系统概述](qmt-skill/overview.md)** - 了解QMT系统架构、两种交易模式和基本概念
- **[三大执行机制](qmt-skill/execution-mechanisms.md)** - handlebar（K线驱动）、subscribe（事件驱动）、run_time（定时器）

### 实现指南
- **[回测完全指南](qmt-skill/backtesting-guide.md)** - 从零开始进行历史数据回测
- **[实盘交易指南](qmt-skill/live-trading-guide.md)** - 部署实时策略和风险管理

### API参考
- **[行情数据API](qmt-skill/market-data-api.md)** - 所有市场数据获取函数
- **[交易API](qmt-skill/trading-api.md)** - 下单、查询、委托管理函数

### 高级主题
- **[最佳实践](qmt-skill/best-practices.md)** - 50+个编码规范、优化技巧和风险控制模式

## 💡 代码示例

四个完整、可运行的策略示例：

| 示例 | 执行机制 | 难度 | 文件 |
|------|--------|------|------|
| 双均线回测策略 | handlebar | ⭐⭐ | [examples/backtest.md](qmt-skill/examples/backtest.md) |
| 双均线实盘策略 | handlebar | ⭐⭐⭐ | [examples/live-trading.md](qmt-skill/examples/live-trading.md) |
| 事件驱动策略 | subscribe | ⭐⭐⭐ | [examples/subscribe.md](qmt-skill/examples/subscribe.md) |
| 定时器策略 | run_time | ⭐⭐ | [examples/run-time.md](qmt-skill/examples/run-time.md) |

## 🎯 学习路径

### 路径1️⃣ - 新手：从回测开始
```
overview.md 
  ↓
backtesting-guide.md 
  ↓
examples/backtest.md (复制代码运行)
  ↓
best-practices.md (优化代码)
```

### 路径2️⃣ - 中级：升级到实盘
```
overview.md 
  ↓
execution-mechanisms.md (理解handlebar)
  ↓
live-trading-guide.md 
  ↓
examples/live-trading.md (学习风险管理)
```

### 路径3️⃣ - 高级：事件驱动交易
```
execution-mechanisms.md (理解subscribe)
  ↓
examples/subscribe.md (三个完整策略)
  ↓
best-practices.md (性能优化)
```

### 路径4️⃣ - 监控系统：定时任务
```
execution-mechanisms.md (理解run_time)
  ↓
examples/run-time.md (三个监控示例)
```

## 📖 文档统计

| 类别 | 数量 | 内容 |
|------|------|------|
| **核心模块** | 7个 | ~36,000字 |
| **代码示例** | 4个 | 1500+行Python代码 |
| **最佳实践** | 50+ | 编码规范、优化、风险控制 |
| **API函数** | 12+ | 详细参考和示例 |

## ⚡ 快速命令

使用以下方式快速访问：

```
# 查看完整导航
./qmt-skill/INDEX.md

# 查看项目总结
./qmt-skill/SUMMARY.md

# 开始学习
./QuickStart.md
```

## 🔧 关键概念速记

| 概念 | 说明 |
|------|------|
| **编码** | 所有文件必须 `#coding:gbk` |
| **单位** | 最小100股 |
| **handlebar** | K线完成后执行（推荐回测），支持实盘 |
| **subscribe** | 实时Tick触发（仅实盘），适合高频 |
| **run_time** | 定时触发（如每分钟一次），用于监控 |
| **quicktrade** | 0=K线模式(等待), 2=立即模式(马上执行) |
| **account** | 交易账户对象，包含持仓、委托等信息 |

## 📝 关键参数速查

### 获取行情数据
```python
# 回测：本地数据
df = C.get_market_data_ex(['close', 'high', 'low'], stock_list, subscribe=False)

# 实盘：服务器订阅
df = C.get_market_data_ex(['close', 'high', 'low'], stock_list, subscribe=True)
```

### 下单
```python
# 买入股票（23）：立即模式，限价单
passorder(23, '0', account, '000001.SZ', '0', 10.5, 100, quicktrade=2)

# 卖出股票（24）：K线模式
passorder(24, '0', account, '000001.SZ', '0', 10.5, 100, quicktrade=0)
```

### 查询
```python
# 账户持仓
positions = get_trade_detail_data('positions', account, 'all')

# 委托单
orders = get_trade_detail_data('orders', account, 'all')

# 成交单
deals = get_trade_detail_data('deals', account, 'all')
```

## ✅ 验证清单

安装完成后，请确认：

- [ ] 已阅读 QuickStart.md
- [ ] 已审查 qmt-skill/overview.md
- [ ] 已查看相关的执行机制说明
- [ ] 已测试 examples/ 中的代码示例
- [ ] 已参考 best-practices.md 检查代码规范

## 📞 使用建议

1. **第一次使用**：从 [QuickStart.md](QuickStart.md) 开始
2. **查找功能**：使用 [INDEX.md](qmt-skill/INDEX.md) 快速查找
3. **学习策略**：选择上述四条学习路径之一
4. **编写代码**：参考 [examples/](qmt-skill/examples/) 中的示例
5. **优化性能**：查阅 [best-practices.md](qmt-skill/best-practices.md)
6. **遇到问题**：查看各模块末尾的疑难解答部分

## 📂 项目结构

```
qmt-skill/
├── README.md                    ← 项目主文档
├── INDEX.md                     ← 完整导航
├── SUMMARY.md                   ← 项目总结
│
├── 【7个核心学习模块】
├── overview.md
├── execution-mechanisms.md
├── backtesting-guide.md
├── live-trading-guide.md
├── market-data-api.md
├── trading-api.md
├── best-practices.md
│
└── examples/                    ← 4个完整可运行示例
    ├── backtest.md
    ├── live-trading.md
    ├── subscribe.md
    └── run-time.md
```

---

**版本**: 1.0.0 | **最后更新**: 2026年3月13日 | **状态**: ✅ 完整
