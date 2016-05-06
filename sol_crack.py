from pycipher import Solitaire
from pycryptanalysis import ngram

# Initialising cipher

cipher_text = "IUTWMVVHVRORNXZZAGPPJSLVPFDLVZMEVGJIVYDZPNAPKQXCIZLGRZWNNCSVKPQTMLKPQNWPGOAYVAPQIPQWRMIXPBTCCEGWHLOZQRFYZGHEJCFETFRULYBLUDNHNYGBEKBKSNXYMRCTHNLXHKHKDFCBBWGVJQBLIESQAJWVLZQTLLASRESDVJMRTBJDOVOAJPQQIVYZHFAFQBHGMVOSDEXBYHKSPYSQLDFRZFYJHEDWPZMVBDCRIYALMMVQWJHVIPDUCKFVZBXMDQVBMXOKODOGYEBWLACFMUVQNSQRKMMNWZBEOOUEXIYDJWUJICKRFQLCESIKHCJQRUFPRRGYHSTZNWOSPAZULTCZPRSOYVETXLLAQMJMVUSOPLCEWYLJUADSJGTLOHOXRHSPZGLADFFAHORATZOBMRVVFDWANXPGUNQGLIHGTRMWBJMFTALCCPZGVLCSINPBUWOVPYXUQUZKTGLTVRZLIRRFNWUULJIVFMEVFIPUNCMDUZAGRHDACDPFKTHTKDKOGUSPYENXTPQUROUZTWCMIGPCKLYWZGUWJRLVKNKQKGPDQNABIRLPVKHOMWXWCQTLGWHXBJFYGIVIWWJXWAVUCOFKJUMZKXKKOEGOETLRAKQVMGKOABGIXQLQMBJYBJUOIZRWHKZCDSMNHMWTRSDBSRULECERARYGFDPERECYGULSJCJWVMLNRZXKQRTTSZWJUVSUXLGKMQPHJWAUBUEJXKYAXCEBLGJHTNKTNZSGYLOFUZUTLNYBHBKGKSCDWIYUXXFYJPNTAFKBGCNLJVGTKDCNBHUSAZRBWSXKICXDISPIRYEOIVXZAWAZIFPGAUYDQSWYCSIQDENTCTAONTOBCIVFYPVPDEMUHDPNTSUOSWVMLXECSHCMHESCGWSUSTAYHKUMOXUFEANTUHNDZHZFLRSHCZBASXPPMCNWMSJTANASBRPHDWJUCTTGMHNTTPIGTVJWWNFUWEOZMCIQMDZDJGLKSSYOXIBGIHPZOMNYBORFNCBTNUHQDOPUOFCCLDFUHIPMKCZKCZVZNMFLWOKIZFKINWQNROAZYLCTMUZYUGOUIMEQSQQAAIQVYQRSPZPUXUNBAORFDDASVMADOGRNPBPKNXGXQOKSEHEAJNZNMQIUMPLHWUFWLEOBKPIASZALJPZQUIKJSGKPGEGMPFBUNHOFKXTSCJMTYBUJEBYNNEVQHKNTIUJBJEEUSQOINRDAZUQMEWEELBLBSGUGXDXLWTUEODCKZYXJUODPPGBSPLAKHPKUZYVWGXMVXEAENQYBPKSDJMTZIBEYMTOFWCVOYZLJSKXGBKAHDTZAMZSFPGPYFFWRBHLNXOAXOITZVFBEXAKVYPAYTIRZMRKIYZRKIQNSDOINPTWMACVOJCXWCOXCEAJBQULUYWQLRERSUIIQTBASGUMAORADTIWOIDHEWLYZBADGFMHHWXNQCZKFTBVJRSYMKGTMLRGNHPUZYOVAOGTVHKHHEQBKTHJYBCUONPEUPDPJMLEOZILYNABGMPEEVJHKADCUEHMNEFWJURTJKTBKZSMTKYPCRVGFPHEIDVFSVNFUMSYAXJAVGMDSZRMHMQVSUEKUWFZFRYOROKWORNQUNJXBHNZAYXWWBEISHIQBOJAAYEKWMGJLGHFDRKBEJTQUQKVRHNJGFHARSOXBRZHKTJFJFNRXQZQRMFKNXRWLVCZBZSFQAOCLPZSGIOTMXTQHBHVYVRYIUSKFXFPKNSQITSRMYGRYXWRFQMBBMJTYOCDTTW"
#cipher_text = "XOJGMGFQSMVPYUGZ"
sol = Solitaire(cipher_text)

# Opening key file
key_file = open("key.lis", "r")

# Initialising cipher test

quadgrams = ngram("quadgrams.txt")
bestscore = -1000000

for i in range(0,40320):
    key_str = key_file.readline()
    if i==10998:
        key = [int(string) for string in key_str.split(",")]
        plain_text = sol.decipher(key)
        plain_text = plain_text.upper()
        score = quadgrams.run(plain_text)
        if score >= bestscore:
            print i
            bestscore = score    
            print score
            print plain_text
            print key
    
