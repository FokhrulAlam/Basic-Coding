#Write a program that asks the user to enter five test scores. The program should display a lettergrade
# for each score and the average test score. Write the following functions in the program:
# •calc_average—This function should accept five test scores as arguments and returnthe average of the scores.
# •determine_grade—This  function  should  accept  a  test  score  as  an  argument  andreturn a letter grade for the
# score, based on the following grading scale:
#    ScoreLetter Grade
#   90–100                A
#   80–89                 B
#   70–79                 C
#   60–69                 D
#   Below 60             F

def calc_average(a,b,c,d,e):
    average=(a+b+c+d+e)/5
    return int(average)

def determine_grade(score):
    if score>=90:
        return 'A'
    if score>=80 and score<=89:
        return 'B'
    if score>=70 and score<=79:
        return 'C'
    if score >=60 and score<=69:
        return 'D'
    if score <60:
        return 'F'

def ask_score():
    print("Please enter five test scores below: ")
    score1=int(input("score1= "))
    score2=int(input("score2= "))
    score3=int(input("score3= "))
    score4=int(input("score4= "))
    score5=int(input("score5= "))
    return score1,score2,score3,score4,score5

def printing_grade(score1,score2,score3,score4,score5):
    print("\nScore\tLetter Grade\n------\t----------")
    print(str(score1)+ '\t\t'+ determine_grade(score1)+'\n'+str(score2)+'\t\t'+determine_grade(score2)+'\n'+\
          str(score3)+'\t\t'+determine_grade(score3)+'\n'+str(score4)+'\t\t'+determine_grade(score4)+'\n'\
          +str(score5)+'\t\t'+determine_grade(score5))

def main():
    score1,score2,score3,score4,score5=ask_score()
    printing_grade(score1,score2,score3,score4,score5)
    print("The average score is ",calc_average(score1,score2,score3,score4,score5))

main()