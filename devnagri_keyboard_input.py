import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import keyboard

except ImportError:
    
    install('keyboard')
    import keyboard

# Blocks until you press esc.
#keyboard.wait('esc')

# Type string then press space to replace with abbreviation. eg: a+space
keyboard.add_abbreviation('a', '\u0905')
keyboard.add_abbreviation('aa', '\u0906')
keyboard.add_abbreviation('i', '\u0907')
keyboard.add_abbreviation('ii', '\u0908')
keyboard.add_abbreviation('u', '\u0909')
keyboard.add_abbreviation('uu', '\u090A')
keyboard.add_abbreviation('e', '\u090F')
keyboard.add_abbreviation('ai', '\u090E')
keyboard.add_abbreviation('o', '\u0913')
keyboard.add_abbreviation('au', '\u0914')
keyboard.add_abbreviation('R', '\u090B')
keyboard.add_abbreviation('k', '\u0915')
keyboard.add_abbreviation('kh', '\u0916')
keyboard.add_abbreviation('g', '\u0917')
keyboard.add_abbreviation('gh', '\u0918')
keyboard.add_abbreviation('ra', '\u0919')
keyboard.add_abbreviation('ch', '\u091A')
keyboard.add_abbreviation('chh', '\u091B')
keyboard.add_abbreviation('j', '\u091C')
keyboard.add_abbreviation('jh', '\u091D')
keyboard.add_abbreviation('gya', '\u091E')
keyboard.add_abbreviation('T', '\u091F')
keyboard.add_abbreviation('Th', '\u0920')
keyboard.add_abbreviation('D', '\u0921')
keyboard.add_abbreviation('Dh', '\u0922')
keyboard.add_abbreviation('ana', '\u0923')
keyboard.add_abbreviation('t', '\u0924')
keyboard.add_abbreviation('th', '\u0925')
keyboard.add_abbreviation('d', '\u0926')
keyboard.add_abbreviation('dh', '\u0927')
keyboard.add_abbreviation('n', '\u0928')
keyboard.add_abbreviation('p', '\u092A')
keyboard.add_abbreviation('f', '\u092B')
keyboard.add_abbreviation('b', '\u092C')
keyboard.add_abbreviation('bh', '\u092D')
keyboard.add_abbreviation('m', '\u092E')
keyboard.add_abbreviation('y', '\u092F')
keyboard.add_abbreviation('r', '\u0930')
keyboard.add_abbreviation('l', '\u0932')
keyboard.add_abbreviation('rd', '\u0933')
keyboard.add_abbreviation('v', '\u0935')
keyboard.add_abbreviation('sh', '\u0936')
keyboard.add_abbreviation('Sh', '\u0937')
keyboard.add_abbreviation('s', '\u0938')
keyboard.add_abbreviation('h', '\u0939')


# Block forever, like `while True`.
keyboard.wait()
