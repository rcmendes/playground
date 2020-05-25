import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(title: "BMI Calculator", home: Home()));

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  TextEditingController weightController = TextEditingController();
  TextEditingController heightController = TextEditingController();

  String _info = "Please, fill in your data.";

  GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  void _reset() {
    weightController.text = "";
    heightController.text = "";
    setState(() {
      _info = "Please, fill in your data.";
      _formKey = GlobalKey<FormState>();
    });
  }

  double _calculate(double weight, double height) {
    return weight / (height * height);
  }

  void _onCalculateHandler() {
    double weight = double.parse(weightController.text);
    double height = double.parse(heightController.text) / 100;
    double bmi = _calculate(weight, height);

    setState(() {
      if (bmi < 18.6) {
        _info = "Below of the ideal weight (${bmi.toStringAsPrecision(4)})";
      } else if (bmi >= 18.6 && bmi < 24.9) {
        _info = "Ideal weight (${bmi.toStringAsPrecision(4)})";
      } else if (bmi >= 24.9 && bmi < 29.9) {
        _info =
            "Slightly above of the ideal weight (${bmi.toStringAsPrecision(4)})";
      } else if (bmi >= 29.9 && bmi < 34.9) {
        _info = "Obesity Grade I (${bmi.toStringAsPrecision(4)})";
      } else if (bmi >= 34.9 && bmi < 39.9) {
        _info = "Obesity Grade II (${bmi.toStringAsPrecision(4)})";
      } else if (bmi >= 40) {
        _info = "Obesity Grade III (${bmi.toStringAsPrecision(4)})";
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Body Mass Index Calculator"),
        backgroundColor: Colors.blueGrey,
        centerTitle: true,
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.refresh),
            onPressed: _reset,
          )
        ],
      ),
      backgroundColor: Colors.white10,
      body: SingleChildScrollView(
        padding: EdgeInsets.fromLTRB(10.0, 0, 10.0, 0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              Icon(
                Icons.person_outline,
                size: 120.0,
                color: Colors.grey,
              ),
              TextFormField(
                keyboardType: TextInputType.number,
                decoration: InputDecoration(labelText: "Weight (kg):"),
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.grey, fontSize: 25.0),
                controller: weightController,
                validator: (value) {
                  if (value.isEmpty) {
                    return "Inform the weight";
                  }
                  return null;
                },
              ),
              TextFormField(
                keyboardType: TextInputType.number,
                decoration: InputDecoration(labelText: "Height (cm):"),
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.grey, fontSize: 25.0),
                controller: heightController,
                validator: (value) {
                  if (value.isEmpty) {
                    return "Inform the height";
                  }
                  return null;
                },
              ),
              Padding(
                padding: EdgeInsets.only(top: 10, bottom: 10),
                child: Container(
                  height: 50.0,
                  child: RaisedButton(
                    child: Text(
                      "Calculate!",
                      style: TextStyle(color: Colors.white, fontSize: 20.0),
                    ),
                    onPressed: () {
                      if (_formKey.currentState.validate()) {
                        _onCalculateHandler();
                      }
                    },
                  ),
                ),
              ),
              Text(
                "$_info",
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.grey, fontSize: 25.0),
              )
            ],
          ),
        ),
      ),
    );
  }
}
