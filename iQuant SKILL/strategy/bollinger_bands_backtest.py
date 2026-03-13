#coding:gbk

"""
布林带通道回测策略
==================
策略描述：
- 基于布林带（Bollinger Bands）的反向突破策略
- 中轨：N周期简单移动平均线
- 上轨：中轨 + K*标准差
- 下轨：中轨 - K*标准差
- 买入信号：价格下穿下轨时买入（价格过低）
- 卖出信号：价格上穿上轨时卖出（价格过高）

策略参数：
- period: 20 天（布林带计算周期）
- k_value: 2 （标准差倍数）

应用周期：日线
"""

# ===== 导入库 =====
import pandas as pd
import numpy as np
from datetime import datetime

# ===== 初始化函数 =====
def init(C):
    """
    策略初始化函数
    参数 C: ContextInfo 对象，包含策略的上下文信息
    """
    
    # 设置交易品种
    C.stock = C.stockcode + '.' + C.market
    print(f"设置交易品种: {C.stock}")
    
    # 设置策略参数
    C.bb_period = 20                # 布林带周期（日）
    C.bb_k = 2                      # 标准差倍数
    C.accountid = "backtest"        # 回测账号（任意字符串）
    
    # 初始化统计信息
    C.trade_count = 0               # 交易次数
    C.win_trades = 0                # 赢利交易次数
    C.total_profit = 0              # 总净利润
    C.last_buy_price = 0            # 最后一次买入价格
    
    # 持仓跟踪
    C.buy_positions = []            # 买入记录列表
    
    print(f"策略参数: 周期={C.bb_period}天, K值={C.bb_k}")
    print("策略初始化完成！")


def handlebar(C):
    """
    K线处理函数 - 每根K线触发一次
    在回测模式下，历史K线从左向右逐根遍历
    """
    
    # ========== 1. 获取当前K线时间 ==========
    bar_date = timetag_to_datetime(
        C.get_bar_timetag(C.barpos), 
        '%Y%m%d%H%M%S'
    )
    
    # ========== 2. 获取历史行情数据 ==========
    # 关键：回测中必须使用 subscribe=False
    local_data = C.get_market_data_ex(
        ['close'],                                  # 获取收盘价
        [C.stock],                                  # 交易品种
        end_time=bar_date,                          # 数据截止时间
        period=C.period,                            # K线周期
        count=C.bb_period + 5,                      # 多获取几根用于计算
        subscribe=False                             # ← 回测关键参数
    )
    
    # ========== 3. 提取收盘价列表 ==========
    close_list = list(local_data[C.stock].iloc[:, 0])
    
    # 检查数据长度
    if len(close_list) < C.bb_period:
        print(f"[{bar_date}] 行情数据不足（{len(close_list)}/{C.bb_period}），跳过处理")
        return
    
    # ========== 4. 计算布林带参数 ==========
    recent_closes = close_list[-C.bb_period:]
    
    # 中轨：简单移动平均线
    middle_band = round(np.mean(recent_closes), 2)
    
    # 标准差
    std_dev = round(np.std(recent_closes, ddof=1), 2)
    
    # 上轨：中轨 + K * 标准差
    upper_band = round(middle_band + C.bb_k * std_dev, 2)
    
    # 下轨：中轨 - K * 标准差
    lower_band = round(middle_band - C.bb_k * std_dev, 2)
    
    # 当前价格
    current_price = close_list[-1]
    
    # 前一根价格
    prev_price = close_list[-2] if len(close_list) >= 2 else current_price
    
    print(f"[{bar_date}] 价格:{current_price:.2f} | "
          f"上轨:{upper_band:.2f} | 中轨:{middle_band:.2f} | 下轨:{lower_band:.2f}")
    
    # ========== 5. 获取账户交易信息 ==========
    # 获取账户信息
    account = get_trade_detail_data(C.accountid, 'stock', 'account')
    if not account or len(account) == 0:
        print(f"[{bar_date}] 账户获取失败")
        return
    
    account = account[0]
    available_cash = int(account.m_dAvailable)
    account_balance = int(account.m_dBalance)
    
    # 获取持仓信息
    holdings = get_trade_detail_data(C.accountid, 'stock', 'position')
    holdings_dict = {
        f'{i.m_strInstrumentID}.{i.m_strExchangeID}': i.m_nVolume 
        for i in holdings
    }
    
    holding_vol = holdings_dict.get(C.stock, 0)
    
    # ========== 6. 计算交易数量 ==========
    # 每手最少100股，计算能买多少手
    vol = int(available_cash / current_price / 100) * 100
    
    # ========== 7. 交易逻辑 - 买入信号 ==========
    # 条件1：当前未持仓
    # 条件2：价格从上方下穿下轨（价格过低，值得买入）
    if holding_vol == 0 and prev_price > lower_band and current_price <= lower_band:
        if vol >= 100 and available_cash > 0:
            print(f"[{bar_date}] ★★★ 买入信号 - 价格下穿下轨")
            print(f"       当前价:{current_price:.2f} | 下轨:{lower_band:.2f}")
            
            # 下单（市价单买入）
            passorder(
                23,                 # 23=买入
                1101,               # 市价单
                C.accountid,        # 账号
                C.stock,            # 品种
                5,                  # 订单类型
                -1,                 # 止价（-1表示不设置）
                vol,                # 数量
                C                   # ContextInfo对象
            )
            
            C.trade_count += 1
            C.last_buy_price = current_price
            C.buy_positions.append({
                'date': bar_date,
                'price': current_price,
                'volume': vol
            })
            
            print(f"       成功下单 - 买入 {vol} 股 @ {current_price:.2f}")
            
            # 绘制买入标记
            C.draw_text(1, 1, '买')
    
    # ========== 8. 交易逻辑 - 卖出信号 ==========
    # 条件1：当前持仓中
    # 条件2：价格从下方上穿上轨（价格过高，应该卖出获利）
    elif holding_vol > 0 and prev_price < upper_band and current_price >= upper_band:
        print(f"[{bar_date}] ★★★ 卖出信号 - 价格上穿上轨")
        print(f"       当前价:{current_price:.2f} | 上轨:{upper_band:.2f}")
        
        # 计算利润
        profit_per_share = current_price - C.last_buy_price
        total_profit = profit_per_share * holding_vol
        profit_rate = (profit_per_share / C.last_buy_price * 100) if C.last_buy_price > 0 else 0
        
        # 下单（市价单卖出）
        passorder(
            24,                 # 24=卖出
            1101,               # 市价单
            C.accountid,        # 账号
            C.stock,            # 品种
            5,                  # 订单类型
            -1,                 # 止价（-1表示不设置）
            holding_vol,        # 数量
            C                   # ContextInfo对象
        )
        
        if total_profit > 0:
            C.win_trades += 1
        
        C.total_profit += total_profit
        
        print(f"       成功下单 - 卖出 {holding_vol} 股 @ {current_price:.2f}")
        print(f"       买入价:{C.last_buy_price:.2f} | 卖出价:{current_price:.2f} | "
              f"单笔收益:{total_profit:.2f}元 (收益率:{profit_rate:.2f}%)")
        
        # 绘制卖出标记
        C.draw_text(1, 2, '卖')
    
    # ========== 9. 其他逻辑 - 止损 ==========
    # 如果持仓中且价格跌幅超过5%，会执行止损卖出
    # （可选功能，根据实际需要调整）
    elif holding_vol > 0 and C.last_buy_price > 0:
        loss_rate = (current_price - C.last_buy_price) / C.last_buy_price
        if loss_rate < -0.05:  # 跌幅超过5%
            print(f"[{bar_date}] ⚠ 止损信号 - 亏损{abs(loss_rate)*100:.2f}% 准备卖出")
            

def on_before_end(C):
    """
    回测结束前的处理函数
    """
    print("\n" + "="*60)
    print("回测结果统计")
    print("="*60)
    print(f"总交易次数: {C.trade_count}")
    print(f"赢利交易次数: {C.win_trades}")
    print(f"总收益: {C.total_profit:.2f}元")
    
    if C.trade_count > 0:
        print(f"成功率: {C.win_trades/C.trade_count*100:.2f}%")
        print(f"平均单笔: {C.total_profit/C.trade_count:.2f}元")
    
    print("="*60)
