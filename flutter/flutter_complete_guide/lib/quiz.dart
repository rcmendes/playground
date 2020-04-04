import "package:flutter/material.dart";

import "answer.dart";
import "question.dart";

class Quiz extends StatelessWidget {
  final List<Map<String, Object>> questions;
  final Function onAnswerHandler;
  final int questionIndex;

  Quiz(
      {@required this.questions,
      @required this.onAnswerHandler,
      @required this.questionIndex});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Question(questions[questionIndex]["question"]),
        ...(questions[questionIndex]["answers"] as List<Map<String, Object>>)
            .map((answer) {
          return Answer(
              onPressedHandler: () => onAnswerHandler(answer["points"]),
              text: answer["text"]);
        }).toList()
      ],
    );
  }
}
