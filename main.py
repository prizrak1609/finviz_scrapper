from finviz.screener import Screener
import finviz.main_func

urls = ["https://finviz.com/screener.ashx"]

tickers = []

last_dividend = 0.0

max_div = 0.0

for url in urls:
    stock_list = Screener.init_from_url(url, rows=8000)
    for pos in range(0, stock_list.__len__()):
        try:
            details = stock_list.get(pos)
            ticker = details["Ticker"]
            stock = finviz.get_stock(ticker)
            if max_div < float(stock["Dividend"]):
                max_div = float(stock["Dividend"])
            # print("pos ", pos, " ticker ", ticker, " div ", stock["Dividend"], " max div ", max_div)
            val = float(stock["Price"]) / float(stock["Dividend"])
            if stock not in tickers and last_dividend < float(stock["Dividend"]):
                # print("add ", ticker)
                last_dividend = float(stock["Dividend"])
                stock["Ticker"] = ticker
                tickers.append(stock)
        except:
            pass

tickers.sort(key=lambda item: item["Dividend"], reverse=True)

for i in range(0, 5 if tickers.__len__() > 5 else tickers.__len__()):
    ticker = tickers[i]
    # print(ticker["Ticker"], "   Price: ", ticker["Price"], "   Dividend: ", ticker["Dividend"], " ",
    #       ticker["Dividend %"], "   Price to div: ", float(ticker["Price"]) / float(ticker["Dividend"]))
    # print(finviz.get_analyst_price_targets(ticker["Ticker"]))