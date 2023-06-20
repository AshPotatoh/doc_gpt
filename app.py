import rich
import argparse
import sys
from chatbot import chat_bot
from get_embeddings import get_embeddings

#chroma server
db_storage = ''

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-t' ,'--temperature', type=float, default='0.5', help='temperature of the model set a value between 0.0 and 1.0')
    parse.add_argument('-m', '--message', type=str, )
    parse.add_argument('-c' ,'--chunk-overlap', type=float, default='0.3', help='chunk overlap set a value between 0.0 and 1.0')
    parse.add_argument('-s', '--single-search', type=str, help='get embeddings from a single file or folder contents, only runs once. Does not save embeddings. Specify file path.')
    parse.add_argument('-a', '--append', type=str, help='get embeddings from file or folders and append to chromadb') 
    args = parse.parse_args()
    print(args.temperature, args.chunk_overlap, args.message)
    if args.single-search:
        get_embeddings(args.embeddings, 'storage')
    if args.append:
        get_embeddings(args.append, db_storage)

    if args.message:
        reply = chat_bot(args.message, args.temperature, args.chunk_overlap)
        rich.print(reply)

if __name__ == '__main__':
    main()
