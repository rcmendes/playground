import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';

void main() => runApp(MaterialApp(
      title: "Task List",
      home: Home(),
    ));

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final _newTaskFieldController = TextEditingController();
  var _list = [];
  var _lastRemovedItem;
  var _lastRemovedItemPosition = -1;

  @override
  void initState() {
    super.initState();

    _loadData().then((value) => setState(() => _list = value));
  }

  void _onAddTaskHandler() {
    setState(() {
      final title = _newTaskFieldController.text;
      final item = {"title": title, "completed": false};
      _list.add(item);
      _newTaskFieldController.text = "";
      _saveData();
    });
  }

  void _onChangeTaskStatusHandler(int index, bool value) {
    setState(() {
      _list[index]["completed"] = value;
      _saveData();
    });
  }

  Future<void> _onRefreshList() async {
    setState(() {
      _list.sort((a, b) {
        if (a["completed"] && !b["completed"]) {
          return 1;
        } else if (!a["completed"] && b["completed"]) {
          return -1;
        } else {
          return 0;
        }
      });
      _saveData();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Task List"),
        backgroundColor: Colors.blueGrey,
        centerTitle: true,
      ),
      body: Column(
        children: <Widget>[
          _buildNewTaskContainer(),
          Expanded(
            child: RefreshIndicator(
                child: _buildTaskList(), onRefresh: _onRefreshList),
          ),
        ],
      ),
    );
  }

  ListView _buildTaskList() {
    return ListView.builder(
        padding: EdgeInsets.only(top: 10),
        itemCount: _list.length,
        itemBuilder: (context, index) {
          return Dismissible(
            key: Key(DateTime.now().millisecondsSinceEpoch.toString()),
            child: _buildTaskListItem(index),
            direction: DismissDirection.startToEnd,
            background: Container(
              color: Colors.red,
              child: Align(
                alignment: Alignment(-0.9, 0.0),
                child: Icon(
                  Icons.delete,
                  color: Colors.white,
                ),
              ),
            ),
            onDismissed: (direction) {
              _lastRemovedItem = Map.from(_list[index]);
              _lastRemovedItemPosition = index;
              _list.removeAt(index);

              final undoSnack = SnackBar(
                content:
                    Text("Task '${_lastRemovedItem['title']}' was removed."),
                action: SnackBarAction(
                    label: "UNDO",
                    onPressed: () {
                      setState(() {
                        _list.insert(
                            _lastRemovedItemPosition, _lastRemovedItem);
                        _saveData();
                      });
                    }),
                duration: Duration(seconds: 2),
              );

              Scaffold.of(context).removeCurrentSnackBar();
              Scaffold.of(context).showSnackBar(undoSnack);
            },
          );
        });
  }

  CheckboxListTile _buildTaskListItem(int index) {
    final title = _list[index]["title"];
    final checked = _list[index]["completed"];
    return CheckboxListTile(
      value: checked,
      title: Text(title),
      onChanged: (value) => _onChangeTaskStatusHandler(index, value),
      secondary: CircleAvatar(
        child: Icon(checked ? Icons.check : Icons.error),
      ),
    );
  }

  Container _buildNewTaskContainer() {
    return Container(
      padding: EdgeInsets.fromLTRB(20, 4, 16, 2),
      child: Row(
        children: <Widget>[
          Expanded(
            child: TextField(
              decoration: InputDecoration(labelText: "New Task"),
              controller: _newTaskFieldController,
            ),
          ),
          CircleAvatar(
            child: IconButton(
              icon: Icon(
                Icons.add,
                color: Colors.white,
              ),
              color: Colors.blueGrey,
              onPressed: _onAddTaskHandler,
            ),
          )
        ],
      ),
    );
  }

  Future<File> _getFile() async {
    var directory = await getApplicationDocumentsDirectory();
    return File("${directory.path}/data.json");
  }

  void _saveData() async {
    var contents = json.encode(_list);
    var file = await _getFile();
    file.writeAsStringSync(contents);
  }

  Future<List> _loadData() async {
    var file = await _getFile();
    var data = file.readAsStringSync();

    return json.decode(data);
  }
}
