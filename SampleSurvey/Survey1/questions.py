#This class holds the questions that are to be asked in the survey

class AllQuestions:
    allQuestions = {
        1:{'q':'This is Question 1', '1':'This is option 1', '2':'This is option 2', '3':'This is option 3'},
        2:{'q':'This is Question 2', '1':'This is option 1', '2':'This is option 2', '3':'This is option 3'},
        }        
    
    def getQuestion(self, num):
        return self.allQuestions[num]

    def numQuestions(self):
        return 2
