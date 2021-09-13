from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

msg = {'name': 'Reliance'}

#Ratios
ratio = [
  {'name': 'Basic EPS',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Diluted EPS',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Book Value',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Divident/Share',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'PBDIT Margin(%)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Net Profit Margin(%)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Return on Networth/Equity(%)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Return on Capital Employed(%)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Return on Assets',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Total Debt/Equity(X)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Asset Turnover Ratio(%)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Current Raito(X)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Quick Ratio(X)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Divident Payout Ratio(NP)(%)',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  },
  {'name': 'Earnings Yield',
  'data':[45,46,47,48,49,37,56,60,31,23],
   'graph': '#chart1'
  }
]

#speeches
speech = [
  {
      'summary': 'lorem',
      'keywords': ['one', 'two', 'three'],
      'fullCont': 'lorem'
  },
  {
      'summary': 'lorem',
      'keywords': ['one', 'two', 'three'],
      'fullCont': 'lorem'
  }
]

#newsList
newsList = ['https://www.google.com/',
            'https://www.google.com/']

@app.route('/')
def index():
    return redirect (url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return render_template('stats.html',usr=user)
    else:
        return render_template('login.html') 

@app.route('/test')
def test():
    return jsonify(msg)

@app.route('/speeches')
def speeches():
    return jsonify(speech)

@app.route('/ratios')
def ratios():
    return jsonify(ratio)

@app.route('/news')
def news():
    return jsonify(newsList)

if __name__ == "__main__":
	app.run(debug=True,port=5003)