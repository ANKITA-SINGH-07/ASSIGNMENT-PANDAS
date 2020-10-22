import pandas as pd
import pycountry_convert as pc

class StackOverFlowAnalysis():
    def __init__(self, input_file):
        self.data=pd.read_csv(input_file, encoding='unicode_escape')
    def avgAgeOfDeveleoper(self):
        try:
            avgAge=int(self.data['Age1stCode'].mean())
            print("Average age of Developer :{}".format(avgAge))
        except Exception as e:
            print("Exception/Error Occured:{}".format(e))
    def pythonDeveForCountry(self,country='All'):
        try:
            total=self.data['Respondent'].agg('count')
            if country=='All':
                final=self.data[self.data['LanguageWorkedWith'].str.contains('Python')].groupby("Country").agg('count')['Respondent']/total*100
            else:
                final=self.data[self.data['LanguageWorkedWith'].str.contains('Python')&self.data['Country'].str.contains(country)].groupby("Country").agg('count')['Respondent']/total*100
            print(final)
        except Exception as e:
            print("Exception/Error occured:{}".format(e))
    def avgSalOfDeve(self,continent='All'):
        try:
            self.data['continent']=self.data.apply(lambda x: pc.country_alpha2_to_continent_code(pc.country_name_to_country_alpha2(x['Country'], cn_name_format="default")),axis=1)
            if continent=='All':
                res=self.data.fillna(0).groupby('continent')['ConvertedComp'].mean()
            else:
                res=self.data[self.data['continent']==continent].fillna(0).groupby('continent')['ConvertedComp'].mean()
            print(res)

        except Exception as e:
            print("Exception/Error occured:{}".format(e))

    def hobbyAsCode(self,continent="All"):
    #Returns distribution of people who code as hobby.
        try:
            
            self.data['continent']=self.data.apply(lambda x: pc.country_alpha2_to_continent_code(pc.country_name_to_country_alpha2(x['Country'], cn_name_format="default")),axis=1)
            if continent=='All':
                code=self.data.fillna(0).groupby("continent ")[(self.data['Hobbyist']=='Yes')].value_counts()
            else:
                code=self.data[self.data['continent']==continent].fillna(0).groupby('continent')[(self.data['Hobbyist'] =='Yes')].value_counts()
            print(code)

        except Exception as e:
            print("Exception/Error occured:{}".format(e))
    def hobbyAsCodeGenderWise(self):
    #Returns distribution of people who code as hobby based on gender.
        try:
          
                counter=self.data.fillna(0).groupby("Gender")[(self.data['Hobbyist'] =='Yes')].value_counts()
                print(counter)
            
            
        except Exception as e:
            print("Exception/Error occured:{}".format(e)) 
    def mostPopularLanguage(self):
        #Returns most popular language people wish to learn in year 2020
        ques3_data = self.data['LanguageDesireNextYear'].dropna() 
        languages = {}
        for row in ques3_data:
            for language in row.split(";"):
                try:
                    languages[language] = languages[language] + 1
                except:
                    languages[language] = 1
        #print(languages)
        sorted_languages = sorted(languages.items(), key = lambda kv:(kv[1], kv[0]))
        sorted_languages.reverse()
        print(sorted_languages)
    def jobSatisfacton(self,continent="All"):
    #Returns Job Satisfaction of Developers based on continent
        try:
            
            self.data['continent']=self.data.apply(lambda x: pc.country_alpha2_to_continent_code(pc.country_name_to_country_alpha2(x['Country'], cn_name_format="default")),axis=1)
            if continent=='All':
                code=self.data.fillna(0).groupby("continent ")['JobSat'].value_counts()
            else:
                code=self.data[self.data['continent']==continent].fillna(0).groupby('continent')['JobSat'].value_counts()
            print(code)

        except Exception as e:
            print("Exception/Error occured:{}".format(e))    

             
if __name__ =='__main__':
    a=StackOverFlowAnalysis("ankita_10_records.csv")
    a.avgAgeOfDeveleoper()
    a.pythonDeveForCountry("Kingdom")
    a.avgSalOfDeve("AS")
    a.hobbyAsCode("AS")
    a.hobbyAsCodeGenderWise("Man")
    a.mostPopularLanguage()
    a.jobSatisfacton()

        


