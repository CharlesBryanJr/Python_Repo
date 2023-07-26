'''interfaces.py'''
print(" ")

class A:
    pass

class RunCodeInterface:
    
    def compile_code(self):
        raise NotImplementedError("compile_code() not implemented")

    def excute_code(self):
        raise NotImplementedError("excute_code() not implemented")

class GoCode(A, RunCodeInterface):

    def compile_code(self):
        print("GoCode: compile_code")
    
    def excute_code(self):
        print("GoCode: excute_code")

class JavaCode(A, RunCodeInterface):

    def compile_code(self):
        print("JavaCode: compile_code")
    
    def excute_code(self):
        print("JavaCode: excute_code")
    
    def B(self):
        print("Hello World")

def run_code(code : RunCodeInterface):
    code.compile_code()
    code.compile_code()
    #code.B()

go = GoCode()
run_code(go)
print(" ")
java = JavaCode()
run_code(java)

print(" ")