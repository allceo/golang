import os
import sys
import string
from optparse import OptionParser
import urllib.request
import chardet

def main():
    '''Run the main program'''
    usage="%prog [options]"
    parser=OptionParser(usage)
    parser.add_option("-u", "--url", action="store", type="string", dest="urlValue",
        help="访问的网址。")
    (options,args)=parser.parse_args()
    if options.urlValue != None:
        geturl(options.urlValue)
    else:
        print('urlValue is null,please input url.')

def geturl(url):
	try:
		wp = urllib.request.urlopen(url)
		content = wp.read()
		print(chardet.detect(content))
		typeEncode = sys.getfilesystemencoding()##系统默认编码
		print(typeEncode)
		infoencode = chardet.detect(content).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
		str_content = content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出
		#str_content = content.decode(chardet.detect(content)['encoding'],'ignore')
		fp = open("web.txt","w")
		fp.write(str_content)
		fp.close() 
	except KeyboardInterrupt as e:
		print >> sys.stderr, 'Program interrupted, exiting...'
		sys.exit(10)

if __name__ == '__main__':
        main()