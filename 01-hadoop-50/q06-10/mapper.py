import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
      key_columna = line.split('   ')[0]
      valor_columna = line.split('   ')[2].strip()
      sys.stdout.write("{}\t{}\n".format(key_columna,valor_columna))
