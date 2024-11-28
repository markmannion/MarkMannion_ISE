import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

fetchData(String url) async {
  http.Response response = await http.get(Uri.parse(url));
  return response.body;
}

void main() {
  runApp(MaterialApp(
    home: HomePage(),
    routes: {
      '/calculator': (context) => GolfApp(),
    },
  ));
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Text(
                'Yardage Calculator',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/calculator');
                },
                child: const Text('Go to Calculator'),
              ),
            ],
          ),
        ),
      ),
    );
  }
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
      appBar: AppBar(title: const Text('Fota Island\nDeerpark Course', style: TextStyle(fontSize: 35))),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              _buildInputCard('Yardage', yardController),
              _buildInputCard('Wind Speed MPH (Neg if downwind)', windController),
              _buildInputCard('Temperature *C', tempController),
              _buildInputCard('Hole', holeController),
              const SizedBox(height: 20),
              ElevatedButton(onPressed: calculate, child: const Text('Calculate')),
              const SizedBox(height: 20),
              Text(
                result,
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 20),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildInputCard(String label, TextEditingController controller) {
    return Card(
      elevation: 2,
      margin: const EdgeInsets.symmetric(vertical: 8),
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              label,
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w500),
            ),
            TextField(
              controller: controller,
              decoration: const InputDecoration(border: OutlineInputBorder()),
              keyboardType: TextInputType.number,
            ),
          ],
        ),
      ),
    );
  }
}