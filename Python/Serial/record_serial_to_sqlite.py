
# Code expects serial output to be in the format "V: X X X X X X X X)" e.g. "V: 3.28 0.01 1.36 0.14 0.61 0.65 0.68 0.65" (without double quotes)

import serial
import argparse
import sqlite3

class DataRecorder:
    def __init__(self,filename):
        if filename == "None":
            self.f = None
            return
        else:
            self.f = filename
        self.con = sqlite3.connect(self.f)
        self.cur = self.con.cursor()
        self.cur.execute('''
    CREATE TABLE IF NOT EXISTS Voltages (
        id INTEGER PRIMARY KEY,
        channel TEXT,
        unit TEXT,
        value INTEGER                 
            )
        ''')
    def write(self,text):
        if self.f == None:
            return
        self.cur.execute("SELECT COUNT(*) FROM Voltages;")
        count = self.cur.fetchone()[0]
        self.cur.execute(f"""
    INSERT INTO Voltages VALUES
        ('{count}','{text[0]}', '{text[1]}', '{text[2]}')
""")
    def close(self):
        if self.f == None:
            return
        self.con.commit()
        self.con.close()

def main(args):
    data_file = DataRecorder(args.output)
    try:
        ser = serial.Serial(args.port, args.baudrate)

        

        while True:
            data = ser.readline()
            text = data.decode('utf-8')
            if text[0] == "V":
                return_data = text.split()
                return_data.pop(0)
                for k,value in enumerate(return_data):
                    data_file.write((f"Channel {k}","Volts",value))
            print(text, end="")
            
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ser.close()
        print("Serial port was closed.")
        data_file.close()
        print("The database was closed.")

if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument("-p", "--port",required=True, help="Define serial port (e.g. COM4 or /dev/ttyUSB0)")
    args.add_argument("-b", "--baudrate",type=int, default=9600, help="Define baudrate (default: 9600)")
    args.add_argument("-o","--output",default="data.db", help='Output file name (use None to disable output) (default data.txt)')
    args = args.parse_args()
    main(args)