
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *
# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),

    to_Conv_color_3("input_1", 16, 512, offset="(0,1.5,0)", to="(0,0,0)", height=1, depth=20, width=1,caption=" "),#64
    to_Conv_color_3("input_2", 16, 512, offset="(0,-1.5,0)",to="(0,0,0)", height=1, depth=20, width=1,caption=" "),#64
    to_Sum( "sum", offset="(1.5,2,0)", to="(input_2-east)", radius=2.5, opacity=0.6),
    to_connection( "input_1", "sum"),
    to_connection( "input_2", "sum"),
    to_Conv_color_4("Conv_1", 16, 512, offset="(1.5,0,0)",to="(sum-east)", height=1, depth=40, width=1,caption=" "),#128
    to_connection( "sum", "Conv_1"),
    to_Conv_color_4("Conv_2", 16, 512, offset="(1.5,0,0)", to="(Conv_1-east)", height=1, depth=80, width=1, caption=" "),#256
    to_connection("Conv_1", "Conv_2"),
    to_Conv_color_4("Conv_3", 16, 512, offset="(1.5,0,0)", to="(Conv_2-east)", height=1, depth=40, width=1, caption=" "),#128
    to_connection("Conv_2", "Conv_3"),
    to_Conv_color_4("Conv_4", 16, 512, offset="(1.5,0,0)", to="(Conv_3-east)", height=1, depth=2, width=1, caption=" "),#128
    to_connection("Conv_3", "Conv_4"),
    to_end()


    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
