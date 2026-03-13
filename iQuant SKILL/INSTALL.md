# QMT Python策略开发SKILL - 安装完成 ✅

## 📦 SKILL安装信息

| 项目 | 值 |
|------|-----|
| **SKILL名称** | QMT Python策略开发SKILL库 |
| **版本** | 1.0.0 |
| **安装位置** | `c:\Users\Administrator\Desktop\iQuant SKILL\` |
| **状态** | ✅ 已安装 |
| **主入口** | [SKILL.md](SKILL.md) |

## 📂 已安装组件

### 核心模块 (7个)
- ✅ [overview.md](qmt-skill/overview.md) - QMT系统概述
- ✅ [execution-mechanisms.md](qmt-skill/execution-mechanisms.md) - 三大执行机制
- ✅ [backtesting-guide.md](qmt-skill/backtesting-guide.md) - 回测指南
- ✅ [live-trading-guide.md](qmt-skill/live-trading-guide.md) - 实盘指南
- ✅ [market-data-api.md](qmt-skill/market-data-api.md) - 行情API
- ✅ [trading-api.md](qmt-skill/trading-api.md) - 交易API
- ✅ [best-practices.md](qmt-skill/best-practices.md) - 最佳实践

### 代码示例 (4个)
- ✅ [examples/backtest.md](qmt-skill/examples/backtest.md) - 双均线回测策略 (600+行)
- ✅ [examples/live-trading.md](qmt-skill/examples/live-trading.md) - 双均线实盘策略 (500+行)
- ✅ [examples/subscribe.md](qmt-skill/examples/subscribe.md) - 事件驱动策略 (400+行)
- ✅ [examples/run-time.md](qmt-skill/examples/run-time.md) - 定时器策略 (500+行)

### 导航文件 (3个)
- ✅ [SKILL.md](SKILL.md) - **SKILL主配置文件** ⭐
- ✅ [QuickStart.md](QuickStart.md) - 快速开始指南
- ✅ [qmt-skill/INDEX.md](qmt-skill/INDEX.md) - 完整导航索引

## 🚀 接下来做什么

### 方式1️⃣: 立即开始学习
```
1. 打开 QuickStart.md - 了解项目概要
2. 按照推荐路径选择一条学习路径
3. 阅读对应模块
4. 运行代码示例
```

### 方式2️⃣: 在Copilot中使用
```
- 在Chat中提到"QMT"相关问题时，会自动引用本SKILL
- 可以直接问"如何用QMT实现...?"
- Copilot会搜索相关模块并提供答案
```

### 方式3️⃣: 复制代码到项目
```
1. 打开 qmt-skill/examples/ 中的任一示例
2. 复制代码到你的QMT策略文件
3. 根据 best-practices.md 调整参数
4. 在QMT中运行
```

## 📋 SKILL使用检查清单

启动使用前，请确认：

### 第一次使用
- [ ] 已找到 SKILL.md (主配置文件)
- [ ] 已浏览 QuickStart.md (入门指南)
- [ ] 已打开 qmt-skill/INDEX.md (完整导航)

### 选择学习路径
- [ ] 新手? → 选择"路径1️⃣-回测" 
- [ ] 想升级? → 选择"路径2️⃣-实盘"
- [ ] 高频交易? → 选择"路径3️⃣-订阅"
- [ ] 监控系统? → 选择"路径4️⃣-定时"

### 使用代码示例
- [ ] 选好对应的示例文件
- [ ] 复制代码到你的QMT策略
- [ ] 修改必要的参数（股票代码、手数等）
- [ ] 参考 best-practices.md 优化代码

### 遇到问题
- [ ] 查看对应模块末尾的"常见问题"部分
- [ ] 参考 trading-api.md 或 market-data-api.md 的错误代码
- [ ] 检查 best-practices.md 的相关最佳实践

## 💡 快速参考

### 文件位置速查

| 我想... | 查看文件 |
|--------|--------|
| 了解QMT基础 | [overview.md](qmt-skill/overview.md) |
| 选择执行机制 | [execution-mechanisms.md](qmt-skill/execution-mechanisms.md) |
| 进行回测 | [backtesting-guide.md](qmt-skill/backtesting-guide.md) + [examples/backtest.md](qmt-skill/examples/backtest.md) |
| 做实盘交易 | [live-trading-guide.md](qmt-skill/live-trading-guide.md) + [examples/live-trading.md](qmt-skill/examples/live-trading.md) |
| 查找函数用法 | [market-data-api.md](qmt-skill/market-data-api.md) 或 [trading-api.md](qmt-skill/trading-api.md) |
| 优化我的代码 | [best-practices.md](qmt-skill/best-practices.md) |
| 查看所有文件 | [qmt-skill/INDEX.md](qmt-skill/INDEX.md) |

### 核心代码模板速查

**行情数据获取**
```python
# 从本地获取(回测)
df = C.get_market_data_ex(['close'], ['000001.SZ'], subscribe=False)

# 订阅服务器(实盘)
df = C.get_market_data_ex(['close'], ['000001.SZ'], subscribe=True)
```

**下单**
```python
passorder(23, '0', account, '000001.SZ', '0', 10.5, 100, quicktrade=2)
```

**查询持仓**
```python
positions = get_trade_detail_data('positions', account, 'all')
```

## 📂 完整项目树

```
c:\Users\Administrator\Desktop\iQuant SKILL\
│
├── SKILL.md                             ⭐ SKILL主配置文件
├── INSTALL.md                           ← 你在这里
├── QuickStart.md                        ← 快速开始
├── CHECKLIST.md                         ← 项目验收
│
└── qmt-skill/
    ├── README.md                        ← 项目文档
    ├── INDEX.md                         ← 导航索引
    ├── SUMMARY.md                       ← 项目总结
    │
    ├── overview.md                      (3000字)
    ├── execution-mechanisms.md          (5000字)
    ├── backtesting-guide.md             (6000字)
    ├── live-trading-guide.md            (7000字)
    ├── market-data-api.md               (5000字)
    ├── trading-api.md                   (5000字)
    ├── best-practices.md                (6000字)
    │
    └── examples/
        ├── backtest.md                  (600+行)
        ├── live-trading.md              (500+行)
        ├── subscribe.md                 (400+行)
        └── run-time.md                  (500+行)
```

## 🎊 安装完成！

**现在你可以：**

1. ✅ 立即开始学习 QMT Python 开发
2. ✅ 复制完整的、经过验证的代码示例
3. ✅ 快速查找API函数和用法
4. ✅ 参考最佳实践优化你的策略
5. ✅ 在Copilot中获得相关的建议和指导

---

**提示**: 第一次使用请打开 [QuickStart.md](QuickStart.md) 或 [SKILL.md](SKILL.md)

**版本**: 1.0.0 安装版 | **安装日期**: 2026年3月13日 | **状态**: ✅ 就绪
