import "package:flutter/material.dart";

class Result extends StatelessWidget {
  final int score;
  final Function onPressedResetHandler;

  Result({@required this.score, this.onPressedResetHandler});

  String get phrase {
    if (score > 15) {
      return "Very good!";
    }

    if (score > 10 && score <= 15) {
      return "Cloooose!";
    }
    return "Not that quite, maybe next time. ;)";
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: <Widget>[
          Container(
            child: Text(phrase,
                style: TextStyle(
                  fontSize: 36,
                  fontWeight: FontWeight.bold,
                ),
                textAlign: TextAlign.center),
            margin: EdgeInsets.only(top: 20, bottom: 20),
          ),
          FlatButton(
            child: Text("Start over"),
            onPressed: onPressedResetHandler,
            textColor: Colors.blue,
          )
        ],
      ),
    );
  }
}
