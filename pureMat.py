# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 20:28:02 2021

@author: balle
"""

class MyMatrix:
    """Cette classe implémente une matrice comme étant une liste de listes. 
    Chaque liste étant une ligne. La matrice doit donc être instanciée comme 
    [[1,4,9],[12,-3,0],[12,0,0], ...]"""
    
    def __init__(self,coeffs):            
        self.coeffs = coeffs
        self.nrow = len(coeffs)
        self.ncol = len(coeffs[0])
            
    def dim(self):
        """Retourne le format (n,p) de la matrice"""
        return (self.nrow,self.ncol)
        
    def coeff(self,i,j):
        """Retourne le coefficientient i,j """
        return self.coeffs[i][j]
    
    def isSquare(self):
        """Retourne si la matrice est carree"""
        if self.nrow == self.ncol:
            return True
        else:
            return False
    def t(self):
    #return [[self.coeffs[j][i] for j in range(self.ncol)] for i in range(self.nrow)]
        transposee = [list(i) for i in zip(*self.coeffs)]
        return MyMatrix(transposee)
    
    def equal(self,other):
        """Teste l'égalité coefficient par conefficient entre deux matrices """
        return self.coeffs == other.coeffs
            
    def sym(self):
        """Teste la symétrie de la matrice"""
        return self.coeffs == self.t()
    
    def __add__(self,other):
        """Somme de deux matrices """
        if self.dim() == other.dim():
            k = self.ncol
            # sum(self.coeffs,[]) fusionne self.coeffs en une seule liste
            m = [i+j for (i,j) in zip(sum(self.coeffs,[]), sum(other.coeffs,[]))] 
            # Redonner le format liste de listes
            sum_mat = [m[i:i+k] for i in range(0,len(m),k)]
            return MyMatrix(sum_mat)
        else:
            print('Somme impossible')
            
    def __neg__(self):
        """Opposé de la matrice"""
        k = self.ncol
        # Calculer l'opposé de toute la matrice fusionnée 
        neg_mat=[-i for i in sum(self.coeffs,[])]
        # Redonner à la matrice fusionnée la forme attendue par la classe
        ng_mat=[neg_mat[i:i+k] for i in range(0,len(neg_mat),k)] 
        return MyMatrix(ng_mat)         
            
    def __sub__(self,other):
        """Retourne la differnce de deux matrices"""
        if self.dim() == other.dim():
            return self.__add__(other.__neg__())
        else:
            print("Différence Impossible")
    
    def __mul__(self,other):
        """Effectue le produit entre deux matrices"""
        if self.ncol == other.nrow: #le nombre de colonne de la premiere doit valoir le nombre de ligne de la seconde
            k = self.nrow
            res0 = [0 for i in range(self.nrow*other.ncol)] # Liste vide de 0 
            result = [res0[i:i+k] for i in range(0,len(res0),k)] # liste vide de 0 de la forme attendue par la classe
            
            for i in range(k):
                for j in range(other.ncol):
                       for k in range(other.nrow):
                               result[i][j] += self.coeffs[i][k] * other.coeffs[k][j]
            return MyMatrix(result)
        else:
            print("Produit Impossible")
            
    def minor(self,i,j):
        """Retourne le mineur d'ordre i, j"""
        m = self.coeffs
        return MyMatrix([row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])])
            
    
    def det(self):
        """Retourne le déterminant pour une matrice carrée"""        
        if self.isSquare():
            coeffs = self.coeffs
          # Initialisation pour une matrice carrée 2 x 2
            if self.nrow == 2:
                return coeffs[0][0]*coeffs[1][1]-coeffs[0][1]*coeffs[1][0]
          # Cas général
            det = 0
            for c in range(self.nrow):
                det += ((-1)**c)*coeffs[0][c]*(self.minor(0,c).det())
            return det          
        else:
            print("Le déterminant n'est défini que pour les matrices carrées")       
            
            
    def inv(self):
        """Retourne l'inverse de la matrice """
        m = self.coeffs
        determinant = self.det()
        # Cas de base matrice 2 x 2
        if self.nrow == 2:
            return MyMatrix([[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]])
    
        #Calcul de la matrice des cofacteurs
        m=MyMatrix(m)
        cofactors = []
        for r in range(m.nrow):
            cofactorRow = []
            for c in range(m.nrow):
                minor = m.minor(r,c)
                cofactorRow.append(((-1)**(r+c)) * minor.det())
            cofactors.append(cofactorRow)
            
        cofactors = [list(i) for i in zip(*cofactors)]
        
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = (cofactors[r][c]/determinant)
        
        return MyMatrix(cofactors)     
            
            
    def solve(self,b):
        """Retourne la solution d'une equation de la forme AX = b """
        if self.det() != 0:
            inverse = self.inv().coeffs
            return [sum([i*j for i, j in  zip(inverse[k],b)]) for k in range(len(inverse))]
            
        else:
            print("Equation insoluble")
    def demo(self,a):
        print('bonjour')
            