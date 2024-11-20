# Sistema de Autenticação de Funcionários

## Sobre

Este projeto implementa um sistema de autenticação para diferentes tipos de funcionários em uma empresa, como **Gerente**, **Operador de Caixa** e **Segurança**, utilizando conceitos de **Programação Orientada a Objetos (POO)** e **classes abstratas**. O sistema tem como objetivo autenticar usuários com base em diferentes parâmetros, como CPF, número do caixa ou posto de segurança, dependendo do tipo de funcionário.

## Funcionalidades

- **Autenticação de Funcionários**: Cada tipo de funcionário (Gerente, Operador de Caixa, Segurança) utiliza um parâmetro diferente para autenticação:
  - **Gerente**: Utiliza o CPF para validar o usuário.
  - **Operador de Caixa**: Utiliza o número do caixa para validar o usuário.
  - **Segurança**: Utiliza o posto para validar o usuário.
  
- **Métodos Adicionais**: Cada classe tem métodos adicionais que retornam mensagens representativas, como o método `acionarAlarme` na classe **Segurança**.

## Diagrama de Classes

O diagrama de classes abaixo ilustra a estrutura do sistema e os relacionamentos entre as classes:

![Captura de tela 2024-11-20 145426](https://github.com/user-attachments/assets/b5835cb8-5f3b-4d1f-b303-30d5e92da6a5)

