from json import dumps

symbols = [["TVC:GOLD",""], ["TVC:SILVER",""], ["BINANCE:BTCUSD",""], ["ETHUSD",""], ["FX:USDCHF",""]]
symbolsObject = {"symbols":[], "showSymbolLogo":True, "colorTheme":"dark", "isTransparent":"false", "displayMode":"adaptive", "local":"en"}

for symbol_value in symbols:
	symbolsObject['symbols'].append({"proName":symbol_value[0], "description":symbol_value[1]})


tape = '''
	<div class="tradingview-widget-container">
  		<div class="tradingview-widget-container__widget"></div>
  		<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{}</script>
	</div>'''.format(dumps(symbolsObject))
