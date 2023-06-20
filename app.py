import rich
import argparse
import sys
from chatbot import chat_bot



def main():
    parse = argparse.ArgumentParser()
    temp = parse.add_argument('-t' ,'--temperature', type=float, default='0.5', help='temperature of the model set a value between 0.0 and 1.0')
    request = parse.add_argument('-m', '--message', type=string, )
    chunk_overlap = parse.add_argument('-c' ,'--chunk-overlap', type=float, default='0.3', help='chunk overlap set a value between 0.0 and 1.0')

