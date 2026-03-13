# QMT 系统概述

## 📋 QMT极速策略交易系统概览

**QMT（极速策略交易系统）** 是一个内置了Python 3.6环境的量化交易平台，提供行情数据与交易下单两大核心功能。

### 核心特性

#### 1. 内置Python环境
- **版本**：Python 3.6
- **支持库**：pandas、numpy、talib 等常用量化分析库
- **编码**：使用GBK编码

#### 2. 两大核心功能
- **行情数据**：实时获取与历史数据回溯
- **交易下单**：接入交易所，实现实时交易

#### 3. 应用场景
- ✅ 指标计算
- ✅ 策略编写
- ✅ 策略回测
- ✅ 实盘下单

---

## 🎯 两种交易模式

### 1. 回测模型

**定义**：遍历历史K线数据，模拟交易过程

#### 特点
- 使用本地历史数据
- 无需向服务器订阅实时行情
- 速度快，适合策略优化
- 可得到策略的历史表现

#### 工作流程
```
1. 下载历史行情数据（数据管理）
    └─ 选择周期（日线、周线等）
    └─ 选择板块（沪深A股等）
    └─ 选择时间范围（全部）

2. 配置回测参数
    └─ 设置默认周期
    └─ 设置默认主图
    └─ 配置资金账号

3. 回测执行
    └─ 副图模式运行（必须）
    └─ 得到历史净值走势
```

#### 撮合规则
- 指定价格在当前K线高低点间 → 按指定价格撮合
- 指定价格超过高低点范围 → 按当前K线收盘价撮合
- 委托数量大于可用数量 → 按可用数量撮合

### 2. 实盘模型

**定义**：在盘中接收最新行情，实时发送交易信号

#### 特点
- 接收未来K线数据
- 实时生成策略信号
- 实时下单到交易所
- 支持模拟和真实交易

#### 两种账号类型
- **模拟账号**：使用QMT模拟柜台
- **真实账号**：连接交易所真实柜台

#### 撮合规则
- 价格笼子限制（股票品种）：价格不能超过当前价2%
- 数量限制：超过可用数量时废单

---

## ⚙️ 三种运行机制

### 1. 逐K线驱动（handlebar）
```python
def handlebar(C):
    # 每根K线触发一次
    pass
```

- **回测**：历史K线从左向右逐根触发
- **实盘**：盘中分笔数据到达时触发，满足时间间隔则进行一次交易
- **适用**：需要模拟历史K线效果或逐K线交易

### 2. 事件驱动（subscribe）
```python
C.subscribe_quote(stock, callback=callback_func)
```

- **触发**：新分笔数据到达时触发回调
- **适用**：分笔级别的实时交易
- **场景**：高频或需要分笔数据的策略

### 3. 定时任务（run_time）
```python
C.run_time("function_name", "1nSecond", "2019-10-14 13:20:00")
```

- **触发**：按固定时间间隔触发
- **适用**：需要定时检查市场状态的策略
- **场景**：监控市场加权指数、定时调整持仓等

---

## 📊 运行机制对比

| 指标 | handlebar | subscribe | run_time |
|------|-----------|-----------|----------|
| **触发方式** | 逐K线 | 事件驱动 | 定时任务 |
| **回测支持** | ✅ 是 | ❌ 否 | ❌ 否 |
| **实盘支持** | ✅ 是 | ✅ 是 | ✅ 是 |
| **数据粒度** | K线 | 分笔 | 任意 |
| **使用场景** | 模拟K线或回测 | 分笔实时交易 | 定时监控交易 |
| **K线拼接** | 自动处理 | 需手动处理 | 需手动处理 |

---

## 🔧 核心函数简介

### 初始化函数
```python
def init(C):
    """
    策略初始化函数
    参数: C - ContextInfo对象，包含策略上下文信息
    """
    pass
```

### 行情数据获取
```python
# 获取历史行情数据（回测推荐）
data = C.get_market_data_ex(
    ['close', 'high', 'low', 'open'],  # 字段列表
    ['600000.SH'],                      # 品种列表
    end_time=bar_date,
    period='1d',
    count=100,
    subscribe=False                     # 回测时设为False
)

# 获取最新行情数据（实盘推荐）
tick = C.get_full_tick(['600000.SH'])
```

### 交易下单
```python
passorder(
    buyorsell,      # 23=买 24=卖（股票）
    price_type,     # 1101=市价
    account,        # 账号
    stock,          # 品种
    order_type,     # 14=普通下单
    stop_price,     # 止损价 -1=不设置
    order_vol,      # 数量
    [strategy_name, quicktrade, remark, C]  # 可选参数
)
```

### 获取交易数据
```python
# 获取账户信息
account = get_trade_detail_data('account_name', 'STOCK', 'account')

# 获取持仓信息
positions = get_trade_detail_data('account_name', 'STOCK', 'position')

# 获取成交记录
deals = get_trade_detail_data('account_name', 'STOCK', 'deal')
```

---

## 📝 编码规范

### 必须事项
```python
#coding:gbk  # 放在文件第一行，指定编码为GBK

# 缩进统一使用 4个空格（或 ->）
# ✅ 正确
def init(C):
    C.stock = 'test'
    
# ❌ 错误（混合缩进）
def init(C):
  C.stock = 'test'    # 2个空格
```

### 导入常用库
```python
import pandas as pd
import numpy as np
import talib
import datetime
```

---

## 🚦 委托管理策略

### 逐K线模式（passorder quicktrade=0）
```python
# 使用ContextInfo对象保存状态
class ContextInfo:
    def __init__(self):
        self.holding = False       # 持仓状态
        self.entry_price = 0       # 入场价格
        self.latest_signal = None  # 最新信号
```

### 立即下单模式（passorder quicktrade=2）
```python
# 使用全局变量保存状态
class TradeState:
    def __init__(self):
        self.waiting_list = []     # 待查询委托列表
        self.bought_list = []      # 已买入列表

A = TradeState()  # 全局实例
```

---

## 💡 常见场景选择

### 场景1：历史策略回测
- ✅ 运行机制：**handlebar**
- ✅ 委托模式：逐K线模式
- ✅ 数据源：本地历史数据
- ✅ 信号处理：无需等待

### 场景2：盘中模拟K线交易
- ✅ 运行机制：**handlebar**
- ✅ 委托模式：逐K线模式
- ✅ 数据源：实时分笔
- ✅ 信号处理：按K线周期等待

### 场景3：分笔级别实时交易
- ✅ 运行机制：**subscribe**
- ✅ 委托模式：立即下单模式
- ✅ 数据源：实时分笔推送
- ✅ 信号处理：立即响应

### 场景4：定时监控市场
- ✅ 运行机制：**run_time**
- ✅ 委托模式：立即下单模式
- ✅ 数据源：定时查询
- ✅ 信号处理：定时处理

---

## 📚 下一步

选择对应的模块继续学习：

1. **了解运行机制** → [执行机制详解](./execution-mechanisms.md)
2. **开始回测** → [回测模型指南](./backtesting-guide.md)
3. **进行实盘** → [实盘交易指南](./live-trading-guide.md)
4. **查询API** → [市场数据API](./market-data-api.md) / [交易API](./trading-api.md)
5. **查看示例** → [代码示例](./examples/)

