import argparse
import ShellyPy

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--on", help="switch on", action="store_true")
    parser.add_argument("--off", help="switch off", action="store_true")
    args = parser.parse_args()

    device = ShellyPy.Shelly("192.168.0.111")

    if(args.on):
        device.relay(0, turn=True)

    if(args.off):
        device.relay(0, turn=False)


if __name__ == "__main__":
  main()