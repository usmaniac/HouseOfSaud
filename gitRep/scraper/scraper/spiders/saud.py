import scrapy
from .lineage import *
import json
import re
import pymongo
from pymongo import MongoClient



class QuotesSpider(scrapy.Spider):
    name = "saudScraper"
    start_urls = [
        "https://www.google.com/search?q=ibn+saud+sons&oq=ibn+saud+sons&aqs=chrome..69i57j35i39j0l3j69i61j69i60l2.6975j0j7&sourceid=chrome&ie=UTF-8"
    ]
    mdict = {}
    exceptions = {'Muhammad bin Abdulaziz Al Saud':'https://www.google.com/search?sa=X&sxsrf=ACYBGNSztgGW43YPwbD2bJNb6keaZ0FwjQ:1580971675666&q=muhammad+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LUz9U3MDcrrzDXkspOttIvSM0vyEkFUkXF-XlWyRmZOSlFqXmLWNVzSzMSc3MTUxSSMvMUEpNSSnMSqzKrFBJzFIoTS1MUYCoBwvsHWFMAAAA&ved=2ahUKEwiW3IK5qrznAhXRmuYKHWH5D6gQ44YBKAIwGXoECA4QJA&biw=1440&bih=718&dpr=2',
    'Ahmed bin Abdulaziz Al Saud':'https://www.google.com/search?sa=X&sxsrf=ACYBGNSy2L9sYbJV9Tj6vr7Pl07qUq40MQ:1580972526542&q=ahmed+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LUz9U3MMvIqCzUkspOttIvSM0vyEkFUkXF-XlWyRmZOSlFqXmLWFUSM3JTUxSSMvMUEpNSSnMSqzKrFBJzFIoTS1MUYMoAocIzG1AAAAA&ved=2ahUKEwjjgeDOrbznAhXb8XMBHawaBLMQ44YBKAIwInoECA0QIA&biw=1440&bih=718',
    'Mamdouh bin Abdulaziz Al Saud':'https://www.google.com/search?sa=X&sxsrf=ACYBGNQhYPNHymDWUZnkmN9A-6yOode5-Q:1580972628793&q=mamdouh+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LSz9U3yDaoMMpO1pLKTrbSL0jNL8hJBVJFxfl5VskZmTkpRal5i1jVchNzU_JLMxSSMvMUEpNSSnMSqzKrFBJzFIoTS1MUYAoBOyhKaFMAAAA&ved=2ahUKEwik8MD_rbznAhV87XMBHSRWBXoQ44YBKAIwG3oECAwQHg&biw=1440&bih=718',
    'Turki II bin Abdulaziz Al Saud': 'https://www.google.com/search?sa=X&sxsrf=ACYBGNSOlNulSvpv3V5Eh0my8rJki3aATQ:1580972460784&q=turki+ii+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LSz9U3MDJPMk420pLKTrbSL0jNL8hJBVJFxfl5VskZmTkpRal5i1jVS0qLsjMVMjMVkjLzFBKTUkpzEqsyqxQScxSKE0tTFGAqAagKE99UAAAA&ved=2ahUKEwjyzLKvrbznAhVeH7cAHaHuBBIQ44YBKAIwG3oECA0QKA&biw=1440&bih=718',
    'Bandar bin Abdulaziz Al Saud':'https://www.google.com/search?sa=X&sxsrf=ACYBGNS87FUjUp71zjDDwcPNu-ZWUwxMPQ:1580972493339&q=bandar+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LSz9U3MDK3LEtL05LKTrbSL0jNL8hJBVJFxfl5VskZmTkpRal5i1hVkxLzUhKLFJIy8xQSk1JKcxKrMqsUEnMUihNLUxRg6gD9D9Z1UgAAAA&ved=2ahUKEwiCxvW-rbznAhUt73MBHbBEABIQ44YBKAMwHXoECA0QJw&biw=1440&bih=718',
    'Saad bin Abdulaziz Al Saud': 'https://www.google.com/search?sxsrf=ACYBGNQCFoNf06CUH9GKKhK7PR4uKENdpA:1581086821514&q=saad+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LSz9U3yDayNDZL1pLKTrbSL0jNL8hJBVJFxfl5VskZmTkpRal5i1iVixMTUxSSMvMUEpNSSnMSqzKrFBJzFIoTS1MUYKoA8XCPsFAAAAA&sa=X&ved=2ahUKEwjCyuuy17_nAhWy_XMBHXzRASkQ44YBKAIwInoECA4QFA&sxsrf=ACYBGNQCFoNf06CUH9GKKhK7PR4uKENdpA:1581086821514&biw=1440&bih=717',
    'Mishaal bin Abdulaziz Al Saud':'https://www.google.com/search?sa=X&sxsrf=ACYBGNQdLNRunblTsq8v25tCNM2Cbqiwkw:1581396306686&q=mishaal+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LUz9U3SC_IS0nWkspOttIvSM0vyEkFUkXF-XlWyRmZOSlFqXmLWNVyM4szEhNzFJIy8xQSk1JKcxKrMqsUgALFiaUpCjCFAFcz4d9SAAAA&ved=2ahUKEwisqu-o2MjnAhWJSJQKHcKfBzMQ44YBKAIwG3oECA4QIA&biw=1440&bih=717&dpr=2',
    'Badr bin Abdulaziz Al Saud': 'https://www.google.com/search?sxsrf=ACYBGNQFrUlRnjaBho9zQTfzDehWQiFzYg:1581398606655&q=badr+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LSz9U3MDJPMio315LKTrbSL0jNL8hJBVJFxfl5VskZmTkpRal5i1iVkxJTihSSMvMUEpNSSnMSqzKrFBJzFIoTS1MUYKoASRnWkFAAAAA&sa=X&ved=2ahUKEwinrsrx4MjnAhUGrpQKHW0jCZ4Q44YBKAIwInoECA0QFw&sxsrf=ACYBGNQFrUlRnjaBho9zQTfzDehWQiFzYg:1581398606655&biw=1440&bih=717',
    'Abdul-Rahman bin Abdulaziz Al Saud':'https://www.google.com/search?sxsrf=ACYBGNTFES8yU0RF5FP7TvtR8CEfGJeriw:1581398670499&q=abdul-rahman+bin+abdulaziz+al+saud+children&stick=H4sIAAAAAAAAAOPgE-LSz9U3MDJPMrJI0pLKTrbSL0jNL8hJBVJFxfl5VskZmTkpRal5i1i1E5NSSnN0ixIzchPzFJIy8xTAAolVmVUKiTkKxYmlKQow1QB9VCHUWAAAAA&sa=X&ved=2ahUKEwj8joOQ4cjnAhXW62EKHRA-AacQ44YBKAIwJ3oECA0QEw&sxsrf=ACYBGNTFES8yU0RF5FP7TvtR8CEfGJeriw:1581398670499&biw=1440&bih=717'}

    mothers = {'Abdul Majeed bin Abdulaziz Al Saud':'Haya bint Saad Al Sudairi', 
    'Salman bin Abdulaziz': 'Hassa Al Sudairi', 
    'Badr bin Abdulaziz Al Saud':'Haya bint Saad Al Sudairi', 
    'Hathloul bin Abdulaziz Al Saud':'Saida al Yamaniyah', 
    'Mishari bin Abdulaziz Al Saud':'Bushra', 
    'Fawwaz bin Abdulaziz Al Saud':'Bazza II', 
    'Thamir bin Abdulaziz Al Saud':'Nouf bint Al Shalan', 
    'Hamoud bin Abdulaziz Al Saud':'Futayma', 
    'Sattam bin Abdulaziz Al Saud':'Mudhi', 
    'Majid bin Abdulaziz Al Saud':'Mudhi', 
    'Mamdouh bin Abdulaziz Al Saud':'Nouf bint Al Shalan', 
    'Turki II bin Abdulaziz Al Saud':'Hassa Al Sudairi', 
    'Nasser bin Abdulaziz Al Saud':'Bazza I', 
    'Nawwaf bin Abdulaziz Al Saud':'Munaiyir', 
    'Saad bin Abdulaziz Al Saud':'Jawhara bint Saad bin Abdul Muhsin al Sudairi', 
    'Abdul Muhsin bin Abdulaziz Al Saud':'Jawhara bint Saad bin Abdul Muhsin al Sudairi', 
    'Mansour bin Abdulaziz Al Saud':'Shahida', 
    'Abdul Elah bin Abdulaziz Al Saud':'Haya bint Saad Al Sudairi', 
    "Musa'id bin Abdulaziz Al Saud":'Jawhara bint Saad bin Abdul Muhsin al Sudairi', 
    'Turki I bin Abdulaziz Al Saud':'Wadhah bint Muhammad Al Hussein Al Orair', 
    'Abdul-Rahman bin Abdulaziz Al Saud':'Hassa Al Sudairi', 
    'Mishaal bin Abdulaziz Al Saud':'Shahida', 
    'Talal bin Abdulaziz Al Saud':'Munaiyir', 
    'Muhammad bin Abdulaziz Al Saud':'Al Jawhara bint Musaed Al Jiluwi', 
    'Mutaib bin Abdulaziz Al Saud':'Shahida', 
    'Bandar bin Abdulaziz Al Saud':'Bazza II', 
    'Ahmed bin Abdulaziz Al Saud':'Hassa Al Sudairi', 
    'Mashhur bin Abdulaziz Al Saud':'Nouf bint Al Shalan', 
    'Nayef bin Abdul-Aziz Al Saud':'Hassa Al Sudairi', 
    'Khalid bin Abdulaziz':'Al Jawhara bint Musaed Al Jiluwi', 
    'Fahd bin Abdulaziz':'Hassa Al Sudairi', 
    'Sultan bin Abdulaziz Al Saud':'Hassa Al Sudairi', 
    'Faisal bin Abdulaziz':'Tarfah bint Abdullah Al Sheikh', 
    'Muqrin bin Abdulaziz':'Baraka Al Yamaniyah', 
    'Saud bin Abdulaziz Al Saud':'Wadhah bint Muhammad Al Hussein Al Orair', 
    'Abdullah bin Abdulaziz':'Fahda bint Asi bin Shuraim Al Shammari'}
    
    cluster = MongoClient("mongodb+srv://dbUser:UzzyHaydos@cluster0-dd4a8.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
    db = cluster["test"]
    collection = db["saudi_descriptions"]

    def parse(self, response):
        for href in response.css("#main > div:nth-child(4) > div > div:nth-child(2) > div > div > div>div> a[href]"):
            yield response.follow(href, self.parse_son)

    def parse_son(self,response):
        x = response.xpath('//span[.="Children"]//following-sibling::span//span[.="more"]/a/@href')
        deadstatus = response.xpath('//span[.="Died"]')
        if deadstatus:
            deadstatus = True
        else:
            deadstatus = False

        if x:
            name = response.css("#main > div:nth-child(5) > div > div> span > div::text").get()
            name = re.sub(r'of.*', 'bin Abdulaziz',str(name))
            self.mdict[str(name)] = []
            for href in x:
                    if name in self.exceptions:
                        yield response.follow(self.exceptions[name],self.parse_grandson)
                    else:
                        yield response.follow(href, self.parse_grandson)
        
        else:
            description = response.css("#main > div:nth-child(5) > div > div > div:nth-child(2) > div > div > div > div::text").get()
            name = response.css("#main > div:nth-child(5) > div > div> span > div::text").get()
            born = response.xpath('//span[.="Born"]/following-sibling::span/span//text()').extract_first()
            if born:
                born = int(re.search(r'19[0-9]{2}',born).group(0))
            else:
                born=""
            one_child = response.xpath('//span[.="Children"]//following-sibling::span//span//span//span/text()').extract()
            if one_child:
                one_child[:] = [x for x in one_child if not re.search(r'bint',x)]
                self.mdict[str(name)] = Lineage(name,one_child, deadstatus,born,self.mothers[name],False,description).__dict__
            else:
                if name == 'Khalid I bin Abdulaziz':
                    return
                self.mdict[str(name)] = Lineage(name,[],deadstatus,born,self.mothers[name],False,description).__dict__

    
    def parse_grandson(self, response):

        #or
        #response.css("#main > div:nth-child(5) > div > div > div:nth-child(2) > div > div > div > div::text").get()
        #(4 divs in)
        name = response.css("#main > div:nth-child(5) > div > div> span > div::text").get()
        description = response.css("#main > div:nth-child(5) > div > div > div:nth-child(2) > div > div > div > div::text").get()
        king = False
        if re.search(r'of.*', str(name)):
            king = True
            name = re.sub(r'of.*', 'bin Abdulaziz',str(name))
        deadstatus = response.xpath('//span[.="Died"]')
        if deadstatus or name in ['Faisal bin Abdulaziz','Mishaal bin Abdulaziz Al Saud']:
            deadstatus = True
        else:
            deadstatus = False
        born = response.xpath('//span[.="Born"]/following-sibling::span/span//text()').extract_first()
        try:
            born = int(re.search(r'19[0-9]{2}',born).group(0))
        except:
            born=""
            print("born fail:", born," name:",name)

        sons = response.css("#main > div:nth-child(4) > div > div:nth-child(2) > div > div > div > div").css('div>div::text').getall()
        sons[:] = [x for x in sons if not re.search(r'bint',x, re.IGNORECASE)]
        sons[:] = [x for x in sons if re.search(r'bin',x, re.IGNORECASE)]
        sons[:] = [re.sub(r'bin.*',f'bin {name}',x, flags = re.IGNORECASE) for x in sons]
        if name:
            self.mdict[str(name)] = Lineage(name,sons,deadstatus,born,self.mothers[name],king,description).__dict__
            
        if len(self.mdict)==36:
            print(self.mdict)
        
        if len(self.mdict) == 36:
            if self.mdict[list(self.mdict.keys())[-1]] != []:
                print("inserting!")
                self.collection.insert_many(self.mdict.values())
                


