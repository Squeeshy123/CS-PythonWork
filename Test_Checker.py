input_file = open(input("Students Answers: "), 'r')
answers_file = open(input("Answer Sheet path: "), 'r')

def check_answer(line):
    line.readline