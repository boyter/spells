import random


def random_name():
    length = random.randint(2, 3)
    
    first = ['acc', 'agua', 'alo', 'apa', 'ke', 'ava', 'avi', 'max', 'bomb', 'collo', 'con', 'cru', 'de', 'den', 'dif', 'dis', 'du', 'en', 'epi', 'eva', 'pat', 'ex', 'ver', 'fer', 'fer', 'fid', 'in', 'fi', 'fla', 'fli', 'fur', 'gem', 'hom', 'immo', 'imp', 'incar', 'in', 'legi', 'le', 'levi', 'liber', 'mor', 'loco', 'lu', 'mobil', 'mors', 'muff', 'ob', 'orc', 'tot', 'pet', 'por', 'incan', 'pri', 'pro', 'quie', 'red', 'rel', 'rev', 'rep', 'rev', 'wing', 'wad', 'ter', 'tar', 'stupe', 'sono', 'sil', 'ser', 'sec', 'scour', 'sal', 'hex', 'rid', 'rict']
    middle = ['men', 'ho', 'rec', 'dav', 'for', 'ar', 'port', 'frin', 'fun', 'juncti', 'let', 'sau', 'fin', 'sen', 'gor', 's', 'nes', 'ron', 'pec', 'pelli', 'el', 'canta', 'ni', 'gra', 'pen', 'nun', 'in', 'or', 'bu', 'dim', 'er', 'car', 'cen', 'li', 'vi', 'a', 'mo', 'liar', 'li', 'mor', 'lia', 'livi', 'hid', 'al', 'rif', 'ta', 'to', 'ash', 'ner', 'el', 'gar', 'di', 'ant', 'en', 'pen', 'tum', 'gi', 'diku', 'e']
    last = ['io', 'ti', 'mora', 'ium', 'ra', 'da', 's', 'ima', 'da', 'us', 'go', 'dus', 'vitis', 'cio', 'rius', 'geo', 'do', 'dium', 'ro', 'gio', 'key', 'co', 'um', 'to', 'armus', 'to', 'a', 'ula', 'ius', 'tem', 'te', 'do', 'culus', 'phus', 'lus', 'enta', 'io', 'vius', 'rous', 'dio', 'mens', 'tis', 'tor', 'mos', 'bus', 'corpus', 'dre', 'to', 'ate', 'eous', 'us', 'icus', 'tato', 'or', 'go', 'tus', 'ucio', 'ucto', 'io', 'vate', 'aro', 'lo', 'lio', 'dium', 'wasi', 'geo', 'allegra', 'fy', 'rus', 'cio', 'sortia', 'sempra', 'vio', 'ia', 'lus']

    name = ''
    if length == 2:
        name = random.choice(first) + random.choice(last)
    if length == 3:
        name = random.choice(first) + random.choice(middle) + random.choice(last)
    return name.capitalize()

def random_spell():
    length = random.randint(1, 2)
    if length == 1:
        return random_name()
    return random_name() + ' ' + random_name()


if __name__ == "__main__":
    for x in range(500):
        print random_spell()