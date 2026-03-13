# QMT Python SKILL 完整知识库

## 📚 本SKILL库介绍

这是一个**完整的、模块化的QMT Python知识库**，基于迅投QMT内置Python环境的官方文档整理而成。

**目的**：为QMT炒股软件的Python策略开发者提供详细的编码规范、最佳实践和完整的代码示例。

---

## 🗂️ 项目结构

```
qmt-skill/
├── INDEX.md                          ← 总索引（从这里开始）
├── overview.md                       ← 系统概述
├── execution-mechanisms.md           ← 三种运行机制详解
├── backtesting-guide.md              ← 回测完全指南
├── live-trading-guide.md             ← 实盘交易完全指南
├── market-data-api.md                ← 行情数据API参考
├── trading-api.md                    ← 交易函数API参考
├── best-practices.md                 ← 编码规范与最佳实践
│
└── examples/                         ← 代码示例集合
    ├── backtest.md                   ← 回测完整示例
    ├── live-trading.md               ← 实盘完整示例
    ├── subscribe.md                  ← 事件驱动示例
    └── run-time.md                   ← 定时任务示例
```

---

## 🚀 快速开始

### 对于初学者

**推荐学习路径**：

1. **第一步**：[系统概述](./overview.md)
   - 了解QMT系统的基本概念
   - 理解两种交易模式（回测/实盘）

2. **第二步**：[运行机制详解](./execution-mechanisms.md)
   - 理解三种运行机制
   - 选择适合的机制

3. **第三步**：选择你的场景
   - **想要回测？** → [回测模型指南](./backtesting-guide.md) + [回测示例](./examples/backtest.md)
   - **想要实盘？** → [实盘交易指南](./live-trading-guide.md) + [实盘示例](./examples/live-trading.md)

4. **第四步**：学习API
   - [市场数据API](./market-data-api.md) - 如何获取行情
   - [交易函数API](./trading-api.md) - 如何下单

5. **第五步**：查看示例代码
   - [examples/](./examples/) 目录有完整可运行的示例

### 对于有经验的开发者

- **跳转到** [最佳实践](./best-practices.md)
- 快速参考 [市场数据API](./market-data-api.md) 和 [交易函数API](./trading-api.md)
- 查看对应场景的 [示例代码](./examples/)

---

## 📖 核心模块介绍

### 1️⃣ 系统概述 ([overview.md](./overview.md))
- QMT系统简介与核心功能
- 回测模型工作原理
- 实盘模型工作原理
- 适用场景判断

**适合人群**：所有新手必读

### 2️⃣ 运行机制详解 ([execution-mechanisms.md](./execution-mechanisms.md))
- **逐K线驱动（handlebar）**
  - 回测模式工作原理
  - 实盘逐K线模式
  - 完整代码框架
  
- **事件驱动（subscribe）**
  - 分笔推送机制
  - 回调函数编写
  - 高频交易应用
  
- **定时任务（run_time）**
  - 时间触发机制
  - 定时函数编写
  - 监控应用

**适合人群**：想要理解运行流程的开发者

### 3️⃣ 回测模型指南 ([backtesting-guide.md](./backtesting-guide.md))
- 数据准备与下载
- 回测参数配置
- 撮合规则详解
- 代码实现步骤
- 结果分析方法
- 常见问题解决

**适合人群**：想要进行历史回测的开发者

### 4️⃣ 实盘交易指南 ([live-trading-guide.md](./live-trading-guide.md))
- 账号配置与文档
- 两种委托模式
  - 逐K线模式（等待K线完成）
  - 立即下单模式（立刻执行）
- 委托管理与查询
- 风险控制
- 常见错误与解决

**适合人群**：准备进行实盘交易的开发者

### 5️⃣ 市场数据API ([market-data-api.md](./market-data-api.md))
- `get_market_data_ex` - 历史数据获取
- `get_full_tick` - 最新行情获取
- `subscribe_quote` - 行情订阅
- `get_last_volume` - 成交量查询
- `get_stock_list_in_sector` - 板块选股
- 性能优化建议

**适合人群**：需要查询行情数据的开发者

### 6️⃣ 交易函数API ([trading-api.md](./trading-api.md))
- `passorder` - 下单函数详解
  - 参数说明
  - 使用示例
  - 错误处理
  
- `get_trade_detail_data` - 数据查询
  - 账户查询
  - 持仓查询
  - 成交查询
  - 委托查询

**适合人群**：需要下单和查询交易数据的开发者

### 7️⃣ 编码规范与最佳实践 ([best-practices.md](./best-practices.md))
- 文件编码与缩进规范
- 代码结构最佳实践
- 性能优化建议
- 风险管理实现
- 调试与日志记录
- 测试验证方法
- 常见陷阱避坑

**适合人群**：想要写出高质量代码的开发者

---

## 💻 代码示例

### 示例1：回测示例 ([examples/backtest.md](./examples/backtest.md))
**双均线回测策略**
- 完整的回测代码
- 参数配置说明
- 运行步骤
- 输出分析

```python
#coding:gbk
def init(C):
    C.stock = C.stockcode + '.' + C.market
    C.line1 = 10  # 快线周期
    C.line2 = 20  # 慢线周期

def handlebar(C):
    # 获取历史数据
    data = C.get_market_data_ex(['close'], [C.stock], count=max(C.line1, C.line2), subscribe=False)
    # 计算均线并交易...
```

### 示例2：实盘示例 ([examples/live-trading.md](./examples/live-trading.md))
**双均线实盘策略（逐K线模式）**
- 完整的实盘代码
- 账户管理
- 委托查询
- 风险控制

### 示例3：事件驱动示例 ([examples/subscribe.md](./examples/subscribe.md))
**基于分笔推送的涨停追买策略**
- 订阅回调函数
- 实时行情处理

### 示例4：定时任务示例 ([examples/run-time.md](./examples/run-time.md))
**市场加权涨幅监控**
- 定时函数实现
- 市场分析

---

## 🔑 关键概念速览

### 编码规范
```python
#coding:gbk  # ← 必须在第一行

import pandas as pd
import numpy as np

def init(C):
    pass

def handlebar(C):
    pass
```

### 回测 vs 实盘
| 方面 | 回测 | 实盘 |
|------|------|------|
| subscribe参数 | False | True |
| 数据源 | 本地历史 | 实时推送 |
| 交易所 | 虚拟撮合 | 真实交易 |
| 发单模式 | 无需等待 | 逐K线/立即 |

### 三种运行机制
```
handlebar  - 逐K线驱动（回测推荐，实盘支持）
subscribe  - 事件驱动（分笔推送）
run_time   - 定时任务（固定间隔）
```

### 委托模式
```
quicktrade=0  - 逐K线模式（等待K线完成，用ContextInfo保存状态）
quicktrade=2  - 立即下单模式（立刻执行，用全局变量保存状态）
```

---

## 🎯 常见开发场景

### 场景1：我想验证一个策略的历史表现
**推荐路径**：
1. [回测模型指南](./backtesting-guide.md) - 学习回测流程
2. [回测示例](./examples/backtest.md) - 参考完整代码
3. [市场数据API](./market-data-api.md) - 查询数据获取方法

### 场景2：我想部署一个实盘交易策略
**推荐路径**：
1. [系统概述](./overview.md) - 理解基本概念
2. [实盘交易指南](./live-trading-guide.md) - 学习实盘流程
3. [实盘示例](./examples/live-trading.md) - 参考完整代码
4. [最佳实践](./best-practices.md) - 风险管理

### 场景3：我想写高效的分笔级别策略
**推荐路径**：
1. [运行机制详解](./execution-mechanisms.md#二事件驱动subscribe-订阅推送) - 理解机制
2. [事件驱动示例](./examples/subscribe.md) - 参考代码
3. [最佳实践](./best-practices.md#性能优化建议) - 性能优化

### 场景4：我想定时监控市场状态
**推荐路径**：
1. [运行机制详解](./execution-mechanisms.md#三定时任务run_time-定时运行) - 理解机制
2. [定时任务示例](./examples/run-time.md) - 参考代码

---

## ⚠️ 重要提示

### 编码规范必须遵守
```python
#coding:gbk  # ← 放在文件第一行，必须！
```

### 回测和实盘的关键区别
```python
# 回测中
data = C.get_market_data_ex(..., subscribe=False)  # False！

# 实盘中
data = C.get_market_data_ex(..., subscribe=True)   # True！
```

### 委托数量必须是100的倍数
```python
# ❌ 错误
vol = 150  # 不是100的倍数

# ✅ 正确
vol = int(cash / price / 100) * 100
```

### 持仓管理方式取决于委托模式
```python
# 逐K线模式（quicktrade=0）
class ContextInfo:
    hold_vol = 0  # 保存在 C 对象中

# 立即下单模式（quicktrade=2）
class GlobalState:
    hold_vol = 0  # 保存在全局变量中
```

---

## 🔗 相关资源

### 官方文档
- [迅投QMT官方网站](http://www.thinktrader.net/)
- [完整知识库](https://dict.thinktrader.net/)

### 社区与支持
- [迅投社区](https://xuntou.net/)
- 微信扫码联系客服

---

## 📚 学习进度跟踪

建议按照以下步骤学习：

- [ ] 阅读 [系统概述](./overview.md)
- [ ] 阅读 [运行机制详解](./execution-mechanisms.md)
- [ ] 选择你的场景：
  - [ ] 回测：[回测模型指南](./backtesting-guide.md) + [示例](./examples/backtest.md)
  - [ ] 实盘：[实盘交易指南](./live-trading-guide.md) + [示例](./examples/live-trading.md)
  - [ ] 高频：[事件驱动示例](./examples/subscribe.md)
  - [ ] 定时：[定时任务示例](./examples/run-time.md)
- [ ] 学习相关API：
  - [ ] [市场数据API](./market-data-api.md)
  - [ ] [交易函数API](./trading-api.md)
- [ ] 学习 [最佳实践](./best-practices.md)
- [ ] 编写你的第一个策略

---

## 💡 使用建议

### ✅ 做这些事

- 📖 完整阅读 [系统概述](./overview.md)
- 🔍 根据场景选择对应模块
- 📝 参考示例代码编写策略
- ✅ 先回测验证，再实盘交易
- 🛡️ 充分考虑风险管理

### ❌ 不要做这些事

- ❌ 跳过规范直接开始编码
- ❌ 混淆回测和实盘的参数
- ❌ 忽视数据检查和异常处理
- ❌ 直接使用网络代码，不理解原理
- ❌ 一上来就下大单，没有充分测试

---

## 📞 获取帮助

- 💬 有问题？查看 [常见问题](./best-practices.md#常见陷阱)
- 🐛 遇到错误？查看 [常见错误与解决](./trading-api.md#常见错误与解决)
- 📚 需要API文档？查看 [市场数据API](./market-data-api.md) 或 [交易函数API](./trading-api.md)
- 🎓 需要学习示例？查看 [示例代码](./examples/)

---

## 📝 许可证与声明

**本SKILL库声明**：
- 本库基于迅投QMT官方文档整理
- 用于学习和参考目的
- 所有示例代码仅供参考，使用前需充分测试
- 使用本库中的代码进行交易产生的损失，使用者自行承担

---

**最后更新**：2026年3月13日

**SKILL库版本**：1.0

---

## 🎯 快速导航

| 我想... | 去哪里 |
|--------|--------|
| 了解QMT系统 | [系统概述](./overview.md) |
| 学习三种运行机制 | [运行机制详解](./execution-mechanisms.md) |
| 进行系统回测 | [回测模型指南](./backtesting-guide.md) |
| 部署实盘交易 | [实盘交易指南](./live-trading-guide.md) |
| 查询行情数据 | [市场数据API](./market-data-api.md) |
| 下单交易 | [交易函数API](./trading-api.md) |
| 学习最佳实践 | [最佳实践](./best-practices.md) |
| 看代码示例 | [示例代码](./examples/) |
| 查看索引 | [总索引](./INDEX.md) |

---

**开始学习**：从 [INDEX.md](./INDEX.md) 开始，或根据你的需求选择对应模块！

