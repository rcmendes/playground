import 'package:flutter/material.dart';

class Answer extends StatelessWidget {
  final Function onPressedHandler;
  final String text;

  Answer({this.onPressedHandler, this.text});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      child: RaisedButton(
        onPressed: onPressedHandler,
        child: Text(text),
        color: Colors.blue,
        textColor: Colors.white,
      ),
      margin: EdgeInsets.symmetric(horizontal: 20, vertical: 4),
    );
  }
}
