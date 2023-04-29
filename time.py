import argparse
import time
import webbrowser

def focus_timer(minutes: int, break_time: int):
    print(f"Focus time starting for {minutes} minutes.")
    time.sleep(minutes * 60)
    print("Time's up! Take a break.")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(break_time * 60)
    print(f"Break time over, back to focusing.")
    focus_timer(minutes, break_time)

parser = argparse.ArgumentParser(description='Start a focus timer.')
parser.add_argument('minutes', type=int, help='The length of each focus period (in minutes).')
parser.add_argument('break_time', type=int, help='The length of each break period (in minutes).')

if __name__ == '__main__':
    args = parser.parse_args()
    focus_timer(args.minutes, args.break_time)
