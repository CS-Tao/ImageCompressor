#!/usr/bin/env python
from optparse import OptionParser
from ImageCompressor import Compressor

def main():
    """主函数"""
    parser = OptionParser()
    parser.add_option('-i', '--input', dest='input_dir', help='源图片目录', metavar='INPUT_DIR')
    parser.add_option('-o', '--output', dest='output_dir', help='压缩后的图片输出目录', metavar='OUTPUT_DIR')
    parser.add_option('-s', '--scale', dest='scale', help='压缩比，取值有1、2、3、4，值越大，生成的图片越小', metavar='SCALE')
    (options, args) = parser.parse_args()
    tool = Compressor.Compressor()
    tool.compress(options.input_dir, options.output_dir, mode=options.scale)

if __name__ == '__main__':
    main()
    print('program exited with status 0.')
    input()