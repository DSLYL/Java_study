import numpy as np
import sys


def LU_deco_inverse(m):
    dim = m.shape[0]
    E = np.mat(np.eye(dim))
    L = np.mat(np.eye(dim))
    U = m.copy()
    for i in range(dim):
        if abs(m[i, i]) < 1e-8:
            print("zero pivot encoUnted")
            sys.exit()
        L[i + 1:, i] = U[i + 1:, i] / U[i, i]
        E[i + 1:, :] = E[i + 1:, :] - L[i + 1:, i] * E[i, :]
        U[i + 1:, :] = U[i + 1:, :] - L[i + 1:, i] * U[i, :]

    print("\nLU分解后的L,U矩阵:")
    print("L=", L)
    print("U=", U)
    print("将A化为上三角阵U后随之变换的E矩阵:")
    print("E=", E)
    E1 = np.mat(np.eye(dim))
    for i in range(dim - 1, -1, -1):
        # 对角元单位化
        E[i, :] = E[i, :] / U[i, i]
        E1[i, :] = E1[i, :] / U[i, i]
        U[i, :] = U[i, :] / U[i, i]

        E[:i, :] = E[:i, :] - U[:i, i] * E[i, :]
        E1[:i, :] = E1[:i, :] - U[:i, i] * E1[i, :]
        U[:i, :] = U[:i, :] - U[:i, i] * U[i, :]  # r_j = m_ji - r_j*r_i

    print("\n将上三角阵U变为单位阵后的U和随之变换后的E分别为:")
    print("U=", U)
    print("E=", E)
    print("使用系统自带的求inverse方法得到的逆为:")
    print("m_inv=", m.I)
    print("\nU的逆E1为:")
    print("E1=", E1)

    E2 = np.mat(np.eye(dim))
    for i in range(dim):
        E2[i + 1:, :] = E2[i + 1:, :] - L[i + 1:, i] * E2[i, :]
        L[i + 1:, :] = L[i + 1:, :] - L[i + 1:, i] * U[i, :]

    print("\n将下三角阵L变为单位阵后的L和随之变换后的E2分别为:")
    print("L=", L)
    print("E2=", E2)

    print("\n由A=LU,得A逆=U的逆*L的逆")
    print("U的逆E1*L的逆E2=", E1 * E2)


if __name__ == "__main__":
    A = np.mat([[5., 4, 3], [2, 4, 9], [5, 0, 11]])
    A_dim = A.shape[0]

    LU_deco_inverse(A)
