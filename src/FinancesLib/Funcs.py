#!/usr/bin/python

import numpy as np

def get_matrix_from_func2(vec1,vec2,func2):
    N1 = vec1.size;
    N2 = vec2.size;
    
    Mat=np.zeros((N1,N2));
    
    for n1 in range(N1):
        for n2 in range(N2):
            Mat[n1][n2]=func2(vec1[n1],vec2[n2]);
    return Mat;
