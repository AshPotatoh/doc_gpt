import rich
import argparse
import sys
from chatbot import chat_bot



def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-t' ,'--temperature', type=float, default='0.5', help='temperature of the model set a value between 0.0 and 1.0')
    parse.add_argument('-m', '--message', type=str, )
    parse.add_argument('-c' ,'--chunk-overlap', type=float, default='0.3', help='chunk overlap set a value between 0.0 and 1.0')
    args = parse.parse_args()
    print(args.temperature, args.chunk_overlap, args.message)
    reply = chat_bot(args.message, args.temperature, args.chunk_overlap)
    rich.print(reply)

if __name__ == '__main__':
    main()
