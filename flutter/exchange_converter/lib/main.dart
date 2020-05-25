import 'package:flutter/material.dart';
import 'dart:async';
import 'package:http/http.dart' as http;
import 'dart:convert';

const url = "https://api.hgbrasil.com/finance?format=json&key=a5403858";

void main() async {
  runApp(MaterialApp(
    title: "Exchange Converter",
    home: Home(),
    theme: ThemeData(
      hintColor: Colors.white,
      primaryColor: Colors.amber,
    ),
  ));
}

Future<Map> getData() async {
  http.Response response = await http.get(url);
  return json.decode(response.body);
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  TextEditingController _brlInput = TextEditingController(text: "");
  TextEditingController _usdInput = TextEditingController(text: "");
  TextEditingController _eurInput = TextEditingController(text: "");

  double _euro = 1.0;
  double _usd = 1.0;

  void _reset() {
    _brlInput.text = "";
    _usdInput.text = "";
    _eurInput.text = "";
  }

  void _brlOnChangeHandler(String value) {
    if (value.isEmpty) {
      _reset();
    }
    double real = double.parse(value);
    _usdInput.text = (real / _usd).toStringAsFixed(2);
    _eurInput.text = (real / _euro).toStringAsFixed(2);
  }

  void _usdOnChangeHandler(String value) {
    if (value.isEmpty) {
      _reset();
    }
    double usd = double.parse(value);
    _brlInput.text = (usd * _usd).toStringAsFixed(2);
    _eurInput.text = (usd * (_usd / _euro)).toStringAsFixed(2);
  }

  void _eurOnChangeHandler(String value) {
    if (value.isEmpty) {
      _reset();
    }
    double eur = double.parse(value);
    _brlInput.text = (eur * _euro).toStringAsFixed(2);
    _usdInput.text = (eur * (_usd / _euro)).toStringAsFixed(2);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black87,
      appBar: AppBar(
        title: Text(
          "Exchange Converter",
          style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.w900,
          ),
        ),
        backgroundColor: Colors.amber,
        centerTitle: true,
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.refresh),
            onPressed: _reset,
          )
        ],
      ),
      body: FutureBuilder(
        future: getFakeData(),
        builder: (context, snapshot) {
          switch (snapshot.connectionState) {
            case ConnectionState.none:
            case ConnectionState.waiting:
              return Center(
                child: Text(
                  "Loading...",
                  style: TextStyle(color: Colors.amber),
                  textAlign: TextAlign.center,
                ),
              );
              break;
            default:
              if (snapshot.hasError) {
                return Text(
                  "Loading failed :(",
                  style: TextStyle(color: Colors.amber),
                  textAlign: TextAlign.center,
                );
              }

              this._usd = snapshot.data["results"]["currencies"]["USD"]["buy"];
              this._euro = snapshot.data["results"]["currencies"]["EUR"]["buy"];

              return buildExchangeForm();
          }
        },
      ),
    );
  }

  SingleChildScrollView buildExchangeForm() {
    return SingleChildScrollView(
        padding: EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            Padding(
              padding: EdgeInsets.only(bottom: 10),
              child: Icon(
                Icons.monetization_on,
                color: Colors.amber,
                size: 100,
              ),
            ),
            buildTextField(
                "R\$", "Brazilian Real", _brlInput, _brlOnChangeHandler),
            Divider(),
            buildTextField(
                "US\$", "US Dollars", _usdInput, _usdOnChangeHandler),
            Divider(),
            buildTextField("€", "Euro", _eurInput, _eurOnChangeHandler),
          ],
        ));
  }

  Center buildTextField(String prefix, String currency,
      TextEditingController controller, Function onChangeEventHandler) {
    return Center(
      child: TextField(
        decoration: InputDecoration(
          labelText: currency,
          labelStyle: TextStyle(color: Colors.amber),
          prefixText: "$prefix ",
          border: OutlineInputBorder(),
        ),
        style: TextStyle(
          color: Colors.amber,
          fontSize: 22,
        ),
        keyboardType: TextInputType.numberWithOptions(decimal: true),
        controller: controller,
        onChanged: onChangeEventHandler,
      ),
    );
  }
}

Future<Map> getFakeData() async {
  String source = """
  {
    "by": "default",
    "valid_key": true,
    "results": {
        "currencies": {
            "source": "BRL",
            "USD": {
                "name": "Dollar",
                "buy": 5.5739,
                "sell": 5.5323,
                "variation": -0.152
            },
            "EUR": {
                "name": "Euro",
                "buy": 6.0329,
                "sell": 6.0277,
                "variation": -0.799
            },
            "GBP": {
                "name": "Pound Sterling",
                "buy": 6.738,
                "sell": null,
                "variation": -0.801
            },
            "ARS": {
                "name": "Argentine Peso",
                "buy": 0.0812,
                "sell": null,
                "variation": -0.612
            },
            "BTC": {
                "name": "Bitcoin",
                "buy": 54459.714,
                "sell": 54459.714,
                "variation": 0.253
            }
        },
        "stocks": {
            "IBOVESPA": {
                "name": "BM&F BOVESPA",
                "location": "Sao Paulo, Brazil",
                "points": 82173.211,
                "variation": -1.03
            },
            "NASDAQ": {
                "name": "NASDAQ Stock Market",
                "location": "New York City, United States",
                "points": 9324.59,
                "variation": 0.61
            },
            "CAC": {
                "name": "CAC 40",
                "location": "Paris, French",
                "variation": -0.02
            },
            "NIKKEI": {
                "name": "Nikkei 225",
                "location": "Tokyo, Japan",
                "variation": -0.8
            }
        },
        "available_sources": [
            "BRL"
        ],
        "bitcoin": {
            "blockchain_info": {
                "name": "Blockchain.info",
                "format": [
                    "USD",
                    "en_US"
                ],
                "last": 9225.32,
                "buy": 9225.32,
                "sell": 9225.32,
                "variation": 0.339
            },
            "coinbase": {
                "name": "Coinbase",
                "format": [
                    "USD",
                    "en_US"
                ],
                "last": 9226.37,
                "variation": 0.344
            },
            "bitstamp": {
                "name": "BitStamp",
                "format": [
                    "USD",
                    "en_US"
                ],
                "last": 9221.98,
                "buy": 9229.44,
                "sell": 9223.09,
                "variation": 0.207
            },
            "foxbit": {
                "name": "FoxBit",
                "format": [
                    "BRL",
                    "pt_BR"
                ],
                "last": 51530.41,
                "variation": -0.069
            },
            "mercadobitcoin": {
                "name": "Mercado Bitcoin",
                "format": [
                    "BRL",
                    "pt_BR"
                ],
                "last": 51601.28649,
                "buy": 51650.02134,
                "sell": 51990.67126,
                "variation": 0.002
            }
        },
        "taxes": [
            {
                "date": "2020-05-19",
                "cdi": 3,
                "selic": 3,
                "daily_factor": 1.00011345,
                "selic_daily": 2.9,
                "cdi_daily": 2.9
            }
        ]
    },
    "execution_time": 0,
    "from_cache": true
}
  """;
  return json.decode(source);
}
