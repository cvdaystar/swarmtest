import yfinance as yf
from swarm import Swarm, Agent
import pandas_ta as ta
import pandas as pd
import os

if __name__ == '__main__':
    client = Swarm()
    context_variables = {}

    general_agent = Agent(
        name="總管理Agent",
        instructions="""你是股票市場查詢的總管理者。
        根據使用者的問題類型，將請求轉發給適當的專家：
        - 股價相關問題 -> 股價查詢專家
        - 財務數據相關問題 -> 財務分析專家
        - 技術指標相關問題 -> 技術分析專家
        如果使用者想要完整分析，可以依序調用多個專家的服務。""",
        functions=[]
    )

    current_agent = general_agent

    user_input = input("\n您的問題: ")

    response = client.run(
        agent=current_agent,
        messages=[{"role": "user", "content": user_input}],
        context_variables=context_variables
    )

    print(f"\n{response.agent.name}:", response.messages[-1]["content"])
    current_agent = response.agent
    context_variables = response.context_variables

    pass