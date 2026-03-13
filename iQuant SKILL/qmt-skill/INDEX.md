# QMT Python SKILL 知识库总索引

## 📚 SKILL 模块导航

本SKILL库基于迅投QMT内置Python知识库整理，提供完整的QMT策略编写指南。

### 核心模块

#### 1. **系统概述** - [overview.md](./overview.md)
- QMT系统简介
- 内置Python环境说明
- 核心功能介绍

#### 2. **运行机制详解** - [execution-mechanisms.md](./execution-mechanisms.md)
- 逐K线驱动（handlebar）
- 事件驱动（subscribe）
- 定时任务（run_time）
- 机制对比与应用场景

#### 3. **回测模型指南** - [backtesting-guide.md](./backtesting-guide.md)
- 回测流程与配置
- 数据准备
- 撮合规则
- 常见注意事项

#### 4. **实盘交易指南** - [live-trading-guide.md](./live-trading-guide.md)
- 实盘模式与配置
- 两种交易模式（逐K线/立即下单）
- 配置账号
- 风险管理

#### 5. **市场数据API** - [market-data-api.md](./market-data-api.md)
- 行情数据获取函数
- 数据结构说明
- 订阅与推送机制
- 性能优化

#### 6. **交易函数API** - [trading-api.md](./trading-api.md)
- 下单函数 `passorder`
- 交易函数参数详解
- 下单代码说明
- 成交回报处理

#### 7. **编码规范与最佳实践** - [best-practices.md](./best-practices.md)
- 编码规范要求
- 性能优化建议
- 常见错误与解决方案
- 调试技巧

### 代码示例

#### 8. **回测示例** - [examples/backtest.md](./examples/backtest.md)
- 双均线回测策略完整示例
- 回测参数配置
- 数据获取与处理

#### 9. **实盘示例** - [examples/live-trading.md](./examples/live-trading.md)
- 双均线实盘策略完整示例
- handlebar机制实现
- 委托管理

#### 10. **事件驱动示例** - [examples/subscribe.md](./examples/subscribe.md)
- subscribe订阅回调示例
- 行情推送处理

#### 11. **定时任务示例** - [examples/run-time.md](./examples/run-time.md)
- run_time定时运行示例
- 市场加权涨幅计算

---

## 🚀 快速开始

### 第一步：理解系统
1. 阅读 [overview.md](./overview.md) 了解QMT系统基础
2. 阅读 [execution-mechanisms.md](./execution-mechanisms.md) 选择合适的运行机制

### 第二步：选择场景
- **用于回测**：阅读 [backtesting-guide.md](./backtesting-guide.md) + [examples/backtest.md](./examples/backtest.md)
- **用于实盘**：阅读 [live-trading-guide.md](./live-trading-guide.md) + [examples/live-trading.md](./examples/live-trading.md)

### 第三步：学习API
- 行情数据：[market-data-api.md](./market-data-api.md)
- 交易下单：[trading-api.md](./trading-api.md)

### 第四步：编写策略
- 参考 [examples/](./examples/) 目录的示例
- 遵循 [best-practices.md](./best-practices.md) 的规范

---

## ⚠️ 关键注意事项

### 编码规范
```python
#coding:gbk  # 必须在文件第一行
# 使用GBK编码
# 缩进统一使用 4个空格 或 ->
```

### 运行模式选择
| 场景 | 运行机制 | 适用情况 |
|------|--------|--------|
| 历史回测 | `handlebar` | 遍历历史K线 |
| 盘中模拟K线 | `handlebar` | 接收分笔并按K线处理 |
| 盘中实时交易 | `subscribe` | 分笔实时数据推送 |
| 固定间隔交易 | `run_time` | 定时执行策略 |

### 委托管理
- 逐K线模式（passorder quicktrade=0）：使用 `ContextInfo` 保存状态
- 立即下单模式（passorder quicktrade=2）：使用全局变量保存状态

---

## 📖 相关链接

- [迅投QMT官方网站](http://www.thinktrader.net/)
- [迅投知识库](https://dict.thinktrader.net/)
- [社区论坛](https://xuntou.net/)

---

## 📝 文档更新

本SKILL库基于QMT 2025年5月版本知识库整理。

最后更新：2026年3月13日

---

💡 **提示**：建议按照"快速开始"的步骤顺序阅读，避免跳跃式学习。
