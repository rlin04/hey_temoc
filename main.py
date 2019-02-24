from CrawlRoot import CrawlRoot
from pathlib import Path
from difflib import get_close_matches

def getMatch(patterns, word):
    print(get_close_matches (word, patterns))


def main():
    #my_file = Path("/csvfile.csv")
    #if not my_file.exist():
    CrawlRoot().url_to_csv()
    print(CrawlRoot().find_answer("What is the purpose and scope of UT Dallas's participation in Historically Underutilized Business (HUB) Development?".lower()))


if __name__ == "__main__":
    main()
