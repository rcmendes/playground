import 'package:flutter/material.dart';
import "quiz.dart";
import "result.dart";

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _MyAppState();
  }
}

class _MyAppState extends State<MyApp> {
  var _questionIndex = 0;
  var _score = 0;

  void _answerQuestion(int points) {
    setState(() {
      _questionIndex++;
      _score += points;
      print(_questionIndex);
      print(_score);
    });
  }

  void _onResetHandler() {
    setState(() {
      _questionIndex = 0;
      _score = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    var _questions = [
      {
        "question": "What's one of my favorite animals?",
        "answers": [
          {"text": "Dog", "points": 10},
          {"text": "Cat", "points": 5},
          {"text": "Horse", "points": 3},
          {"text": "Bird", "points": 2}
        ]
      },
      {
        "question": "What's  one of my favorite colors?",
        "answers": [
          {"text": "Black", "points": 1},
          {"text": "Blue", "points": 5},
          {"text": "White", "points": 8},
          {"text": "Green", "points": 10}
        ],
      }
    ];
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('The Complete Flutter Guide'),
        ),
        body: _questionIndex < 2
            ? Quiz(
                onAnswerHandler: _answerQuestion,
                questions: _questions,
                questionIndex: _questionIndex,
              )
            : Result(
                score: _score,
                onPressedResetHandler: _onResetHandler,
              ),
      ),
    );
  }
}
