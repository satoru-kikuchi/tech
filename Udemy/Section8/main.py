from termcolor import cprint
import string
import csv


hello_template = """\
================================================
こんにちは！私はRobokoです。あなたの名前は何ですか？
Hello, I am Roboko. What is your name?
================================================
"""

question_template = """\
================================================
$nameさん、どこのレストランが好きですか？
$name, which restaurants do you like?
================================================
"""

recommend_template = """"\
================================================
私のオススメのレストランは$recommend$です
I recommend $recommend restaurant.

このレストランは好きですか？[Yes/No]
Do you like it?[y/n]
================================================
"""

def main():
    
    # 名前を入力してもらう
    cprint(hello_template, 'green', end='')
    name = input()
    
    # オススメのレストランを入力してもらう
    question = string.Template(question_template).substitute(name=name)
    cprint(question, 'green', end='')
    restaurant = input()
    
    # 名前、レストランをcsvに書き出す
    with open('ranking.csv', 'a+') as csv_file:
        
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        

if __name__ == '__main__':
    main()
    