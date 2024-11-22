import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

fetchData(String url) async{
  http.Response response = await http.get(Uri.parse(url));
  return response.body;
}


void main() {
  runApp(MaterialApp(home: GolfApp()));
}

class GolfApp extends StatefulWidget {
  const GolfApp({super.key});

  @override
  GolfAppState createState() => GolfAppState();
}

class GolfAppState extends State<GolfApp> {
  final TextEditingController yardController = TextEditingController();
  final TextEditingController windController = TextEditingController();
  final TextEditingController tempController = TextEditingController();
  final TextEditingController holeController = TextEditingController();

  String result = '';

  Future<void> calculate() async {
    try {
      final url = Uri.parse('http://127.0.0.1:5000/calculate'); 
      final body = {
        'yard': int.tryParse(yardController.text) ?? 0,
        'wind': int.tryParse(windController.text) ?? 0,
        'temp': int.tryParse(tempController.text) ?? 0,
        'hole': int.tryParse(holeController.text) ?? 0,
      };

      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(body),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        if (data['final_yardage'] != null && data['recommended_club'] != null) {
          setState(() {
            result =
                "Final Yardage: ${data['final_yardage']}\nRecommended Club: ${data['recommended_club']}";
          });
        } else {
          setState(() {
            result = "Error: Invalid response from server.";
          });
        }
      } else {
        setState(() {
          result = "Error: ${response.body}";
        });
      }
    } catch (e) {
      setState(() {
        result = "Error: ${e.toString()}";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Yardage Calculator')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: yardController,
              decoration: const InputDecoration(labelText: 'Yardage'),
              keyboardType: TextInputType.number,
            ),
            TextField(
              controller: windController,
              decoration: const InputDecoration(labelText: 'Wind Speed MPH (Neg if downwind)'),
              keyboardType: TextInputType.number,
            ),
            TextField(
              controller: tempController,
              decoration: const InputDecoration(labelText: 'Temperature *C'),
              keyboardType: TextInputType.number,
            ),
            TextField(
              controller: holeController,
              decoration: const InputDecoration(labelText: 'Hole'),
              keyboardType: TextInputType.number,
            ),
            const SizedBox(height: 20),
            ElevatedButton(onPressed: calculate, child: const Text('Calculate')),
            const SizedBox(height: 20),
            Text(result, textAlign: TextAlign.center),
          ],
        ),
      ),
    );
  }
}
