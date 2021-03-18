def read_file(filename):  # 投入參數，在此為檔名	#3
	
	lines = [] # 創造lines空清單
	
	with open(filename, 'r', encoding='utf-8-sig') as f:  # sig為去掉記憶體編碼	#4
		for line in f: # 一行一行列出，每一行為一個line
			lines.append(line.strip()) # 把每一行line裝進lines清單
	return lines	#5

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person+': '+line)
	return new

def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('input.txt') # 給檔名		#2
	lines = convert(lines)
	write_file('output.txt',lines)
	
main()	# 使用main這個function，亦為程式進入點		#1