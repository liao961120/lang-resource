#%%
import os

#%%
def main():
    OUTFILE_haszh = 'ptt_terms-has_chinese.txt'
    OUTFILE_allzh = 'ptt_terms-all_chinese.txt'
    punc = set('，、：；。:;,')

    with open("ptt_terms.csv") as f:
        
        terms_haszh = set()
        terms_allzh = set()

        for i, line in enumerate(f):
            if i == 0: continue
            term = ','.join(line.strip().split(',')[:-1])
            terms = ''.join(c if c not in punc else '\u3000' for c in term).split('\u3000')
            
            # Check presence of chinese
            for t in terms:
                if has_zh(t): 
                    terms_haszh.add(t)
                    if all_zh(t):
                        terms_allzh.add(t)

    # Save files
    with open(OUTFILE_haszh, 'w') as f:
        for t in terms_haszh:
            f.write(t)
            f.write('\n')
    with open(OUTFILE_allzh, 'w') as f:
        for t in terms_allzh:
            f.write(t)
            f.write('\n')



# Helper
def has_zh(x: str):
    for char in x:
        if (char > u'\u4e00' and char < u'\u9fff') or (char > u'\u3400' and char < u'\u4DBF'):
            return True

    return False


def all_zh(x: str):
    for char in x:
        if not ((char > u'\u4e00' and char < u'\u9fff') or (char > u'\u3400' and char < u'\u4DBF')):
            return False
    
    return True


if __name__ == "__main__":
    main()