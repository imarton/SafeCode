'''
Created on 2017. ápr. 10.

@author: István
'''
import logging


logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(message)s')
log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)

class CodeGenerator:
    
    codeLen = 6 #milyen hosszú a széf kód
    pos = [] # széfkód pozíciók
    
    result = [] # kulcsok halmaza, amely megfelel a feltételeknek
    
    def initPos(self):
        for i in range(self.codeLen):
            self.pos.append(i)
#         log.debug("Init Pos: " + self.pos.__str__())
        log.debug("Kód számjegyeinek száma: {}".format(self.pos))

    def generateKeys(self):
        
        self.initPos()
        # összes lehetséges 3 jegyű kulcs előállítása
        keySet = self.getCombination(self.pos, 3)
        log.debug("Kulcs készlet: {}".format(keySet))
        # az halmazból tizet kell kiválasztani az összes leheteséges módon 
        # és ellenőrizni hogy a tizes megfelel-e a feltételeknek
        return self.getCombination(keySet, 10, True)
        
    
    def getCombination(self, cList, k, needValidation=False):
        subsets = []
        
        s = [] # indexek nyilvántartása
            
        if(k <= len(cList)):
            
            for i in range(k): #indexek inicializálása
                s.append(i)
                
            ss = self.getSubset(cList, s)
            if needValidation :
                if self.isValid(ss) :
                    subsets.append(ss)
            else:
                subsets.append(ss)
            
            while True:
                
                # pizicio keresése, amelyet lehet novelni
                boo = True
                i = k-1
                while boo:
                    if i<0 or s[i] != len(cList)-k+i :
                        boo = False
                    else :
                        i-=1
                
                if i<0 :
                    break
                else :
                    s[i] += 1
                    i+=1
                    while i<k :
                        s[i] = s[i - 1] + 1; 
                        i+=1
                    
                    ss = self.getSubset(cList, s)   
                    if needValidation :
                        if self.isValid(ss) :
                            subsets.append(ss)
                    else:
                        subsets.append(ss) 


        return subsets
    
    cnt = 1   
    def isValid(self, keySet):  
        log.debug("{}. Kulcsok: {}".format(self.cnt,keySet))
        self.cnt+=1      
        # Vizsgálat 1: van-e olyan kulcspár ami kiadja az egész kódot
        allDuo = self.getCombination(keySet, 2)
        log.debug("Kulcspárok: {}".format(allDuo))
        allIn = {0,1,2,3,4,5}                
        for d in allDuo:
#             print("Duo: {}".format(d))
            c = set(d[0]) | set(d[1])
            dif = allIn - c
#             print("len: {} diff: {}".format(len(dif), dif))
            if len(dif) == 0 : #ha van ilyen akkor nem érvényes a kulcskészlet
                log.debug("Hibás kulcspár: {}".format(d))
                return False
        
        # Vizsgálat 2: Bármely kulcs hármas kiadja-e az egész kódot
        allTrio = self.getCombination(keySet, 3)
        log.debug("Kulcshármasok: {}".format(allTrio))
        for t in allTrio:
#             print("Trio: {}".format(t))
            c = set(t[0]) | set(t[1]) | set(t[2])
            dif = allIn - c
#             print("len: {} diff: {}".format(len(dif), dif))
            if len(dif) != 0 : #ha van olyan ami nem akkor nem érvényes a kulcskészlet
                log.debug("Hibás kulcshármas: {}".format(t))
                return False 
        
        return True
                
    def getSubset(self, sinput, subset):
        '''
        Előállítja az indexeknek megfelelő részhalmazt
        '''
        ret = []
        for i in range(len(subset)):
            ret.insert(i, sinput[subset[i]])
        #log.debug("subset: {}".format(ret))
        return ret


if __name__ == '__main__':
    cg = CodeGenerator()
#     print(cg.getSubset([1,2,3,4,5,6], [0,1,4]))

#     comb = cg.getCombination([1,2,3,4,5,6], 3) 
#     print(len(comb))
#     print(comb)
#     s = [[0,1],[0,2],[0,3],[1,2],[1,3]]
#     cg.isValid(s)
    
    print(cg.generateKeys())
