import random
import sys

def print_matrix(mat):
        for l in mat:
                print(l)
        print("\n\n\n")

def generate_matrix(size):
        mat = []
        for _ in xrange(size):
                temp_arr = []
                for _ in xrange(size):
                        temp_arr.append(random.randint(1,101))
                mat.append(temp_arr)
        return mat

def matrix_rotation(size):
        mat = generate_matrix(size)        
        print_matrix(mat)        
        for i in xrange(size/2+1):
                for j in xrange(i,size-i):
                        print("j = " + str(j))
                        temp = mat[i][j]
                        mat[i][j] = mat[size-i][j]
                        mat[size-i][j] = mat[size-j][size-i]
                        mat[size-j][size-i] = mat[i][size-j]
                        mat[i][size-j] = temp
        print_matrix(mat)            

if __name__ == '__main__':
        matrix_rotation(int(sys.argv[1])-1)
