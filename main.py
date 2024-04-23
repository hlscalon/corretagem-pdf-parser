import argparse
import sys
import genial

def main():
    parser = argparse.ArgumentParser("corretagem-pdf-parser")
    parser.add_argument("corretora", help="Corretora")
    parser.add_argument("arquivo", help="Caminho completo do arquivo")
    args = parser.parse_args()

    if args.corretora != "genial":
        print("Valores válidos para corretoras: genial")
        sys.exit(0)

    genial.parse(args.arquivo)

main()
