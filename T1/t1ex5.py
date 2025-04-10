'''

Exercícios 05
    Enunciado: Árvore Genealógica

    Imagine que você recebeu a tarefa de criar uma árvore genealógica para uma família.
    
    A árvore deve ser capaz de armazenar informações sobre várias gerações de uma família e suas relações.

    Requisitos:

        Modelo de Dados:

            Cada membro da família deve ser representado como um dicionário contendo: nome, idade, sexo e uma lista de filhos.
            
            A lista de filhos de cada membro da família deve conter dicionários representando cada filho.
            
            Funções a serem implementadas:

                adicionar_membro(nome, idade, sexo, pai=None):
                    
                    Adiciona um membro à árvore genealógica.
                    
                    Se o pai for especificado, o membro é adicionado como filho desse pai.
                    
                buscar_membro(nome):

                    Retorna o dicionário representando o membro da família com o nome especificado. 
                
                descendentes(nome):
                    
                    Retorna uma lista de todos os descendentes do membro com o nome especificado.
                    
                    Esta função deve ser implementada de forma recursiva. 
            
            Exemplo de Uso:

                Adicione um membro chamado "João" com 70 anos.
                
                Adicione um filho para "João" chamado "Carlos" com 50 anos.
                
                Adicione um filho para "Carlos" chamado "Pedro" com 30 anos.
                
                Adicione um filho para "Pedro" chamado "Lucas" com 10 anos.
                
                Ao chamar a função descendentes("João"), ela deve retornar uma lista contendo "Carlos", "Pedro" e "Lucas".
                
        Desafio Extra:

        Implemente uma função antepassados(nome) que, dado o nome de um membro, retorna uma lista de todos os seus antepassados diretos (pai, avô, bisavô, etc.).
        
        Esta função também deve ser implementada de forma recursiva.
        
        Este enunciado exige que o aluno utilize listas para armazenar os filhos de cada membro, dicionários para armazenar informações sobre cada membro e recursividade para buscar descendentes e antepassados.
'''


class ArvoreGenealogica:
    def __init__(self):
        self.membros = []

    def adicionar_membro(self, nome, idade, sexo, pai=None):
        #criar dicionário novo membro
        novo_membro = {'nome': nome, 'idade': idade, 'sexo': sexo, 'filhos': [], 'pai': pai}
        
        # se um pai for especificado, adicionar o novo membro como filho
        if pai:
            pai_encontrado = self.buscar_membro(pai)
            if pai_encontrado:
                pai_encontrado['filhos'].append(novo_membro)
        
        # adicionar membro à lista de membros da árvore
        self.membros.append(novo_membro)
