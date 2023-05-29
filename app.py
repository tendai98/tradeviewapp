import streamlit as st
import streamlit.components.v1 as components
import json
from ticker_tape import tape

st.set_page_config(layout="wide")

st.sidebar.subheader('Trade View')
#ticker = st.sidebar.text_input('Ticker', value = "TVC:GOLD")
#theme = st.sidebar.selectbox('Theme', options = ['dark', 'light'])
#fund_type = st.sidebar.selectbox('Fundamental Display', options = ['regular', 'compact'])

widget_data = {"symbol":None, "height": "100%", "width":"100%", "local":"en", "colorTheme":"dark", "isTransperent":False}
symbols = ["TVC:GOLD", "TVC:SILVER", "BINANCE:BTCUSD", "ETHUSD", "FX:USDCHF"]
WIDGET_THEME = "dark"
WIDGET_HEIGHT = 150
WIDGET_WIDTH = 800

def generate_widget(ticker):

	widget_data['symbol'] = ticker

	widget = '''
		<div class="tradingview-widget-container">
  		<div class="tradingview-widget-container__widget"></div>
  		<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
			{}
  		</script>
		</div>'''.format(json.dumps(widget_data))

	return widget



def main():

	for symbol in symbols:
		widget = generate_widget(symbol)
		components.html(widget, height=WIDGET_HEIGHT, width=WIDGET_WIDTH)

	 components.html(tape)


main()
