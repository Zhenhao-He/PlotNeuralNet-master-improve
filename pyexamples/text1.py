
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *
# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),

    to_Conv("imput", s_filer=16, n_filer=512, offset="(0,0,0)", to="(0,0,0)", height=16, depth=16, width=12, caption=" "),#输入层

    *block_Conv_norm_relu( name='1_Conv_1', botton='imput', middle='1_norm_1', top='1_relu_1', s_filer=16, n_filer=256, offset="(1.5,2.5,0)", size=(16,16,4)),
    *block_Conv_norm_relu( name='1_Conv_2', botton='1_relu_1', middle='1_norm_2', top='1_relu_2', s_filer=16, n_filer=512, offset="(1,0,0)", size=(16,16,8)),
    *block_Conv_norm_relu( name='1_Conv_3', botton='1_relu_2', middle='1_norm_3', top='1_relu_3', s_filer=16, n_filer=256, offset="(1,0,0)", size=(16,16,4)),
    *block_Conv_norm_relu( name='1_Conv_4', botton='1_relu_3', middle='1_norm_4', top='1_relu_4', s_filer=16, n_filer=512, offset="(1,0,0)", size=(16,16,8)),
    to_Conv("1_Conv_5", 16, 512, offset="(1,0,0)", to="(1_relu_4-east)", height=16, depth=16, width=1.5, caption=" " ),
    to_SoftMax( "SoftMax", s_filer=16, offset="(0,0,0)", to="(1_Conv_5-east)", width=0.5, height=16, depth=16, opacity=0.5, caption=" " ),
    to_connection( "1_relu_4", "1_Conv_5"),

    to_Conv_color_1("MLP_input_1_1", 16, 512, offset="(1,0,0)", to="(SoftMax-east)", height=1, depth=5, width=1, caption=" " ),
    to_Conv_color_1("MLP_input_1_2", 16, 512, offset="(0,0,0)", to="(MLP_input_1_1-east)", height=1, depth=5, width=1, caption=" " ),
    to_Conv_color_1("MLP_input_1_3", 16, 512, offset="(0,0,0)", to="(MLP_input_1_2-east)", height=1, depth=5, width=1, caption=" " ),
    to_connection( "SoftMax", "MLP_input_1_1"),

    to_Conv_color_1("MLP_input_2_1", 16, 512, offset="(1,0,0)", to="(MLP_input_1_3-east)", height=1, depth=20, width=1, caption=" " ),
    to_Conv_color_1("MLP_input_2_2", 16, 512, offset="(0,0,0)", to="(MLP_input_2_1-east)", height=1, depth=20, width=1, caption=" " ),
    to_Conv_color_1("MLP_input_2_3", 16, 512, offset="(0,0,0)", to="(MLP_input_2_2-east)", height=1, depth=20, width=1, caption=" " ),
    to_connection( "MLP_input_1_3", "MLP_input_2_1"),

    to_Conv_color_1("MLP_out_1_1", 16, 512, offset="(1,0,0)", to="(MLP_input_2_3-east)", height=1, depth=40, width=1,caption=" "),
    to_Conv_color_1("MLP_out_1_2", 16, 512, offset="(0,0,0)", to="(MLP_out_1_1-east)", height=1, depth=40, width=1,caption=" "),
    to_Conv_color_1("MLP_out_1_3", 16, 512, offset="(0,0,0)", to="(MLP_out_1_2-east)", height=1, depth=40, width=1,caption=" "),
    to_connection("MLP_input_2_3", "MLP_out_1_1"),

    *block_Conv_norm_relu( name='2_Conv_1', botton='imput', middle='2_norm_1', top='2_relu_1', s_filer=16, n_filer=256, offset="(1.5,-2.5,0)", size=(16,16,4)),
    *block_Conv_norm_relu( name='2_Conv_2', botton='2_relu_1', middle='2_norm_2', top='2_relu_2', s_filer=16, n_filer=512, offset="(1,0,0)", size=(16,16,8)),
    *block_Conv_norm_relu( name='2_Conv_3', botton='2_relu_2', middle='2_norm_3', top='2_relu_3', s_filer=16, n_filer=256, offset="(1,0,0)", size=(16,16,4)),
    *block_Conv_norm_relu( name='2_Conv_4', botton='2_relu_3', middle='2_norm_4', top='2_relu_4', s_filer=16, n_filer=512, offset="(1,0,0)", size=(16,16,8)),
    to_Conv("2_Conv_5", 16, 512, offset="(1,0,0)", to="(2_relu_4-east)", height=16, depth=16, width=4, caption=" " ),
    to_connection("2_relu_4", "2_Conv_5"),

    to_Conv_color_2("MLP_out_2_1", 16, 512, offset="(3.5,0,0)", to="(2_Conv_5-east)", height=1, depth=40, width=1,caption=" "),
    to_Conv_color_2("MLP_out_2_2", 16, 512, offset="(0,0,0)", to="(MLP_out_2_1-east)", height=1, depth=40, width=1,caption=" "),
    to_Conv_color_2("MLP_out_2_3", 16, 512, offset="(0,0,0)", to="(MLP_out_2_2-east)", height=1, depth=40, width=1,caption=" "),
    to_connection("2_Conv_5", "MLP_out_2_1"),

    to_Sum( "sum", offset="(3,2.5,0)", to="(MLP_out_2_3-east)", radius=2.5, opacity=0.6),
    #to_skip( of='MLP_out_2_3', to='sum', pos=-0.5),
    to_connection("MLP_out_2_3", "sum"),
    to_connection("MLP_out_1_3", "sum"),

    to_Conv_color_3("MLP_out_3_1", 16, 512, offset="(1,0,0)", to="(sum-east)", height=1, depth=40, width=1,caption=" "),
    to_Conv_color_3("MLP_out_3_2", 16, 512, offset="(0,0,0)", to="(MLP_out_3_1-east)", height=1, depth=40, width=1,caption=" "),
    to_Conv_color_3("MLP_out_3_3", 16, 512, offset="(0,0,0)", to="(MLP_out_3_2-east)", height=1, depth=40, width=1,caption=" "),
    to_connection("sum", "MLP_out_3_1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
