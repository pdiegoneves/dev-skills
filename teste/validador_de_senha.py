def validar_senha(senha):
    if not len(senha) >= 8:
        return False
    
    count_nums = 0
    for char in senha:
        try:
            int(char)
            count_nums += 1
        except:
            pass
        
    if not count_nums >= 1:
        return False

    return True
    

senha1 = "senha123"
senha2 = "senhaabc"
    
print(validar_senha(senha=senha1))
print(validar_senha(senha=senha2))


class RegraValidacao():
    def validacao(self):
        pass
    
class RegraMinimo8Chars(RegraValidacao): 
    def validacao(self, senha):
        return len(senha) >= 8

class RegraMinimo1Num(RegraValidacao):
    QUANTIDADE_MINIMA_NUMS = 1
    
    def validacao(self, senha):
        count_nums = 0
        for char in senha:
            try:
                int(char)
                count_nums += 1
            except:
                pass
        
        if not count_nums >= self.QUANTIDADE_MINIMA_NUMS:
            return False
        
        return True

    

def validar_senha(senha, regra: RegraValidacao):
    regra = regra()
    return regra.validacao(senha)
    

senha = "senha123"
    
print(validar_senha(senha=senha, regra=RegraMinimo8Chars))
print(validar_senha(senha=senha, regra=RegraMinimo1Num))