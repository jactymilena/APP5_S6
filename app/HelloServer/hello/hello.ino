#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Saenzros2_4";
const char* password = "********"; // NE PAS PUSH 
const char* serverURL = "http://10.0.0.223:5000/ids";

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
    http.begin(serverURL);


    // Construisez les données à envoyer au serveur
    String data = "{\"ids\": [\"7f3bfd87-a46d-4a51-bdeb-7a479432a8f8\", \"5b964c48-2edc-43b3-b6bf-c50a563460a2\" ]}";

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
