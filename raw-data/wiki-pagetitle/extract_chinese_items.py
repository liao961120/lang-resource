#%%
import os


#%%
def main():
    OUTFILE_haszh = 'zhwiki-20200620-titles-has_chinese.txt'
    OUTFILE_allzh = 'zhwiki-20200620-titles-all_chinese.txt'

    with open("zhwiki-20200620-all-titles") as f:
        
        titles_haszh = set()
        titles_allzh = set()

        for line in f:
            namespace, title = line.strip().split('\t')
            
            # Check presence of chinese
            if has_zh(title): 
                titles_haszh.add(title)
                if all_zh(title):
                    titles_allzh.add(title)


    # Save files
    with open(OUTFILE_haszh, 'w') as f:
        for title in titles_haszh:
            f.write(title)
            f.write('\n')
    with open(OUTFILE_allzh, 'w') as f:
        for title in titles_allzh:
            f.write(title)
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