# IR Remote Controlled Car using ESP32 & PicoBricks (MicroPython Version)

This project demonstrates how to build and program an IR-controlled car using the [PicoBricks](https://picobricks.com/) platform with MicroPython. The car responds to remote control commands and automatically stops if it detects an obstacle in front of it.

## 🧰 Hardware Required
- PicoBricks with ESP32
- IR Receiver (connected to GPIO 17)
- HC-SR04 Ultrasonic Sensor (TRIG: GPIO 26, ECHO: GPIO 27)
- 2 DC Motors controlled via I2C Motor Driver
- IR Remote (NEC protocol)

## 🧠 Features
- Move Forward, Backward, Left, Right
- Stop on command or when obstacle is closer than 15 cm
- Remote input via IR receiver
- MicroPython compatible with PicoBricks

## 📁 File
- `IR_Remote_Car_MicroPython.py` — main source code for uploading to ESP32

## 🎮 IR Remote Buttons Mapping

| Button     | Action          |
|------------|-----------------|
| ⬆️ Up       | Move forward    |
| ⬇️ Down     | Move backward   |
| ⬅️ Left     | Turn left       |
| ➡️ Right    | Turn right      |
| OK         | Stop            |

> All unknown IR codes are printed via serial.

## 📷 Example Output

```text
Distance: 27 cm
Moving forward...
Distance: 13 cm
Obstacle detected. Stopped.
```

## 🧾 License
MIT License © 2025 Büşra

---

**Made with ❤️ using PicoBricks and MicroPython**
