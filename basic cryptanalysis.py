from pprint import pprint
cipher_string='btnpufhz esxfh vyhvefz ufhez xsgfnafcfz umabtfz qz kmhmgsjfg ghndf tiufhzumbfz ahneez ydsdafhfzasdw uhnanbne pmdwefz lmeeumufhz oymgz tnuz kmdz vncfz pmdwfgz dmsxf ltmbq wmz zdmsez zmiz pszkfmayhf aydf zyd zumdwef vvzfz wnvvefz khfflmhf tmpzafhz bndz sdksdsasfz mpnfvmz athmztfz tmppfh tfcfz bivfhuydq gnldfg ghsxfh pmdwefh zuskki zlmv zunnksdw gfmgfh ahsxsme dyqfg kemw pmhwsdme byvsdwfg enzfhz uzfygn bhsuueflmhf bmebyemanhz gnldsdw pydwz uyzt xmc uydafg zbhffd gsf enzfh difalnhq kenlbtmhaz venbqfg ayvf vmhkz zbmw jfhnfz ggfg kemxnh vhnqf vmhkfg kemxnhz pyaafhfg tmppfhsdw byvfz befmdfg hnvyzafh kenngsdw vhfmqz zunsefhz knzzsez bhmindz yhe ufzzspmefg bhfasdz hmdgnpdfzz bhfmasndszpz zsenz jnhbtsdw bnnqsf bendf oyfzfz meaz zpnqf zuffgnpfafh ztmhflmhf'
dictionary = dict(A='0',B='0',C='0',D='0',E='0',F='0',G='0',H='0',I='0',J='0',K='0',L='0',M='0',N='0',O='0',P='0',Q='0',R='0',S='0',T='0',U='0',V='0',W='0',X='0',Y='0',Z='0',a='0',b='0',c='0',d='0',e='0',f='0',g='0',h='0',i='0',j='0',k='0',l='0',m='0',n='0',o='0',p='0',q='0',r='0',s='0',t='0',u='0',v='0',w='0',x='0',y='0',z='0')
dict_result= dict()
dict_temp = dict()
dict_final = dict()
final_score = 0
result = []
#decipher_string = 'skulker choke minifloppies scratched recursions hairiest boas dps twiddles orthogonal posers stoppage echo cranking roached trawling saying confusers sysop bytes punting minifloppieses patch ruder pop urchin zaps lase post bit incantation barns munches trawl newsgroups wins scrogs gnarliest arena losses compressing funkiest musics fences wanked drivers weasel dinker phases nuke driver globed biffed slops patches deltas bombed bouncing cripplewares dec tubes grunge pasties trashing hats whacking hairballs pmed drone fools urls pushing twiddle phage screen segmented foregrounded spoiler profiles blts bounced tourists clean clobbers pods gobble con cubings snailing download rfcs hose widget compacter adas glitched crumb mailbombs snark'
decipher_string = 'chompers liver burbles perls videotexes patches ks faradized drone hyperspaces trolls uninteresting protocol mangles wallpapers quads hops fans boxes mangeds naive whack gas snails says misfeature tune sun spangle bbses gobbles freeware hamsters cons infinities amoebas thrashes hammer hexes cyberpunk downed driver mangler spiffy swab spoofing deader trivial nuked flag marginal cubinged losers pseudo crippleware calculators downing mungs push vax punted screen die loser nyetwork flowcharts blocked tube barfs scag zeroes dded flavor broke barfed flavors muttered hammering cubes cleaned robuster flooding breaks spoilers fossils crayons url pessimaled cretins randomness creationisms silos zorching cookie clone queses alts smoke speedometer shareware'
def remove_duplicate(i):
	
	element = dict_result[chr(i+ord('a'))].pop()
	dict_result[chr(i+ord('a'))].add(element)
	for j in range(26):	
		if len(dict_result[chr(j+ord('a'))])>1 and i!=j:
			try:
				dict_result[chr(j+ord('a'))].remove(element)
				if len(dict_result[chr(j+ord('a'))])==1:
					remove_duplicate(j)
			except:
				pass
	return 
	
def score_key(dict_temp):
	post_substitute =[]
	score=0
	pre_substitute = list(cipher_string)
	for char in pre_substitute:
		try:
			post_substitute.append(dict_temp[char][0])
		except KeyError:
			post_substitute.append(char)
	deciphered_text=''.join(post_substitute)
	deciph_words = deciphered_text.split()
	for word in deciph_words:
		if word in a:
			score = score + 1
	return score
	
def iso(string1,string2):
	list1 =[]
	list2 =[]
	if len(string1)!=len(string2):
		return False
	for i in xrange(len(string1)):
		
		if string1[i] in list1:
			if dictionary[string1[i]]!= string2[i]:
				return False
			else:
				continue
		elif string2[i] in list2:
			return False
			
		dictionary[string1[i]]=string2[i]	
			
		list1.append(string1[i])
		list2.append(string2[i])
	return True
	
def possible_key_set_test(j):
	global final_score
	global dict_final
	for i in range(26):
		if len(dict_result[chr(i+ord('a'))]) >1 and i!=j:
			candidate = dict_result[chr(i+ord('a'))]
			for can in candidate:
				dict_result[chr(i+ord('a'))] = [can]
				possible_key_set_test(i)
	
	score = score_key(dict_result)
	print (score)
	if score > final_score:
		final_score = score 
		dict_final = dict_result
	return
with open('dictionary.txt','r') as fp:
	a = fp.read().split('\n')
	a=map(str.lower,a)
	
	s=cipher_string.split()
	#initialize
	for i in range(26):
		dict_result[chr(i+ord('a'))]=set()
	#find word isomophism with dictionary return intersection
	for ciphered in s:
		for decipher in a:
			if iso(ciphered,decipher):
				#print (ciphered,decipher)
				for i in range(len(ciphered)):
					
					if 'mark' not in dict_result[ciphered[i]]:
						try:
							dict_result[ciphered[i]].add(decipher[i])
						except:
							dict_result[ciphered[i]]=set(decipher[i])
					else:
						try:
							dict_temp[ciphered[i]].add(decipher[i])
						except:
							dict_temp[ciphered[i]]=set(decipher[i])
		
		for letter in set(list(ciphered)):
			if 'mark' in dict_result[letter]:
				dict_result[letter] = dict_result[letter]&dict_temp[letter]
				dict_temp[letter] = set()
			dict_result[letter].add('mark')
	#remove the 'mark'
	for i in range(26):
		try:
			dict_result[chr(i+ord('a'))].remove('mark')
		except:
			pass
	#remove duplicate
	for i in range(26):	
		if len(dict_result[chr(i+ord('a'))]) ==1:
			remove_duplicate(i)
	#convert set to list
	for i in range(26):	
		dict_result[chr(i+ord('a'))]=list(dict_result[chr(i+ord('a'))])
	
	#score key sets
	possible_key_set_test(-1)	
				
	pprint (dict_result)
	pprint (dict_final)		
	
	temp_string = list(cipher_string)
	for s in temp_string:
		try:
			result.append(dict_final[s][0])
		except KeyError:
			result.append(s)
	result = ''.join(result)		
	#print (result)
	if result == decipher_string:
		print ('ok')