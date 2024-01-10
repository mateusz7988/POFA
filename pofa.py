

import numpy as np

#rezonator prostopadloscienny

def freq1(v, m, n, p, h = 0.148, a = 0.248, b = 0.124):

    f = v/2 * np.sqrt((m/a)**2 + (n/b)**2 + (p/h)**2)
    #print(f)
    f = f / 10**9
    return f


def freq2(v, xi, p, a = 0.093, h = 0.032):
    f = v/(2*np.pi) * np.sqrt((xi/a)**2 + (p*np.pi/h)**2)
    #print(f)
    f = f / 10**9
    return f


m =  [0, 1, 2]
n =  [0, 1, 2]
p =  [0, 1, 2]

m2 = [0 ,1, 2, 3]
n2 = [1, 2, 3]
p2 = [0, 1]

if __name__ == "__main__":

    er = 2


    v = 3*10**8

    v_er = v/np.sqrt(er)

    freq1(v, 1, 1, 1)

    for i in m:
        for j in n:
            for k in p:
                print(f"Frequency calculated for E{i}{j}{k}: {freq1(v, i, j, k)} \n" 
                      f"Frequency calculated for E{i}{j}{k} but with different Er: {freq1(v_er, i, j, k)}")



    xi = np.array([[999, 2.405, 5.520, 8.654], [999, 3.832, 7.016], [999, 5.136, 8.417], [999, 6.380]])
    xi_prim = np.array([[999, 3.832, 7.016, 10.173], [999, 1.841, 5.331], [999, 3.054, 6.706], [999, 4.201]])
 
    print(xi_prim[0][0])

    print("NOW CALCULATING RESULT FOR ROUND RESONATORS")


    for i in m2:
        for j in n2:
            for k in p2:
                if k==0:
                    try:
                        print(f"Frequency calculated for E{i}{j}{k}: {freq2(v, xi[i][j], k)} \n" 
                        f"Frequency calculated for E{i}{j}{k} but with different Er: {freq2(v_er, xi[i][j], k)}")
                    except Exception as e:
                        # Code to handle other exceptions (general exception handling)
                        print(f"An error occurred: {e}")
                if k==1:
                    try:
                        print(f"Frequency calculated for E{i}{j}{k}: {freq2(v, xi_prim[i][j], k)} \n" 
                        f"Frequency calculated for E{i}{j}{k} but with different Er: {freq2(v_er, xi_prim[i][j], k)}")
                    except Exception as e:
                        # Code to handle other exceptions (general exception handling)
                        print(f"An error occurred: {e}")