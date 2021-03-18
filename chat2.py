def read_file(filename):  # 投入參數，在此為檔名	#3
	
	lines = [] # 創造lines空清單
	
	with open(filename, 'r', encoding='utf-8-sig') as f:  # sig為去掉記憶體編碼	#4
		for line in f: # 一行一行列出，每一行為一個line
			lines.append(line.strip()) # 把每一行line裝進lines清單
	return lines	#5

def convert(lines):
	new = []
	person = None
	Chen_word_count = 0
	JoyceSun_word_count = 0
	Chen_image_count = 0
	Joyce_image_count = 0
	Chen_sticker_count = 0
	Joyce_sticker_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]

		if name == '陳君誌':

			if s[2] == '圖片':
				Chen_image_count += 1

			elif s[2] == '貼圖':
				Chen_sticker_count += 1

			for m in (s[2]):
				Chen_word_count += len(m)

		elif name == 'Joyce':

			if s[3] == '圖片':
				Joyce_image_count += 1

			elif s[3] == '貼圖':
				Joyce_sticker_count += 1

			for m in (s[3]):
				JoyceSun_word_count += len(m)

	print('陳君誌說了', Chen_word_count,'個字，','傳了',Chen_image_count,'個圖片，','傳了',Chen_sticker_count,'個貼圖')
	print('Joyce說了', JoyceSun_word_count,'個字，','傳了',Chen_image_count,'個圖片，','傳了',Chen_sticker_count,'個貼圖')

		 #print(s)

	return new

def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('JoyceSun.txt') # 給檔名		#2
	lines = convert(lines)
	# write_file('output.txt',lines)
	
main()	# 使用main這個function，亦為程式進入點		#1