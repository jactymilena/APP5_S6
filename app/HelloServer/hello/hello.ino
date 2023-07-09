#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Fab5";
const char* password = "****";
const char* serverURL = "http://127.0.0.1:5000/control";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("Connexion au WiFi en cours...");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);    
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Connecté au WiFi !");
  Serial.print("Connecté à ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}
void loop(){

 if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    // Spécifiez l'URL du serveur et l'endpoint
    http.begin(serverURL + "/endpoint");

    // Définissez les en-têtes de la requête si nécessaire
    http.addHeader("Content-Type", "application/json");

    // Construisez les données à envoyer au serveur
    String data = "{\"temperature\": 25.5, \"humidity\": 60}";

    // Envoyez une requête POST avec les données
    int httpResponseCode = http.POST(data);

    if (httpResponseCode > 0) {
      Serial.print("Réponse du serveur : ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Erreur lors de l'envoi de la requête : ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }

  delay(5000); // Attendez 5 secondes avant d'envoyer la prochaine requête
}
