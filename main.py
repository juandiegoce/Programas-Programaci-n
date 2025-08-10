import sys
import io
from sistema_llantera_db import SistemaLlantera

def main():
    print("🔧 Iniciando Clamatin")
    print("=" * 30)
    sistema = SistemaLlantera()
    sistema.run()

if __name__ == '__main__':
    main()