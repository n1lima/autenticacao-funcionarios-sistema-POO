from funcionario import *

if __name__ == '__main__':

    gerente = Gerente('nicoly', '823738', 3673)
    if gerente.autenticar('823738', 3673):
        print(gerente.cancelar_operador())
    else:
        print('FALHA')

    op_caixa = Operador_Caixa('haru', '3783', 8392, 2)
    if op_caixa.autenticar('5', 3783):
        print(op_caixa.registrar_produto())
    else:
        print('FALHA')

    seguranca = Seguranca('kika', '37632', 63535, 4)
    if seguranca.autenticar('4', 63535):
        print(seguranca.acionar_alarme())
    else: 
        print('FALHA')