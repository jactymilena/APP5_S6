#include <WiFi.h>
#include <HTTPClient.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include <BLEEddystoneURL.h>
#include <BLEEddystoneTLM.h>
#include <BLEBeacon.h>

const char* ssid = "Saenzros2_4";
const char* password = "****"; // NE PAS PUSH 
const char* serverURL = "http://10.0.0.223:5000/ids";

std::vector<std::string> activeIds(10);
int scanTime = 1; // seconds
BLEScan *pBLEScan;


class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks
{    
    void onResult(BLEAdvertisedDevice advertisedDevice)
    {
    }
};

void setupBLE() {
  Serial.println("Scanning...");

  BLEDevice::init("");
  pBLEScan = BLEDevice::getScan(); //create new scan
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true); //active scan uses more power, but get results faster
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99); // less or equal setInterval value
}

void setupWifi() {
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

void setup() {
  Serial.begin(115200);
  setupWifi();
  setupBLE();
}


void scanBLEBeacon() {
  activeIds.clear();
  BLEScanResults foundDevices = pBLEScan->start(scanTime, false);
  int count = foundDevices.getCount();
  for(int i = 0; i < count; i++) {
      auto foundDevice = foundDevices.getDevice(i);
      if (foundDevice.haveManufacturerData())
      {
        std::string strManufacturerData = foundDevice.getManufacturerData();

        uint8_t cManufacturerData[100];
        strManufacturerData.copy((char *)cManufacturerData, strManufacturerData.length(), 0);

        if (strManufacturerData.length() == 25 && cManufacturerData[0] == 0x4C && cManufacturerData[1] == 0x00)
        {
          BLEBeacon oBeacon = BLEBeacon();
          oBeacon.setData(strManufacturerData);
          activeIds.push_back(oBeacon.getProximityUUID().toString());

          Serial.printf("UUID: %s\n", oBeacon.getProximityUUID().toString().c_str());
        }
      }
  }
  
}

void loop() {
  scanBLEBeacon();

 if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(serverURL);

    String data = "{\"ids\": [";
    for(int i = 0; i < activeIds.size(); i++) {
      data += "\"" + String(activeIds[i].c_str());
      if(i != activeIds.size() - 1) {
        data += "\",";
      } else {
        data += "\"";
      }
    }
    data += "\]}";

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

  delay(1000); // Attendez 5 secondes avant d'envoyer la prochaine requête
}
