import urllib3
import certifi
import csv
from bs4 import BeautifulSoup


class CrawlRoot:
    def url_to_csv(self):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        url = "https://faq.utdallas.edu/en"

        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, features="html.parser")
        # find all the corresponding question and their answer. put in dictionary
        # (intent:question):answer
        main_list = []
        more_list = []
        url_2 = 'https://faq.utdallas.edu'
        # find more links
        for link in soup.findAll('li', {'class': 'article article-more'}):
            more_list.append(url_2 + link.find('a')['href'])
        for more_url in more_list:
            response = http.request('GET', more_url)
            soup = BeautifulSoup(response.data, features="html.parser")
            for link in soup.findAll('li', {'class': 'article less-important'}):
                question = link.find('a').text
                url = (url_2+link.find('a')['href'])
                intent = self.find_intent(question)
                iq_array = [intent, question, url]
                # create array (intent:question)
                main_list.append(iq_array)
            # headers = ['question', 'url']
            with open('csv_file.csv', mode='w') as csv_file:
                writer = csv.writer(csv_file, delimiter = ',', lineterminator='\n')
                for i in main_list:
                    writer.writerow([i[0].lower(), i[1].lower(), i[2].lower()])
                    # print(question + " " + url)

    def find_intent(self, question):
        # initialize list of intents
        list_intents = ['why']
        for l in list_intents:
            if question.__contains__(l):
                return l
        return "none"


    def find_answer(self, question):

        with open('csv_file.csv', mode='r') as csv_file:
            url = ""
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if question == row[1]:
                    url = row[2]

        # find the answer
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, features="html.parser")
        return soup.find('div', {'class': 'col-md-9 text-content'}).find('p').text

