# This is fork, original code is located here

https://github.com/google-coral/project-keyword-spotter

# How to install

*More details:*<br>
*https://coral.ai/docs/dev-board-mini/get-started/*<br>
*https://www.youtube.com/watch?v=nJ8Qs_RFWZc*<br>

```
mdt devices

mdt shell

~/ nmcli dev wifi connect [SSID] password [PWD] ifname wlan0

~/ nmcli connection show

mdt shell 192.168.0.129

~/ sudo apt-get update
~/ sudo apt-get dist-upgrade
~/ sudo reboot now

mdt shell 192.168.0.129

~/ sudo apt-get install python3.7-dev
~/ sudo apt-get install portaudio19-dev
~/ pip3 install pyaudio
~/ pip3 install ShellyPy

~/ rm -rf project-keyword-spotter

~/ git clone https://github.com/mvlasenko/project-keyword-spotter

~/ cd project-keyword-spotter

~/ git pull

~/ sudo shutdown now
```

# How to reflash

*It is important to run `sudo shutdown now` before you switch off the power. If you did't do this and broke the image, then this section is for you.*<br>

*More details:*<br>
*https://coral.ai/docs/dev-board-mini/reflash/*<br>
*https://www.youtube.com/watch?v=KgJ5QwVFTEk*<br>

copy fastboot.exe to any PATH folder

```
pip install pyftdi pyserial
```

download image
https://coral.ai/software/#mendel-dev-board-mini

unzip, go to img folder

```
bash enable_lk_fastboot.sh
```

connect jumper and usb

```
fastboot devices

bash flash.sh
```

# Run test application

```
~/ python3 run_model.py
```
use `exit_application` label to exit from endles application

# Run Shelly control

```
~/ python3 run_voice_control.py
```
use `exit_application` label to exit from endles application

Execute params:

`--model_file=custom_model.tflite` - Optional: use custom model.

`--labels_file=custom_labels.txt` - Optional: use custom labels.

`--init_label=attention` - Optional: lebel that inits hearing. Version of phrase 'OK Google' or 'Alexa'.

`--init_time=10` - Optional: number of seconds that hearing active after init_label was told.

`--exit_label=exit_application` - Optional: custom exit_application label.

`--mic=ID` - Optional: Input source microphone ID.

`--num_frames_hop=33` - Optional: Number of frames to wait between model inference calls. Smaller numbers will reduce the latancy while increasing compute cost. Must devide 198. Defaults to 33.

`--sample_rate_hz=16000` - Optional: Sample Rate. The model expects 16000. However you may alternative sampling rate that may or may not work. If you specify 48000 it will be downsampled to 16000.

# Examples

run with init word

```
~/ python3 run_voice_control.py --init_label=open_application --init_time=10
```

use another model

```
~/ python3 run_model.py --model_file=model.tflite --labels_file=labels.txt
```