import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = String.fromEnvironment(
    'BASE_URL',
    defaultValue: 'http://192.168.8.6:8000',
  );

  Future<Map<String, dynamic>> analyzeFood(File image) async {
    final uri = Uri.parse('$baseUrl/api/analyze');

    final request = http.MultipartRequest(
      'POST',
      uri,
    );

    request.files.add(
      await http.MultipartFile.fromPath(
        'image',
        image.path,
      ),
    );

    final streamedResponse = await request.send();

    final response = await http.Response.fromStream(
      streamedResponse,
    );

    if (response.statusCode == 429) {
      throw Exception(
        'Too many scans. Please wait and try again.',
      );
    }

    if (response.statusCode != 200) {
      throw Exception(
        'Analysis failed: ${response.body}',
      );
    }

    return jsonDecode(response.body);
  }
}