# h3avren

# imports
import os
import sys
from pmd_scanner import Scanner

class PMD:
    def __init__(self) -> None:
        self.had_errors = False
    
    def run_file(self, path):
        with open(path, 'r') as file:
            text = file.read()
        self.run(text)
        
    def run_prompt(self):
        while True:
            try:
                print(">", end = " ")
                line = input()
            except EOFError:
                break
            self.run(line)
    
    def report(self, line_num, message):
        print(f"[line {line_num} ] Error {where} : {message}")
        self.had_error = True
    
    def error(self, line_num, message):
        self.report(line_num, "", message)
    
    def run(self,line): # Runs the code line by line
        scanner_obj = Scanner(line,self)
        tokens = scanner_obj.scan_tokens()
        for i in tokens:
            print(i)

interpreter = PMD()

if(len(sys.argv) > 2):
    print("Usage : python3 pmd.py [script]")
    sys.exit(64)
elif(len(sys.argv) == 2):
    interpreter.run_file(sys.argv[1])
else:
    interpreter.run_prompt()