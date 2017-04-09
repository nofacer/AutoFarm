#include <OneWire.h>
#include <DallasTemperature.h>
 
// 定义DS18B20数据口连接arduino的2号IO上
#define ONE_WIRE_BUS 2

// 初始连接在单总线上的单总线设备
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

float temper;
void setup(void)
{
   pinMode(LED_BUILTIN, OUTPUT);  
  // 设置串口通信波特率
  Serial.begin(9600);
  // 初始库
  sensors.begin();
}
 
void loop(void)
{ 
  sensors.requestTemperatures(); // 发送命令获取温度
  temper=sensors.getTempCByIndex(0);
  Serial.println(temper);    
}
